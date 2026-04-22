@echo off

echo [INFO] Starting setup for Windows...

cd /d "%~dp0"

echo [INFO] Installing uv...
pip install uv

echo [INFO] Syncing dependencies...
uv sync

echo [SUCCESS] Setup complete

pause
