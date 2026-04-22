# How to make autonomous on Linux

### Create service
```bash
sudo nano /etc/systemd/system/sheep.service
```

### Insert that in sheep.service
```ini
[Unit]
Description=Sheep Counter Service
After=network.target

[Service]
ExecStart=/home/orangepi/project_folder/.venv/bin/python /home/orangepi/project_folder/main.py
WorkingDirectory=/home/orangepi/project_folder
Restart=always
User=orangepi

[Install]
WantedBy=multi-user.target
```

### Activate
```bash
sudo systemctl enable sheep.service
sudo systemctl start sheep.service
```
