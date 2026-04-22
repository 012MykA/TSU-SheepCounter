from ultralytics import YOLO
import cv2

class SheepDetector:
    SHEEP_CLASS_ID = 18

    def __init__(self, model_name: str = "models/yolov8m.pt", conf: float = 0.3):
        self.model = YOLO(model_name)
        self.conf = conf

    def process_frame(self, frame):
        """Processes a single frame and returns the annotated frame + sheep count."""
        results = self.model.predict(
            source=frame, 
            conf=self.conf, 
            verbose=False, 
            classes=[self.SHEEP_CLASS_ID]
        )
        
        sheep_count = 0
        annotated_frame = frame.copy()

        for result in results:
            if result.boxes is not None:
                sheep_count = len(result.boxes)
                # result.plot() draws boxes and labels automatically
                annotated_frame = result.plot()

        return annotated_frame, sheep_count
