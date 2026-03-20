from ultralytics import YOLO

SHEEP_CLASS_ID = 18

def count_sheep(
    image_paths: list[str], model_name: str = "models/yolov8m.pt", conf: float = 0.1
) -> int:
    model = YOLO(model_name)

    total_sheep = 0

    for path in image_paths:
        path = str(path)
        results = model.predict(source=path, conf=conf, verbose=False)

        for result in results:
            if result.boxes is None:
                continue

            classes = result.boxes.cls.tolist()
            sheep_count = sum(1 for cls_id in classes if int(cls_id) == SHEEP_CLASS_ID)
            total_sheep += sheep_count
            print(f"  {path}: sheep found — {sheep_count}")

    return total_sheep
