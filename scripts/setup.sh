set -e

echo "[INFO] Starting setup for Linux..."

cd "$(dirname "$0")/.."

echo "[INFO] Installing uv..."
python3 -m pip install uv

echo "[INFO] Syncing dependencies..."
python3 -m uv sync

echo "[SUCCESS] Setup complete"

read -p "Press Enter to continue . . . "
