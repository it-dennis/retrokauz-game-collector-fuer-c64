# RETROKAUZ Game Collector — Benutzerhandbuch

**Version 1.0.0** · (c) 2026 Dennis Rapp · [www.retrokauz.de](https://www.retrokauz.de) · [info@retrokauz.de](mailto:info@retrokauz.de)

Dieses Handbuch beschreibt die Bedienung des RETROKAUZ Game Collector für den
Commodore 64. Es liegt dem Programm als PDF bei (`HANDBUCH.pdf`) und kann
ausgedruckt werden. Eine gekürzte Fassung ist außerdem direkt im Programm
unter Menüpunkt **[9] Hilfe** abrufbar.

---

## 1. Einleitung

RETROKAUZ Game Collector ist ein Verwaltungsprogramm für Retro-Sammler,
geschrieben in Commodore BASIC V2. Es läuft auf einem echten C64 oder in
einem Emulator (z.B. VICE) und erlaubt es, die eigene Spielesammlung direkt
auf Diskette zu katalogisieren — mit bis zu 100 Einträgen, Sortierung,
Such-/Filterfunktion und Statistik.

## 2. Systemvoraussetzungen

- Ein Commodore 64 (real oder emuliert, z.B. mit VICE/x64sc)
- Ein 1541-kompatibles Diskettenlaufwerk bzw. dessen Emulation (Device 8)
- Die Datei `RETROKAUZ.D64` (fertiges Disketten-Image)

## 3. Installation & erster Start

1. Lade `RETROKAUZ.D64` aus dem Release-Bereich des Projekts herunter.
2. Öffne die Datei in deinem Emulator (z.B. `x64sc RETROKAUZ.D64`) oder
   übertrage sie mit einem Tool wie `cbmtransfer` bzw. per SD2IEC auf eine
   echte Diskette.
3. Lade und starte das Programm:

   ```basic
   LOAD "RETROKAUZ",8,1
   RUN
   ```

4. Das Startbild erscheint kurz, danach öffnet sich das Hauptmenü.

## 4. Das Hauptmenü im Überblick

| Taste | Funktion |
|:-----:|----------|
| 1 | Neuer Eintrag |
| 2 | Spiele anzeigen |
| 3 | Spiele filtern |
| 4 | Eintrag löschen |
| 5 | Statistik |
| 6 | Farbschema wählen |
| 7 | Backup wiederherstellen |
| 8 | Programm beenden |
| 9 | Hilfe |

Die Anzahl der aktuell gespeicherten Einträge wird unten im Menü angezeigt.

## 5. Menüpunkte im Detail

### [1] Neuer Eintrag

Erfasst ein Spiel mit folgenden Angaben:

- **Name** und **Studio** (Freitext)
- **Jahr** (1950–2050)
- **System** — Auswahl aus 18 Voreinstellungen (NES, SNES, Game Boy,
  Famicom, Atari 4/8-Bit, Atari VCS, Atari ST, Genesis, Saturn, Xbox,
  PS1/PS2/PS3, PC-DOS, C64, C16, TI-99/4A, Amstrad)
- **Medium** — Diskette, Kassette, Modul, CD/DVD oder ISO-Datei
- **Rating** — Bewertung von 1 (sehr schlecht) bis 10 (sehr gut)

Nach Bestätigung wird die Liste automatisch alphabetisch sortiert und die
Daten werden gespeichert (inkl. Backup, siehe Abschnitt 7).

### [2] Spiele anzeigen

Zeigt die komplette Sammlung in Vierer-Blöcken an. Mit der **Leertaste**
blätterst du weiter, mit **Enter** kehrst du ins Hauptmenü zurück.

### [3] Spiele filtern

Durchsucht die Sammlung nach:

1. **System** (exakte Übereinstimmung)
2. **Name** (Teilsuche — z.B. findet "mario" alle Mario-Titel)
3. **Medium**
4. **Rating**
5. **Jahr**

Die Treffer werden untereinander mit Studio, Jahr und Rating aufgelistet.

### [4] Eintrag löschen

Zeigt die vorhandenen Einträge nummeriert an. Nach Eingabe der Nummer muss
das Löschen mit `j` bestätigt werden — `0` oder `n` bricht ab.

### [5] Statistik

Zeigt die Gesamtzahl der Spiele, die durchschnittliche Bewertung sowie die
Anzahl der Spiele pro System.

### [6] Farbschema wählen

Drei Farbschemata stehen zur Auswahl:

| Nr. | Schema | Beschreibung |
|:---:|--------|--------------|
| 1 | Classic | Hellblauer Text auf blauem Hintergrund |
| 2 | Hacker | Grüner Text auf schwarzem Hintergrund |
| 3 | Retro | Schwarzweiß |

### [7] Backup wiederherstellen

Beim Speichern legt das Programm automatisch eine Sicherungskopie
(`games.bak`) an. Über diesen Menüpunkt kann sie zurückgespielt werden,
falls die Hauptdatei beschädigt wurde oder eine Änderung rückgängig
gemacht werden soll. Vor dem Überschreiben wird eine Sicherheitsabfrage
angezeigt.

### [8] Programm beenden

Beendet RETROKAUZ nach einer Sicherheitsabfrage.

### [9] Hilfe

Zeigt eine kompakte, fünfseitige Kurzhilfe direkt auf dem Bildschirm — für
den schnellen Blick, ohne dieses Handbuch zur Hand nehmen zu müssen.

## 6. Bedientipps

- **Enter** bestätigt Eingaben und blättert aus Listen zurück ins Menü.
- **Leertaste** blättert innerhalb von Listen (Anzeigen, Hilfe) weiter.
- Bei Ja/Nein-Abfragen wird `j` bzw. `n` erwartet.
- Das Jahr muss zwischen 1950 und 2050 liegen, das Rating zwischen 1 und 10.

## 7. Datenspeicherung & Datensicherheit

Die Sammlung wird als sequentielle Datei `games` auf der Diskette
gespeichert. Vor jedem Speichervorgang wird automatisch ein Backup unter
`games.bak` angelegt. Tritt beim Laden oder Speichern ein Laufwerksfehler
auf, meldet das Programm die Fehlernummer und den Fehlertext des
Diskettenlaufwerks (Command-Channel, Kanal 15).

## 8. Fehlerbehebung (FAQ)

| Problem | Lösung |
|---------|--------|
| "Datei 'games' nicht gefunden!" beim Start | Normal beim allerersten Start — die Datei wird beim ersten Speichern angelegt. |
| Speichern schlägt mit Fehlercode fehl | Diskette bzw. Image auf Schreibschutz oder vollen Speicherplatz prüfen. |
| Daten wirken fehlerhaft/unvollständig | Über Menüpunkt **[7]** das letzte Backup wiederherstellen. |
| "Liste voll!" bei neuem Eintrag | Die maximale Kapazität von 100 Einträgen ist erreicht. |
| Bildschirmfarben wirken vertauscht | Über Menüpunkt **[6]** ein Farbschema neu auswählen. |

## 9. Für Entwickler

Der Quellcode (`RETROKAUZ.bas`) sowie die Build-Skripte für Windows
(`build_retrokauz.bat`) und macOS/Linux (`build.sh`) liegen dem Projekt
bei. Details zum Selbst-Bauen aus dem Quellcode stehen in der `README.md`
des Projekts.

## 10. Kontakt & Lizenz

RETROKAUZ Game Collector ist freie Software unter der **GNU General Public
License v3.0** (siehe `LICENSE`).

**(c) 2026 Dennis Rapp — [www.retrokauz.de](https://www.retrokauz.de)**
**Kontakt: [info@retrokauz.de](mailto:info@retrokauz.de)**
