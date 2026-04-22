import cv2
import time

from src.notifier import BaseNotifier
from src.sheep_detector import SheepDetector


def start_webcam(detector: SheepDetector, notifier: BaseNotifier, interval=5):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Camera not found.")
        return

    last_count = -1
    last_notify_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            break

        processed_frame, count = detector.process_frame(frame)

        current_time = time.time()
        if count != last_count and (current_time - last_notify_time > interval):
            notifier.notify(count, processed_frame)
            last_count = count
            last_notify_time = current_time

        time.sleep(0.1)

    cap.release()
