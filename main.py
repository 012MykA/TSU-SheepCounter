import os
from src.sheep_detector import SheepDetector
from src.video_stream import start_webcam
from src.notifier import ConsoleNotifier, TelegramNotifier

TG_TOKEN = ""
CHAT_ID = ""


def main():
    print("Starting Sheep Counting System...")

    detector = SheepDetector(model_name="models/yolov8m.pt", conf=0.25)

    if len(TG_TOKEN) != 0 or len(CHAT_ID) != 0:
        notifier = TelegramNotifier(TG_TOKEN, CHAT_ID)
    else:
        notifier = ConsoleNotifier()

    try:
        start_webcam(detector, notifier, interval=10)
    except KeyboardInterrupt:
        print("\nStopped by user.")


if __name__ == "__main__":
    main()
