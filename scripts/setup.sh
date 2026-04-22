set -e

echo "[INFO] Starting setup for Linux..."

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

cd "$ROOT_DIR"

echo "[INFO] Installing uv..."
python3 -m pip install uv

echo "[INFO] Syncing dependencies..."
python3 -m uv sync

cd "$ROOT_DIR"

echo "[SUCCESS] Setup complete"

read -p "Press Enter to continue . . . "
