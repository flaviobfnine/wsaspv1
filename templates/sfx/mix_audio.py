# -*- coding: utf-8 -*-
import os
import wave
import numpy as np
import subprocess

audio_voice_path = r"D:\BACKUP_ARQUIVOS\SITES\ASIMOV\SITES\SITE 2\templates\template_software_reels\assets\flavio_audio_1m21_2m11.mp3"
sfx_dir = r"D:\BACKUP_ARQUIVOS\SITES\ASIMOV\SITES\SITE 2\templates\sfx"

subprocess.run(f'ffmpeg -y -i "{audio_voice_path}" -ar 44100 -ac 1 "{os.path.join(sfx_dir, "temp_voice.wav")}"', shell=True, check=True)

with wave.open(os.path.join(sfx_dir, "temp_voice.wav"), "r") as wf:
    sr = wf.getframerate()
    n_frames = wf.getnframes()
    raw = wf.readframes(n_frames)
    voice_sig = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32767.0

try:
    os.remove(os.path.join(sfx_dir, "temp_voice.wav"))
except:
    pass

total_len = len(voice_sig)
mixed = voice_sig.copy()

def read_sfx(filename):
    p = os.path.join(sfx_dir, filename)
    with wave.open(p, "r") as wf:
        n = wf.getnframes()
        r = wf.readframes(n)
        return np.frombuffer(r, dtype=np.int16).astype(np.float32) / 32767.0

whoosh = read_sfx("whoosh.wav") * 0.40
pop = read_sfx("pop.wav") * 0.35
impact = read_sfx("impact.wav") * 0.45

cues = [
    (1.1, whoosh),
    (1.5, pop),
    (11.4, impact),
    (12.5, pop),
    (16.8, pop),
    (26.3, impact),
    (28.4, pop),
    (37.2, whoosh),
    (37.4, impact),
    (42.5, whoosh)
]

for t_sec, sfx in cues:
    idx = int(t_sec * sr)
    l = min(len(sfx), total_len - idx)
    if l > 0:
        mixed[idx:idx+l] += sfx[:l]

mixed = np.clip(mixed, -0.98, 0.98)
out_sig = np.int16(mixed * 32767.0)

wav_out = os.path.join(sfx_dir, "mixed_audio_with_sfx.wav")
with wave.open(wav_out, "w") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(sr)
    wf.writeframes(out_sig.tobytes())

mp3_out = os.path.join(sfx_dir, "audio_master_reels_sfx.mp3")
subprocess.run(f'ffmpeg -y -i "{wav_out}" -b:a 192k "{mp3_out}"', shell=True, check=True)
print("AUDIO COM SFX FINALIZADO:", mp3_out)
