# Retrokauz Game Collector v1.0.0

Ein intuitiver Spiele-Verwalter für den **Commodore 64**, entwickelt in Commodore BASIC V2. Dieses Tool erlaubt es Sammlern, ihre Retro-Schätze direkt auf echter Hardware oder im Emulator zu katalogisieren.

## Features

- **Kapazität:** Verwaltung von bis zu 100 Einträgen
- **Detaillierte Erfassung:** Name, Studio, Jahr, System (18 Voreinstellungen), Medium und Rating
- **Sortierung:** Automatischer Bubble-Sort nach Alphabet beim Speichern
- **Suche & Filter:** Teilsuche in Titeln sowie Filterung nach System, Medium, Jahr oder Bewertung
- **Designs:** Drei wählbare Farbschemata (Classic, Hacker, Retro)
- **Datensicherheit:** Automatisches Backup-System (.bak) und Fehlerprüfung des Laufwerks

## Nutzung am C64 oder Emulator

Lade die fertige Datei `RETROKAUZ.d64` aus dem Repository herunter (Releases) und starte sie in deinem Emulator (z.B. VICE) oder übertrage sie auf eine echte Diskette.

```basic
LOAD "RETROKAUZ",8
RUN
```

---

## Für Entwickler (Build aus Quellcode)

Wenn du den Quellcode (`RETROKAUZ.bas`) verändern und selbst bauen möchtest, kannst du das beiliegende Build-Skript nutzen.

### Voraussetzungen

Du benötigst die **VICE Tools** (`petcat` und `c1541`).

- **macOS:** `brew install vice`
- **Linux (Debian/Ubuntu):** `sudo apt install vice`

### Build-Vorgang

```bash
git clone https://github.com/it-dennis/retrokauz-game-collector
cd retrokauz-game-collector
chmod +x build.sh
./build.sh
```

Das Skript konvertiert `RETROKAUZ.bas` in ein C64-kompatibles `RETROKAUZ.prg` und erstellt automatisch ein frisches `RETROKAUZ.d64` Disk-Image.

---

## Dateistruktur

| Datei | Beschreibung |
|---|---|
| `RETROKAUZ.bas` | Quellcode im ASCII-Textformat |
| `build.sh` | Build-Skript für macOS / Linux |
| `build_retrokauz.bat` | Build-Skript für Windows |
| `README.md` | Diese Dokumentation |
| `LICENSE` | GNU GPL v3.0 Lizenztext |

## Lizenz

Dieses Projekt ist unter der **GNU General Public License v3.0** lizenziert — siehe [LICENSE](LICENSE).

**(c) 2026 Dennis Rapp — [www.retrokauz.de](https://www.retrokauz.de)**
**Kontakt — [E-Mail](mailto:info@retrokauz.de)**
