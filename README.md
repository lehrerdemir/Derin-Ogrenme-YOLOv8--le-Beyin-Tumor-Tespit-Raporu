# YOLOv8 Brain Tumor Detection

Bu proje, Manyetik Rezonans (MR) görüntüleri üzerinden beyin tümörü varlığını otomatik olarak tespit etmek amacıyla YOLOv8 derin öğrenme mimarisi kullanılarak gerçekleştirilmiştir.

## Proje Yapısı
- `Beyin_Tumoru_Tespit_Raporu_final.pdf`: Proje sonuçlarını içeren detaylı rapor.
- `train_model.py`: Model eğitim betiği.
- `brain-tumor.yaml`: Veri seti yapılandırma dosyası.
- `results/`: Eğitim sürecinde elde edilen grafikler ve metrikler.
  - `results.png`: Kayıp ve metrik grafikleri.
  - `confusion_matrix.png`: Karışıklık matrisi.
  - `val_batch0_pred.jpg`: Doğrulama seti tahminleri.

## Kurulum ve Kullanım
1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install ultralytics
   ```
2. Modeli eğitmek için:
   ```bash
   python train_model.py
   ```

## Sonuçlar
Model 5 epoch sonunda mAP@0.5 skorunda **0.4905** ve duyarlılık (Recall) değerinde **0.7744** başarısına ulaşmıştır.
