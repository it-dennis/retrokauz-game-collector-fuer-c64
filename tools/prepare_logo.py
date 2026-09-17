# -*- coding: utf-8 -*-
"""Bereitet retrokauz_erstesLogo.png fuer das Handbuch-Titelblatt auf.

Das Original ist ein Schriftzug mit verrauschtem, mehrfarbigem Halbton-Rand
(Reste einer frueheren Freistellung). Dieses Skript vereinheitlicht die
Farben auf die C64-Palette des Handbuchs (weisser Schriftzug, hellgruener
Schein-Rand) und schneidet auf den sichtbaren Bereich zu.

Voraussetzung: pip install pillow numpy
Ausfuehren aus dem Projekt-Wurzelverzeichnis: python tools/prepare_logo.py
Ergebnis: tools/retrokauz_logo_c64.png (wird von generate_handbuch_pdf.py genutzt)
"""
from PIL import Image
import numpy as np

SRC = "retrokauz_erstesLogo.png"
DST = "tools/retrokauz_logo_c64.png"

WHITE = (255, 255, 255)
ACCENT = (0x94, 0xE0, 0x89)   # Hellgruen, wie im Handbuch-Layout
SOLID_THRESHOLD = 200          # ab hier gilt ein Pixel als "Kernstrich"
PADDING = 40                    # Pixel Rand um den sichtbaren Bereich

im = Image.open(SRC).convert("RGBA")
arr = np.array(im)
alpha = arr[:, :, 3]

solid = alpha >= SOLID_THRESHOLD
halo = (alpha > 0) & (alpha < SOLID_THRESHOLD)

arr[solid, 0:3] = WHITE
arr[solid, 3] = 255
arr[halo, 0:3] = ACCENT
# Die Halo-Alphawerte im Original sind sehr niedrig (~16%) und dadurch auf
# dunkelblauem Grund kaum als Farbe erkennbar - verstaerken, damit der
# hellgruene Rand sichtbar bleibt statt nur als dunklerer Schatten zu wirken.
arr[halo, 3] = np.clip(arr[halo, 3].astype(int) * 4, 0, 190).astype(np.uint8)

ys, xs = np.where(alpha > 0)
x0, x1 = max(xs.min() - PADDING, 0), min(xs.max() + PADDING, arr.shape[1])
y0, y1 = max(ys.min() - PADDING, 0), min(ys.max() + PADDING, arr.shape[0])
cropped = arr[y0:y1, x0:x1]

Image.fromarray(cropped, "RGBA").save(DST)
print(f"{DST} erzeugt ({cropped.shape[1]}x{cropped.shape[0]})")
