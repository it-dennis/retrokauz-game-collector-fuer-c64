#!/bin/bash

# Konfiguration
INPUT="RETROKAUZ.bas"
OUTPUT="RETROKAUZ.prg"
DISK="RETROKAUZ.d64"

echo "--- Retrokauz Game Collector Build Tool ---"

# 1. Prüfen ob VICE Tools installiert sind
if ! command -v petcat &> /dev/null
then
    echo "Fehler: 'petcat' wurde nicht gefunden. Bitte installiere VICE (brew install vice)."
    exit
fi

# 2. .bas zu .prg konvertieren
echo "Konvertiere $INPUT zu $OUTPUT..."
petcat -w2 -o "$OUTPUT" -- "$INPUT"

# 3. Optional: D64 Image erstellen, falls c1541 vorhanden ist
if command -v c1541 &> /dev/null
then
    echo "Erstelle Disk-Image $DISK..."
    rm -f "$DISK"
    c1541 -format "retrokauz,rk" d64 "$DISK"
    c1541 -attach "$DISK" -write "$OUTPUT" "retrokauz"
    echo "Fertig: $DISK wurde erstellt."
else
    echo "Hinweis: 'c1541' nicht gefunden. Nur $OUTPUT wurde erstellt."
fi

echo "Build erfolgreich abgeschlossen."
