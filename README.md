# TSU-sheep-counter
A script that counts sheep in photos using AI model YOLOv8

## Getting Started

### Clone the repository
```bash
git clone https://github.com/012MykA/TSU-SheepCounter.git
cd TSU-SheepCounter
```

### Setup
You can set up the environment automatically using the provided scripts or follow the manual installation steps.


### Automatic Setup (Recommended)
Choose the script corresponding to your operating system:

* **Windows:**
```bash
./scripts/setup.bat
```

* **Linux:**
    
```bash
chmod +x scripts/setup.sh
./scripts/setup.sh
```

---

### Manual Setup
If you prefer to configure everything manually, follow these steps:

1. **Install uv**
The project uses `uv` for dependency management.
```bash
pip install uv
```

2. **Install dependencies**
This command will create a virtual environment and install all required packages (including YOLOv8).
```bash
uv sync
```
