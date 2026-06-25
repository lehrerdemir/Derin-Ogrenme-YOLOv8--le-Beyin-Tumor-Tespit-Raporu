import pandas as pd
import os

# Sonuçları oku
results_path = '/home/ubuntu/runs/detect/Brain_Tumor_Detection/yolov8_training/results.csv'
df = pd.read_csv(results_path)
df.columns = df.columns.str.strip()

# En iyi epoch'u bul (mAP50 baz alınarak)
best_epoch = df.loc[df['metrics/mAP50(B)'].idxmax()]

summary = f"""
### Beyin Tümörü Tespiti Model Eğitim Özeti (YOLOv8n)

| Metrik | Değer |
|--------|-------|
| Toplam Epoch | {len(df)} |
| En İyi mAP@0.5 | {best_epoch['metrics/mAP50(B)']:.4f} |
| En İyi mAP@0.5:0.95 | {best_epoch['metrics/mAP50-95(B)']:.4f} |
| Kesinlik (Precision) | {best_epoch['metrics/precision(B)']:.4f} |
| Duyarlılık (Recall) | {best_epoch['metrics/recall(B)']:.4f} |
| Eğitim Süresi (Saniye) | {df['time'].sum():.2f} |

"""

with open('/home/ubuntu/training_summary.md', 'w') as f:
    f.write(summary)

print("Özet oluşturuldu: /home/ubuntu/training_summary.md")
