@echo off

echo [INFO] Starting setup for Windows...

cd /d "%~dp0"

echo %cd%

set START_DIR=%cd%

echo [INFO] Installing uv...
pip install uv

echo [INFO] Syncing dependencies...
uv sync

cd /d "%~dp0.."

echo %cd%

echo [SUCCESS] Setup complete

pause
