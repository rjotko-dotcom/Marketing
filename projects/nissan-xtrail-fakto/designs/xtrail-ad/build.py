#!/usr/bin/env python3
"""Build the 30 s X-Trail × Fakto Auto ad (1920x1080) from official press photos.

    python build.py            # clips -> edit -> overlay -> music -> final MP4

Footage: Nissan Europe press photos (europe.nissannews.com, 2026 X-Trail release),
moved with tools/parallax.py (depth-based 2.5D camera moves, CPU) and two
LTX-Video image-to-video clips (tools/genvideo.py). Titles/callouts: overlay.html
rendered with tools/video.mjs --alpha. Music: music.py (synthesised here, no licence needed).
Needs DEPTH_MODEL (Depth Anything V2 Small ONNX), a Python with onnxruntime +
opencv + numpy as PY, CHROMIUM_PATH in cloud sessions, ffmpeg.
"""
import json, os, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PROJ = HERE.parents[1]
PRESS = PROJ / 'assets/ref/press'
AI = PROJ / 'assets/out/ai'
WORK = Path(os.environ.get('WORK', HERE / '.work'))
OUT = PROJ / 'assets/out/xtrail-fakto-ad-30s-1920x1080.mp4'
PY = os.environ.get('PY', sys.executable)
FPS = 30
END = 30.0

# start time, source, how it moves, amount, transition INTO the next shot (type, seconds)
SHOTS = [
    (0.00, '44-taillight.jpg',       'push',  0.8, ('fade', 0.5)),
    (2.60, '28-sunset-front34.jpg',  'push',  1.0, ('fade', 0.4)),
    (5.60, '11-grille-dusk.jpg',     'right', 1.2, ('fadewhite', 0.15)),
    # 360: one tan car, walked around in jump cuts
    (7.60, '54-front-tan.jpg',       'push',  0.7, ('smoothleft', 0.15)),
    (8.50, '04-front34-tan-b.jpg',   'left',  1.4, ('smoothleft', 0.15)),
    (9.50, '03-side-tan.jpg',        'left',  1.4, ('smoothleft', 0.15)),
    (10.50, '35-rear34-tan.jpg',     'left',  1.4, ('smoothleft', 0.15)),
    (11.50, '47-rear-badge-tan.jpg', 'push',  0.8, ('smoothleft', 0.15)),
    (12.40, '23-front-close-tan.jpg', 'right', 1.2, ('fadewhite', 0.12)),
    # detail jumps
    (13.40, '13-grille-macro.jpg',   'right', 1.0, ('fadewhite', 0.12)),
    (14.40, '01-wheel-tan.jpg',      'push',  1.0, ('fadewhite', 0.12)),
    (15.40, '24-epower-badge.jpg',   'left',  1.0, ('fadewhite', 0.12)),
    (16.40, '08-screen-maps.jpg',    'push',  0.8, ('fadewhite', 0.12)),
    (17.40, '10-interior.jpg',       'push',  0.9, ('fade', 0.3)),
    # in motion
    (18.60, 'ai:shot5-forest-ltx.mp4', None, 0,   ('fade', 0.4)),
    (21.50, '19-aerial-blue.jpg',    'rise',  1.2, ('fade', 0.4)),
    (23.50, 'ai:shot5b-mountain-ltx.mp4', None, 0, ('fadeblack', 0.5)),
    (25.90, '30-lake-pair.jpg',      'pull',  0.8, None),
]


def run(cmd):
    subprocess.run([str(c) for c in cmd], check=True)


def clips():
    WORK.mkdir(parents=True, exist_ok=True)
    out = []
    for i, (start, src, move, amount, trans) in enumerate(SHOTS):
        nxt = SHOTS[i + 1][0] if i + 1 < len(SHOTS) else END
        length = nxt - start + (trans[1] if trans else 0)
        dst = WORK / f'{i:02d}.mp4'
        if src.startswith('ai:'):
            clip = AI / src[3:]
            dur = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                                                 '-of', 'csv=p=0', str(clip)]))
            slow = max(1.0, length / (dur - 0.05))
            run(['ffmpeg', '-y', '-loglevel', 'error', '-i', clip, '-vf',
                 f'setpts={slow:.4f}*PTS,minterpolate=fps={FPS}:mi_mode=blend,'
                 'scale=1920:1080:force_original_aspect_ratio=increase:flags=lanczos,crop=1920:1080,'
                 'unsharp=5:5:0.6', '-t', f'{length:.3f}', '-r', FPS, '-an', '-c:v', 'libx264', '-crf', '16',
                 '-pix_fmt', 'yuv420p', dst])
        else:
            run([PY, ROOT / 'tools/parallax.py', PRESS / src, dst, '--move', move, '--amount', amount,
                 '--seconds', f'{length:.3f}', '--fps', FPS])
        out.append((dst, length, trans))
        print(f'clip {i:02d} {src} {length:.2f}s', flush=True)
    return out


def edit(parts):
    inputs, chain = [], []
    for i, (p, _, _) in enumerate(parts):
        inputs += ['-i', p]
        chain.append(f'[{i}:v]settb=AVTB,fps={FPS},format=yuv420p[v{i}]')
    prev = 'v0'
    for i in range(1, len(parts)):
        ttype, tdur = parts[i - 1][2]
        offset = SHOTS[i][0]
        chain.append(f'[{prev}][v{i}]xfade=transition={ttype}:duration={tdur}:offset={offset:.3f}[x{i}]')
        prev = f'x{i}'
    # grade: slight teal/orange, contrast, vignette, fade in from black
    chain.append(f'[{prev}]eq=contrast=1.08:saturation=1.05:gamma=0.97,'
                 'colorbalance=rs=-0.03:bs=0.04:rh=0.04:bh=-0.03,vignette=PI/5,'
                 f'fade=t=in:st=0:d=0.8,trim=duration={END}[g]')
    base = WORK / 'base.mp4'
    run(['ffmpeg', '-y', '-loglevel', 'error', *inputs, '-filter_complex', ';'.join(chain), '-map', '[g]',
         '-c:v', 'libx264', '-crf', '15', '-preset', 'medium', '-pix_fmt', 'yuv420p', base])
    return base


def overlay():
    mov = WORK / 'overlay.mov'
    run(['node', ROOT / 'tools/video.mjs', HERE / 'overlay.html', '--size', '1920x1080', '--fps', FPS,
         '--duration', END, '--out', mov, '--alpha'])
    return mov


def music():
    wav = WORK / 'music.wav'
    run([PY, HERE / 'music.py', wav])
    return wav


def final(base, mov, wav):
    OUT.parent.mkdir(parents=True, exist_ok=True)
    run(['ffmpeg', '-y', '-loglevel', 'error', '-i', base, '-i', mov, '-i', wav, '-filter_complex',
         '[0:v][1:v]overlay=0:0:format=auto,noise=alls=5:allf=t,format=yuv420p[v]',
         '-map', '[v]', '-map', '2:a', '-c:v', 'libx264', '-crf', '17', '-preset', 'slow',
         '-c:a', 'aac', '-b:a', '256k', '-t', END, '-movflags', '+faststart', OUT])
    print(OUT)


if __name__ == '__main__':
    steps = sys.argv[1:] or ['all']
    parts = clips() if {'all', 'clips'} & set(steps) else [
        (WORK / f'{i:02d}.mp4', None, s[4]) for i, s in enumerate(SHOTS)]
    base = edit(parts) if {'all', 'edit'} & set(steps) else WORK / 'base.mp4'
    mov = overlay() if {'all', 'overlay'} & set(steps) else WORK / 'overlay.mov'
    wav = music() if {'all', 'music'} & set(steps) else WORK / 'music.wav'
    final(base, mov, wav)
