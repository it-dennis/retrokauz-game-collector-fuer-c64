# -*- coding: utf-8 -*-
"""Erzeugt HANDBUCH.pdf im C64-Retro-Look für RETROKAUZ Game Collector.

Voraussetzung: pip install fpdf2
Ausführen aus dem Projekt-Wurzelverzeichnis:  python tools/generate_handbuch_pdf.py
Inhaltliche Quelle/Referenz: HANDBUCH.md
"""
from fpdf import FPDF
from fpdf.enums import XPos, YPos

PAGE_W, PAGE_H = 210, 297

# Pepto C64-Palette (angelehnt an die Ingame-Farbschemata)
BG = (0x40, 0x31, 0x8D)        # C64 Blau (Hintergrund, Farbe 6)
FRAME = (0x78, 0x69, 0xC4)     # Hellblau (Rahmen, Farbe 14)
TEXT = (0xC9, 0xC4, 0xFF)      # Aufgehelltes Hellblau (Fliesstext, druckfreundlich)
HEAD = (0xFF, 0xFF, 0xFF)      # Weiß (Überschriften)
ACCENT = (0x94, 0xE0, 0x89)    # Hellgrün (Farbe 13, Akzent/Zahlen)
DIM = (0xA3, 0x9A, 0xE0)       # gedämpftes Lila (Fusszeile)

LOGO_PATH = "tools/retrokauz_logo_c64.png"

MARGIN_OUTER = 8
MARGIN_INNER = 16
NEXT = dict(new_x=XPos.LMARGIN, new_y=YPos.NEXT)
STAY = dict(new_x=XPos.RIGHT, new_y=YPos.TOP)


class Handbuch(FPDF):
    def header(self):
        pass

    def footer(self):
        self.set_y(-14)
        self.set_font("Courier", "", 8)
        self.set_text_color(*DIM)
        self.cell(0, 6, f"RETROKAUZ GAME COLLECTOR - HANDBUCH v1.1        Seite {self.page_no()}/{{nb}}",
                  align="C", **NEXT)

    def page_frame(self):
        self.set_fill_color(*BG)
        self.rect(0, 0, PAGE_W, PAGE_H, "F")
        self.set_draw_color(*FRAME)
        self.set_line_width(1.0)
        self.rect(MARGIN_OUTER, MARGIN_OUTER, PAGE_W - 2 * MARGIN_OUTER, PAGE_H - 2 * MARGIN_OUTER)
        self.set_line_width(0.3)
        self.rect(MARGIN_OUTER + 2, MARGIN_OUTER + 2, PAGE_W - 2 * (MARGIN_OUTER + 2), PAGE_H - 2 * (MARGIN_OUTER + 2))

    def add_page(self, *args, **kwargs):
        super().add_page(*args, **kwargs)
        self.page_frame()
        self.set_left_margin(MARGIN_INNER)
        self.set_right_margin(MARGIN_INNER)
        self.set_top_margin(MARGIN_INNER)
        self.set_xy(MARGIN_INNER, MARGIN_INNER)

    def rule(self, w=None, color=FRAME):
        if w is None:
            w = PAGE_W - 2 * MARGIN_INNER
        self.set_draw_color(*color)
        self.set_line_width(0.6)
        x, y = self.get_x(), self.get_y()
        self.line(x, y, x + w, y)
        self.ln(3)

    def h1(self, txt):
        self.set_font("Courier", "B", 20)
        self.set_text_color(*HEAD)
        self.cell(0, 10, txt, **NEXT)
        self.rule()

    def h2(self, num, txt):
        self.ln(2)
        self.set_font("Courier", "B", 13)
        self.set_text_color(*ACCENT)
        self.cell(10, 8, f"{num}", **STAY)
        self.set_text_color(*HEAD)
        self.cell(0, 8, txt, **NEXT)

    def h3(self, txt):
        self.ln(1)
        self.set_font("Courier", "B", 11)
        self.set_text_color(*ACCENT)
        self.cell(0, 6.5, txt, **NEXT)

    def body(self, txt, size=10.5, leading=5.2):
        self.set_font("Courier", "", size)
        self.set_text_color(*TEXT)
        self.multi_cell(0, leading, txt, **NEXT)

    def bullet(self, txt, size=10.5, leading=5.2):
        self.set_font("Courier", "", size)
        self.set_text_color(*TEXT)
        self.cell(6, leading, "-", **STAY)
        self.multi_cell(0, leading, txt, **NEXT)

    def spacer(self, h=3):
        self.ln(h)


pdf = Handbuch(format="A4", unit="mm")
pdf.set_auto_page_break(auto=True, margin=MARGIN_INNER + 6)
pdf.alias_nb_pages()

# ---------------------------------------------------------------- Seite 1 --
pdf.add_page()
pdf.set_y(40)
pdf.set_font("Courier", "B", 15)
pdf.set_text_color(*ACCENT)
pdf.cell(0, 8, "========================================", align="C", **NEXT)
pdf.ln(3)
logo_w = 120
pdf.image(LOGO_PATH, x=(PAGE_W - logo_w) / 2, w=logo_w)
pdf.ln(3)
pdf.set_font("Courier", "B", 16)
pdf.set_text_color(*HEAD)
pdf.cell(0, 10, "GAME COLLECTOR", align="C", **NEXT)
pdf.set_font("Courier", "B", 15)
pdf.set_text_color(*ACCENT)
pdf.cell(0, 8, "========================================", align="C", **NEXT)
pdf.ln(6)
pdf.set_font("Courier", "", 13)
pdf.set_text_color(*TEXT)
pdf.cell(0, 8, "B E N U T Z E R H A N D B U C H", align="C", **NEXT)
pdf.set_font("Courier", "", 11)
pdf.cell(0, 8, "Version 1.1", align="C", **NEXT)
pdf.ln(14)
pdf.set_font("Courier", "", 10.5)
pdf.set_text_color(*TEXT)
pdf.set_x(MARGIN_INNER + 15)
pdf.multi_cell(PAGE_W - 2 * (MARGIN_INNER + 15), 5.5,
    "Ein intuitiver Spiele-Verwalter für den Commodore 64,\n"
    "geschrieben in Commodore BASIC V2 - für echte Hardware\n"
    "und Emulatoren gleichermaßen.", align="C")
pdf.set_y(-40)
pdf.set_font("Courier", "", 9.5)
pdf.set_text_color(*DIM)
pdf.cell(0, 6, "(c) 2026 Dennis Rapp  -  www.retrokauz.de", align="C", **NEXT)
pdf.cell(0, 6, "info@retrokauz.de  -  Lizenz: GNU GPL v3.0", align="C", **NEXT)

# ---------------------------------------------------------------- Seite 2 --
pdf.add_page()
pdf.h1("1. Einleitung & Erste Schritte")

pdf.h3("Was ist RETROKAUZ?")
pdf.body(
    "RETROKAUZ Game Collector ist ein Verwaltungsprogramm für Retro-\n"
    "Sammler. Es läuft auf einem echten C64 oder in einem Emulator\n"
    "(z.B. VICE) und katalogisiert die eigene Spielesammlung direkt auf\n"
    "Diskette - mit bis zu 100 Einträgen, automatischer Sortierung,\n"
    "Such-/Filterfunktion und Statistik."
)
pdf.spacer(2)

pdf.h3("Systemvoraussetzungen")
pdf.bullet("Ein Commodore 64 (real oder emuliert, z.B. mit VICE/x64sc)")
pdf.bullet("Ein 1541-kompatibles Diskettenlaufwerk bzw. dessen Emulation (Device 8)")
pdf.bullet("Die Datei RETROKAUZ.D64 (fertiges Disketten-Image)")
pdf.spacer(2)

pdf.h3("Installation & Start")
pdf.body(
    "1. RETROKAUZ.D64 aus dem Release-Bereich des Projekts laden.\n"
    "2. Datei im Emulator öffnen (z.B. x64sc RETROKAUZ.D64) oder per\n"
    "   SD2IEC / Transfer-Kabel auf eine echte Diskette übertragen.\n"
    "3. Programm laden und starten:"
)
pdf.ln(1)
pdf.set_font("Courier", "B", 11)
pdf.set_text_color(*ACCENT)
pdf.set_x(MARGIN_INNER + 6)
pdf.cell(0, 6, 'LOAD "RETROKAUZ",8,1', **NEXT)
pdf.set_x(MARGIN_INNER + 6)
pdf.cell(0, 6, "RUN", **NEXT)
pdf.spacer(1)
pdf.body("4. Nach dem Startbild öffnet sich automatisch das Hauptmenü.")

pdf.spacer(4)
pdf.h1("2. Das Hauptmenü im Überblick")
rows = [
    ("1", "Neuer Eintrag"),
    ("2", "Spiele anzeigen"),
    ("3", "Spiele filtern"),
    ("4", "Eintrag löschen"),
    ("5", "Statistik"),
    ("6", "Farbschema wählen"),
    ("7", "Backup wiederherstellen"),
    ("8", "Programm beenden"),
    ("9", "Hilfe"),
]
for num, label in rows:
    pdf.set_font("Courier", "B", 11)
    pdf.set_text_color(*ACCENT)
    pdf.cell(14, 6.5, f"[{num}]", **STAY)
    pdf.set_font("Courier", "", 11)
    pdf.set_text_color(*TEXT)
    pdf.cell(0, 6.5, label, **NEXT)

# ---------------------------------------------------------------- Seite 3 --
pdf.add_page()
pdf.h1("3. Menüpunkte im Detail")

pdf.h2("[1]", "Neuer Eintrag")
pdf.body("Erfasst Name, Studio, Jahr (1950-2050), System (18 Vorein-\n"
         "stellungen von NES bis Amstrad), Medium (Diskette, Kassette,\n"
         "Modul, CD/DVD, ISO) und Rating (1-10). Die Liste wird danach\n"
         "automatisch alphabetisch sortiert und gespeichert.")

pdf.h2("[2]", "Spiele anzeigen")
pdf.body("Zeigt die Sammlung in Vierer-Blöcken. Leertaste = weiter,\n"
         "Enter = zurück ins Hauptmenü.")

pdf.h2("[3]", "Spiele filtern")
pdf.body('Suche nach System, Name (Teilsuche, z.B. "mario"), Medium,\n'
         "Rating oder Jahr. Treffer werden mit Studio, Jahr und Rating\n"
         "aufgelistet.")

pdf.h2("[4]", "Eintrag löschen")
pdf.body('Nummer aus der Liste wählen, Löschen mit "j" bestätigen -\n'
         '"0" oder "n" bricht ab.')

pdf.h2("[5]", "Statistik")
pdf.body("Gesamtzahl der Spiele, Durchschnittsbewertung sowie Anzahl\n"
         "der Spiele pro System.")

pdf.h2("[6]", "Farbschema wählen")
pdf.bullet("1 Classic - hellblauer Text auf blauem Hintergrund")
pdf.bullet("2 Hacker  - grüner Text auf schwarzem Hintergrund")
pdf.bullet("3 Retro   - schwarzweiß")

pdf.h2("[7]", "Backup wiederherstellen")
pdf.body("Beim Speichern legt RETROKAUZ automatisch eine Sicherung\n"
         "(games.bak) an. Dieser Punkt spielt sie nach Sicherheits-\n"
         "abfrage zurück, falls die Hauptdatei beschädigt wurde.")

pdf.h2("[8]", "Programm beenden")
pdf.body("Beendet RETROKAUZ nach einer Sicherheitsabfrage.")

pdf.h2("[9]", "Hilfe")
pdf.body("Kompakte Kurzhilfe direkt auf dem Bildschirm - für den\n"
         "schnellen Blick ohne dieses Handbuch.")

# ---------------------------------------------------------------- Seite 4 --
pdf.add_page()
pdf.h1("4. Bedientipps & Datensicherheit")

pdf.h3("Bedientipps")
pdf.bullet("Enter bestätigt Eingaben und blättert aus Listen zurück ins Menü")
pdf.bullet("Leertaste blättert innerhalb von Listen (Anzeigen, Hilfe) weiter")
pdf.bullet('Bei Ja/Nein-Abfragen wird "j" bzw. "n" erwartet')
pdf.bullet("Jahr: 1950-2050, Rating: 1-10")
pdf.spacer(2)

pdf.h3("Datenspeicherung")
pdf.body(
    'Die Sammlung wird als sequentielle Datei "games" auf der Diskette\n'
    "gespeichert. Vor jedem Speichervorgang legt RETROKAUZ automatisch\n"
    'ein Backup unter "games.bak" an. Bei Laufwerksfehlern meldet das\n'
    "Programm Fehlernummer und Fehlertext des Diskettenlaufwerks."
)

pdf.spacer(3)
pdf.h1("5. Fehlerbehebung (FAQ)")
faq = [
    ("Datei 'games' nicht gefunden", "Normal beim allerersten Start - wird beim\nersten Speichern automatisch angelegt."),
    ("Speichern schlägt fehl", "Diskette/Image auf Schreibschutz oder\nvollen Speicherplatz prüfen."),
    ("Daten wirken fehlerhaft", "Über [7] das letzte Backup wiederher-\nstellen."),
    ('"Liste voll!"', "Maximale Kapazität von 100 Einträgen\nerreicht."),
    ("Farben wirken vertauscht", "Über [6] ein Farbschema neu wählen."),
]
for problem, solution in faq:
    pdf.set_font("Courier", "B", 10.5)
    pdf.set_text_color(*ACCENT)
    pdf.multi_cell(0, 5.5, f"? {problem}", **NEXT)
    pdf.set_font("Courier", "", 10.5)
    pdf.set_text_color(*TEXT)
    pdf.set_x(MARGIN_INNER + 6)
    pdf.multi_cell(PAGE_W - 2 * MARGIN_INNER - 6, 5.5, solution, **NEXT)
    pdf.ln(1)

pdf.spacer(3)
pdf.h1("6. Kontakt & Lizenz")
pdf.body(
    "RETROKAUZ Game Collector ist freie Software unter der GNU General\n"
    "Public License v3.0 (siehe LICENSE im Projekt).\n"
)
pdf.set_font("Courier", "B", 11)
pdf.set_text_color(*HEAD)
pdf.cell(0, 7, "(c) 2026 Dennis Rapp - www.retrokauz.de", **NEXT)
pdf.set_font("Courier", "", 10.5)
pdf.set_text_color(*TEXT)
pdf.cell(0, 6, "Kontakt: info@retrokauz.de", **NEXT)

pdf.output("HANDBUCH.pdf")
print("HANDBUCH.pdf erzeugt.")
