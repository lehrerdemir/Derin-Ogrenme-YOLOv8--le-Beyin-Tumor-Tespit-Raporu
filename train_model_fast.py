import torch
from ultralytics import YOLO
import os

def train():
    device = 0 if torch.cuda.is_available() else 'cpu'
    print(f"Eğitim cihazı: {device}")

    model = YOLO('yolov8n.pt')

    results = model.train(
        data='brain-tumor.yaml',
        epochs=10,  # 50 yerine 10 epoch
        imgsz=640,
        device=device,
        project='Brain_Tumor_Detection',
        name='yolov8_training',
        exist_ok=True
    )
    
    print("Eğitim tamamlandı.")

if __name__ == "__main__":
    train()
