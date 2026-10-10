#!/usr/bin/env python3
"""2.5D camera move from one photo: depth-estimated parallax, rendered to MP4 on CPU.

    python tools/parallax.py photo.jpg out.mp4 --move push --seconds 4 [--amount 1]

Moves: push (dolly in), pull (dolly out), left / right (truck sideways, near
things slide faster than far ones, like a short orbit), rise, sink.
Depth comes from Depth Anything V2 Small (Apache-2.0) as ONNX; pass --model or
set DEPTH_MODEL to the .onnx path (huggingface.co/onnx-community/depth-anything-v2-small).
Setup: pip install onnxruntime opencv-python-headless numpy
"""
import argparse, os, subprocess
import cv2
import numpy as np


def depth_map(img, model):
    import onnxruntime as ort
    h, w = img.shape[:2]
    ih, iw = 518, int(round(518 * w / h / 14)) * 14
    x = cv2.resize(img, (iw, ih), interpolation=cv2.INTER_CUBIC)[:, :, ::-1].astype(np.float32) / 255
    x = (x - [0.485, 0.456, 0.406]) / [0.229, 0.224, 0.225]
    x = x.transpose(2, 0, 1)[None].astype(np.float32)
    sess = ort.InferenceSession(model, providers=['CPUExecutionProvider'])
    d = sess.run(None, {sess.get_inputs()[0].name: x})[0][0]
    d = (d - d.min()) / (d.max() - d.min() + 1e-6)          # 1 = near, 0 = far
    # grow near regions a little and soften, so edges stretch the background, not the car
    d = cv2.dilate(d, np.ones((7, 7), np.uint8))
    d = cv2.GaussianBlur(d, (0, 0), 3)
    return cv2.resize(d, (w, h), interpolation=cv2.INTER_CUBIC)


def ease(t):
    return t * t * (3 - 2 * t)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('image')
    ap.add_argument('out')
    ap.add_argument('--move', default='push', choices=['push', 'pull', 'left', 'right', 'rise', 'sink'])
    ap.add_argument('--seconds', type=float, default=4)
    ap.add_argument('--amount', type=float, default=1, help='strength multiplier')
    ap.add_argument('--size', default='1920x1080')
    ap.add_argument('--fps', type=int, default=30)
    ap.add_argument('--model', default=os.environ.get('DEPTH_MODEL', 'models/depth-anything-v2-small.onnx'))
    a = ap.parse_args()

    W, H = map(int, a.size.split('x'))
    src = cv2.imread(a.image)
    # cover the frame with 12% margin for the move, upscale with Lanczos + light sharpen
    s = max(W / src.shape[1], H / src.shape[0]) * 1.12
    img = cv2.resize(src, (round(src.shape[1] * s), round(src.shape[0] * s)), interpolation=cv2.INTER_LANCZOS4)
    blur = cv2.GaussianBlur(img, (0, 0), 1.2)
    img = cv2.addWeighted(img, 1.35, blur, -0.35, 0)
    depth = depth_map(img, a.model).astype(np.float32)

    h, w = img.shape[:2]
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    cx, cy = w / 2, h / 2
    x0, y0 = (w - W) // 2, (h - H) // 2
    k = a.amount
    frames = round(a.seconds * a.fps)
    ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'bgr24',
                           '-s', f'{W}x{H}', '-r', str(a.fps), '-i', '-', '-c:v', 'libx264', '-crf', '16',
                           '-preset', 'medium', '-pix_fmt', 'yuv420p', a.out], stdin=subprocess.PIPE)
    for f in range(frames):
        t = ease(f / max(frames - 1, 1))
        zoom, dx, dy = 1.0, 0.0, 0.0
        if a.move in ('push', 'pull'):
            p = t if a.move == 'push' else 1 - t
            zoom = 1 + 0.10 * k * p * (0.35 + depth)           # near things grow faster
        elif a.move in ('left', 'right'):
            dx = (1 if a.move == 'left' else -1) * (t - 0.5) * 0.09 * w * k * (depth - 0.35)
            zoom = 1 + 0.03 * k
        else:
            dy = (1 if a.move == 'sink' else -1) * (t - 0.5) * 0.08 * h * k * (depth - 0.35)
            zoom = 1 + 0.03 * k
        mx = cx + (xx - cx) / zoom - dx
        my = cy + (yy - cy) / zoom - dy
        frame = cv2.remap(img, mx, my, cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
        ff.stdin.write(np.ascontiguousarray(frame[y0:y0 + H, x0:x0 + W]).tobytes())
    ff.stdin.close()
    ff.wait()
    print(a.out)


if __name__ == '__main__':
    main()
