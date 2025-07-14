from ultralytics import YOLO
import os

DATA_YAML_PATH = r"D:\Poker\poker hand detector\data.yaml"

if not os.path.exists(DATA_YAML_PATH):
    raise FileNotFoundError(f"data.yaml not found at {DATA_YAML_PATH}")

model = YOLO("yolov8l.pt")

model.train(
    data=DATA_YAML_PATH,
    epochs=20,
    imgsz=640,
    batch=4,
    device="cpu",
    workers=1,
    verbose=True,
    name="Poker Hand Detector v1",
)                           