#!/usr/bin/env python3
"""Synthesised cinematic score for the 30 s X-Trail ad. Our own sound, no licence needed.

    python music.py out.wav

Cue points follow build.py: pulse from 2.6 s, hit + riser into the 360 at 7.6 s,
whooshes on the jump cuts, a gap and boom at 18.6 s (in motion), final boom at 25.9 s.
"""
import sys, wave
import numpy as np

SR = 48000
DUR = 30.0
BPM = 96
BEAT = 60 / BPM
CUTS = [8.5, 9.5, 10.5, 11.5, 12.4, 13.4, 14.4, 15.4, 16.4, 17.4]
rng = np.random.default_rng(7)
t = np.arange(int(SR * DUR)) / SR


def env(a, d, length):
    n = int(length * SR)
    x = np.arange(n) / SR
    return np.minimum(1, x / max(a, 1e-4)) * np.exp(-np.maximum(0, x - a) / d)


def place(buf, sig, at, gain=1.0):
    i = int(at * SR)
    j = min(len(buf), i + len(sig))
    if i < len(buf):
        buf[i:j] += gain * sig[:j - i]


def smooth(x, n):
    return np.convolve(x, np.ones(n) / n, mode='same')


def kick(length=0.5, f0=110, f1=42, decay=0.22):
    x = np.arange(int(length * SR)) / SR
    f = f1 + (f0 - f1) * np.exp(-x / 0.04)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x / decay)


def boom(length=3.5):
    x = np.arange(int(length * SR)) / SR
    f = 30 + 70 * np.exp(-x / 0.08)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x / 1.1)
    air = smooth(rng.standard_normal(len(x)), 40) * np.exp(-x / 0.5) * 0.6
    return body + air


def tick():
    n = rng.standard_normal(int(0.05 * SR))
    return (n - smooth(n, 6)) * env(0.001, 0.012, 0.05)


def whoosh(length=0.35):
    n = smooth(rng.standard_normal(int(length * SR)), 12)
    x = np.linspace(0, 1, len(n))
    return n * np.sin(np.pi * x) ** 2


def riser(length):
    x = np.arange(int(length * SR)) / SR
    p = x / length
    sweep = np.sin(2 * np.pi * np.cumsum(180 + 1600 * p ** 2) / SR) * 0.25
    noise = rng.standard_normal(len(x))
    noise = noise - smooth(noise, int(60 - 50 * 0.5))
    return (sweep + noise * 0.5) * p ** 2.2


def tone(freqs, harmonics=6):
    out = np.zeros_like(t)
    for f in freqs:
        for h in range(1, harmonics + 1):
            out += np.sin(2 * np.pi * f * h * t + rng.uniform(0, 6.28)) / h ** 1.6
    return out / len(freqs)


def reverb(x, secs=1.8, mix=0.25):
    ir = rng.standard_normal(int(secs * SR)) * np.exp(-np.arange(int(secs * SR)) / SR / (secs / 5))
    ir = smooth(ir, 8)
    n = len(x) + len(ir)
    wet = np.fft.irfft(np.fft.rfft(x, n) * np.fft.rfft(ir, n), n)[:len(x)]
    wet *= np.abs(x).max() / (np.abs(wet).max() + 1e-9)
    return x * (1 - mix) + wet * mix


def build():
    mix = np.zeros_like(t)
    # bed: low A drone + A-minor pad, swelling in, ducking at the gap, out at the end
    drone = tone([55, 55.25], 8) * 0.5
    pad = tone([110, 164.81, 261.63, 329.63], 4) * (0.8 + 0.2 * np.sin(2 * np.pi * 0.25 * t))
    bed_env = np.clip(t / 2.5, 0, 1) * (0.55 + 0.45 * np.clip((t - 7.6) / 1, 0, 1))
    gap = ~((t > 18.25) & (t < 18.6))
    bed_env *= gap * np.clip((30 - t) / 1.5, 0, 1) ** 0.5
    mix += (drone * 0.6 + pad * 0.35) * bed_env

    # heartbeat pulse 2.6–7.6, driving 8ths 7.6–18.2, full groove 18.6–25.9
    b = 2.6
    while b < 7.6:
        place(mix, kick(), b, 0.7)
        b += BEAT
    b = 7.6
    while b < 18.2:
        place(mix, kick(), b, 0.85)
        place(mix, tick(), b + BEAT / 2, 0.25)
        b += BEAT / 2 if b > 13.4 else BEAT
    b = 18.6
    while b < 25.6:
        place(mix, kick(decay=0.28), b, 1.0)
        place(mix, tick(), b + BEAT / 2, 0.35)
        place(mix, whoosh(0.18), b + BEAT * 0.75, 0.15)
        b += BEAT

    for at, length in [(6.0, 1.6), (16.8, 1.45), (24.4, 1.5)]:
        place(mix, riser(length), at, 0.5)
    for c in CUTS:
        place(mix, whoosh(), c - 0.17, 0.35)
    place(mix, kick(0.8, 160, 50, 0.4), 5.6, 0.8)        # light hit on the grille
    place(mix, boom(), 7.6, 0.9)                          # into the 360
    place(mix, boom(), 18.6, 1.1)                         # in motion
    place(mix, boom(4.0), 25.9, 1.2)                      # end card

    mix = reverb(mix)
    mix = np.tanh(mix / (np.abs(mix).max() + 1e-9) * 1.6)
    mix *= 10 ** (-1 / 20) / np.abs(mix).max()
    fade = np.clip((DUR - t) / 0.6, 0, 1)
    left = mix * fade
    right = np.roll(mix, int(0.011 * SR)) * fade           # a touch of width
    return np.stack([left, right], 1)


if __name__ == '__main__':
    audio = (build() * 32767).astype(np.int16)
    with wave.open(sys.argv[1], 'wb') as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(audio.tobytes())
    print(sys.argv[1])
