from ultralytics import YOLO

model = None

def _load_model():
    global model
    if model is None:
        model = YOLO("yolov8n.pt")

def detect_objects(image_path: str):
    _load_model()
    
    results = model(image_path)

    names = results[0].names
    classes = results[0].boxes.cls.tolist()

    detected = [names[int(c)] for c in classes]

    return detected
