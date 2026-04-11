import sys
from src.sheep_detector import SheepDetector
from src.video_stream import start_webcam

def main():
    print("Starting Sheep Counting System...")
    
    detector = SheepDetector(model_name="models/yolov8n.pt", conf=0.25)
    
    try:
        start_webcam(detector)
    except KeyboardInterrupt:
        print("\nStopped by user.")
    finally:
        print("Application closed.")

if __name__ == "__main__":
    main()
