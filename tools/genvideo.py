#!/usr/bin/env python3
"""Photo-to-video with open-source models on free Hugging Face ZeroGPU Spaces.

    python tools/genvideo.py start.jpg "the SUV drives toward the camera, cinematic" \
        --seconds 4 --out projects/<slug>/assets/out/ai/shot5.mp4 [--model ltx|wan]

ltx (default): Lightricks LTX-Video distilled, 896x512. Works without a login.
wan: Wan 2.2 14B image-to-video. Refuses anonymous calls, so it needs HF_TOKEN.
Without HF_TOKEN the free GPU allowance is about 2 short clips, then it resets
later. A free Hugging Face account's read token in HF_TOKEN raises it.
Both models' licences allow commercial use of the output; re-check before publishing.
Setup: python3 -m venv .venv && .venv/bin/pip install gradio_client
"""
import argparse, os, shutil, sys

NEGATIVE = ('worst quality, inconsistent motion, blurry, jittery, distorted, '
            'morphing car, deformed wheels, changing logo or badge, text, subtitles')

def ltx(client, handle_file, a):
    return client.predict(a.prompt, NEGATIVE, handle_file(a.image), None, 512, 896,
                          'image-to-video', a.seconds, 9, a.seed or 0, a.seed is None, 1, True,
                          api_name='/image_to_video')

def wan(client, handle_file, a):
    return client.predict(handle_file(a.image), a.prompt, 6, NEGATIVE, a.seconds, 1, 1,
                          a.seed or 0, a.seed is None, api_name='/generate_video')

MODELS = {
    'ltx': ('Lightricks/ltx-video-distilled', ltx),
    'wan': ('zerogpu-aoti/wan2-2-fp8da-aoti-faster', wan),
}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('image')
    ap.add_argument('prompt')
    ap.add_argument('--model', choices=MODELS, default='ltx')
    ap.add_argument('--seconds', type=float, default=4)
    ap.add_argument('--seed', type=int, default=None, help='omit for a random seed')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    token = os.environ.get('HF_TOKEN')
    if a.model == 'wan' and not token:
        sys.exit('wan needs HF_TOKEN (a free Hugging Face read token); use --model ltx without one.')

    from gradio_client import Client, handle_file
    space, call = MODELS[a.model]
    client = Client(space, token=token, verbose=False) if token else Client(space, verbose=False)
    video, seed = call(client, handle_file, a)
    path = video['video'] if isinstance(video, dict) else video
    os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
    shutil.copy(path, a.out)
    print(f'{a.out}  seed={seed}')

if __name__ == '__main__':
    main()
