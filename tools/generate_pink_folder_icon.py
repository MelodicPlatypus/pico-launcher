#!/usr/bin/env python3
"""
Generate a 64x64 4-bpp tiled texture (2048 bytes) and a 16-color BGR555 palette (32 bytes)
for a demo 'pink' folder icon. Output:
  _pico/themes/demo/folder_icons/pink.bin
  _pico/themes/demo/folder_icons/pinkPltt.bin
"""
import os, struct
ROOT = os.path.dirname(os.path.dirname(__file__))
OUT_DIR = os.path.join(ROOT, "_pico", "themes", "demo", "folder_icons")
os.makedirs(OUT_DIR, exist_ok=True)

def bgr555(r,g,b):
    # DS BGR555 (bits: 0-4 B, 5-9 G, 10-14 R)
    return struct.pack("<H", ((b & 0xF8) >> 3) | (((g & 0xF8) >> 3) << 5) | (((r & 0xF8) >> 3) << 10))

with open(os.path.join(OUT_DIR, "pink.bin"), "wb") as f:
    f.write(bytes([0x11]) * 2048)  # index 1 everywhere (0x11 pairs)

pal = bytearray(32)                 # 16 * 2 bytes
pal[0:2] = bgr555(0,0,0)            # index 0
pal[2:4] = bgr555(236,72,153)       # index 1 -> pink (#EC4899)
with open(os.path.join(OUT_DIR, "pinkPltt.bin"), "wb") as f:
    f.write(pal)

print("Generated:", os.path.join(OUT_DIR, "pink.bin"), os.path.join(OUT_DIR, "pinkPltt.bin"))
