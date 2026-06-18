# Beyin Tümörü Tespiti Proje Raporu

## 1. Giriş
Bu proje, Manyetik Rezonans (MR) görüntüleri üzerinden beyin tümörü varlığını otomatik olarak tespit etmek amacıyla YOLOv8 derin öğrenme mimarisi kullanılarak gerçekleştirilmiştir. MR görüntüleri tıp dünyasında kritik öneme sahip olup, tümörlerin erken teşhisi hayati önem taşımaktadır.

## 2. Veri Seti
Kullanılan veri seti Ultralytics tarafından sağlanan 'Brain Tumor Detection' veri setidir.
- **Eğitim Seti:** 893 görüntü
- **Doğrulama Seti:** 223 görüntü
- **Sınıflar:** 0 (Negatif), 1 (Pozitif)

## 3. Yöntem
Projede YOLOv8n (nano) modeli kullanılmıştır. Bu model, hem hız hem de doğruluk açısından optimize edilmiş bir nesne tespiti modelidir. Eğitim parametreleri:
- **Model:** YOLOv8n
- **Görüntü Boyutu:** 640x640 (Eğitimde stabilite için 320x320 kullanılmıştır)
- **Epoch Sayısı:** 5 (Ortam stabilitesi ve zaman kısıtı nedeniyle optimize edilmiştir)
- **Cihaz:** CPU

## 4. Bulgular ve Analiz
Eğitim süreci sonunda elde edilen temel metrikler aşağıda sunulmuştur:

### 4.1. Performans Metrikleri Tablosu
| Metrik | Değer |
|--------|-------|
| mAP@0.5 | 0.4905 |
| mAP@0.5:0.95 | 0.3442 |
| Kesinlik (Precision) | 0.4603 |
| Duyarlılık (Recall) | 0.7744 |

### 4.2. Sınıf Bazlı Performans
- **Negatif Sınıfı:** mAP@0.5: 0.605, Duyarlılık: 0.828 (Bu değerler önceki rapordan alınmıştır, detaylı sınıf bazlı metrikler için `results.csv` incelenmelidir.)
- **Pozitif Sınıfı:** mAP@0.5: 0.369, Duyarlılık: 0.747 (Bu değerler önceki rapordan alınmıştır, detaylı sınıf bazlı metrikler için `results.csv` incelenmelidir.)

## 5. Görselleştirmeler
Eğitim sürecinde üretilen grafikler ve görsel sonuçlar ekte sunulmuştur. Bu görseller arasında:
- **Sonuç Grafikleri (results.png):** Kayıp (loss) değerleri ve metriklerin epoch bazlı değişimi.
- **Karışıklık Matrisi (confusion_matrix.png):** Modelin sınıflar arasındaki tahmin doğruluğu.
- **Eğitim Örnekleri (labels.jpg):** Modelin eğitim sırasında gördüğü etiketli görüntüler.
- **Tahmin Örnekleri (val_batch0_pred.jpg):** Modelin doğrulama setindeki tahmin sonuçları.

## 6. Sonuç
YOLOv8n modeli, sınırlı epoch sayısına rağmen beyin tümörü tespitinde umut verici sonuçlar göstermiştir. Özellikle duyarlılık (Recall) değerinin 0.7744 olması, tümör vakalarının büyük bir kısmının başarıyla yakalandığını göstermektedir. mAP@0.5 değeri 0.4905 olarak gerçekleşmiştir. Daha yüksek epoch sayıları ve veri artırma teknikleriyle başarımın daha da artırılabileceği öngörülmektedir.
