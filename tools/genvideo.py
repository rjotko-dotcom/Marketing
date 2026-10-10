#!/usr/bin/env python3
"""Image-to-video with open-source Wan 2.2 on a free Hugging Face ZeroGPU Space.

    python tools/genvideo.py start.jpg "the SUV drives toward the camera, cinematic" \
        --seconds 5 --seed 42 --out projects/<slug>/assets/out/shot5.mp4

Needs HF_TOKEN (a free Hugging Face account's read token) in the environment;
anonymous calls are refused. Free accounts get a small daily GPU quota, so
expect a few clips per day. Wan 2.2 is Apache-2.0, so the output may be used
commercially. Setup: python3 -m venv .venv && .venv/bin/pip install gradio_client
"""
import argparse, os, shutil, sys

SPACE = 'zerogpu-aoti/wan2-2-fp8da-aoti-faster'
NEGATIVE = ('morphing car, deformed wheels, changing logo or badge, extra doors, '
            'text, subtitles, blurry, low quality, static frame, jittery')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('image')
    ap.add_argument('prompt')
    ap.add_argument('--seconds', type=float, default=5)
    ap.add_argument('--steps', type=int, default=6)
    ap.add_argument('--seed', type=int, default=None, help='omit for a random seed')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    token = os.environ.get('HF_TOKEN')
    if not token:
        sys.exit('HF_TOKEN is not set; add a Hugging Face read token to the environment.')

    from gradio_client import Client, handle_file
    client = Client(SPACE, hf_token=token, verbose=False)
    video, seed = client.predict(
        handle_file(a.image), a.prompt, a.steps, NEGATIVE, a.seconds, 1, 1,
        a.seed or 0, a.seed is None, api_name='/generate_video')
    path = video['video'] if isinstance(video, dict) else video
    os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
    shutil.copy(path, a.out)
    print(f'{a.out}  seed={seed}')

if __name__ == '__main__':
    main()
