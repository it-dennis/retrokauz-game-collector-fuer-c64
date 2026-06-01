@echo off
setlocal enabledelayedexpansion

rem === CONFIG ===
set "VICE=C:\Program Files\Vice"
set "SRC=%~dp0RETROKAUZ.BAS"
set "PRG=%~dp0RETROKAUZ.PRG"
set "D64=%~dp0RETROKAUZ.D64"
set "D64BAK=%~dp0RETROKAUZ.D64.bak"
set "DISKNAME=RETROKAUZ"
set "DISKID=RK"

if not exist "%VICE%\petcat.exe" (
  echo ERROR: petcat.exe not found in %VICE%
  pause & exit /b 1
)
if not exist "%VICE%\c1541.exe" (
  echo ERROR: c1541.exe not found in %VICE%
  pause & exit /b 1
)
if not exist "%SRC%" (
  echo ERROR: Source file not found: %SRC%
  pause & exit /b 1
)

rem Backup des alten D64 (enthaelt gespeicherte Spieldaten)
if exist "%D64%" (
  echo Erstelle Backup: %D64BAK%
  copy /y "%D64%" "%D64BAK%" >nul
)

if exist "%PRG%" del /f /q "%PRG%"
if exist "%D64%" del /f /q "%D64%"

echo Tokenizing BASIC source...
"%VICE%\petcat.exe" -w2 -o "%PRG%" -- "%SRC%"
if errorlevel 1 (echo ERROR: petcat failed. & pause & exit /b 1)
if not exist "%PRG%" (echo ERROR: PRG not created. & pause & exit /b 1)

echo Creating D64 image...
"%VICE%\c1541.exe" -format "%DISKNAME%,%DISKID%" d64 "%D64%"
if errorlevel 1 (echo ERROR: c1541 format failed. & pause & exit /b 1)

echo Writing PRG into D64...
"%VICE%\c1541.exe" -attach "%D64%" -write "%PRG%" "retrokauz,p"
if errorlevel 1 (echo ERROR: c1541 write failed. & pause & exit /b 1)

echo Verzeichnis:
"%VICE%\c1541.exe" -attach "%D64%" -list

rem rp9 mit aktuellem D64 aktualisieren (Python erforderlich)
where python >nul 2>&1
if not errorlevel 1 (
  echo Aktualisiere rp9...
  python -c "import zipfile,shutil; rp9=r'%~dp0retrokauz (-, -, C64).rp9'; tmp=r'%TEMP%\retrokauz_new.rp9'; m=zipfile.ZipFile(rp9).read('rp9-manifest.xml'); z=zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED); z.writestr('rp9-manifest.xml',m); z.write(r'%D64%','retrokauz.d64'); z.close(); shutil.move(tmp,rp9); print('rp9 aktualisiert.')"
)

echo.
echo Done. D64: %D64%
echo.
echo WICHTIG fuer Datenpersistenz:
echo   In C64 Forever direkt RETROKAUZ.D64 oeffnen,
echo   NICHT die .rp9 Datei!
pause
endlocal
