# 🧠 VeriFace - Sketch to Real Face Generation with Pix2Pix

**Veriface**, sadece eskiz (sketch) görselleri kullanarak gerçekçi yüz fotoğrafları üretmek için geliştirilmiş bir görüntüden görüntüye çeviri projesidir. Projede [Pix2Pix](https://phillipi.github.io/pix2pix/) GAN mimarisi kullanılmıştır.
> 📌 **Not:** Bu projede kullanılan Pix2Pix mimarisi literatürde tanımlı bir yapıdır. Ancak bu çalışma kapsamında model tamamen **kişisel veri seti ile sıfırdan eğitilmiş**, herhangi bir hazır (pretrained) model ağırlığı kullanılmamıştır.


## 📁 Proje Yapısı

```
Veriface/
├── pytorch-CycleGAN-and-pix2pix/      # Ana model kodları
├── performans.py                      # SSIM ve PSNR değerlendirme scripti
├── README.md                          # Bu dosya
├── results/                           # Test çıktıları (çıkarılabilir)
├── checkpoints/                       # Eğitim çıktıları (çıkarılabilir)
└── newdataset/                        # A|B formatlı görseller (yüklenmez)
```

## 🧪 Kullanılan Veri Seti

- [CUHK Face Sketch Database (CUFS)](https://github.com/junhocho/FSNet/blob/master/README.md#cufs-dataset) baz alınarak oluşturulmuştur.
- Toplam ~10.000 örnekten oluşan A|B hizalanmış yüz ve sketch çiftleri kullanılmıştır.
- Eğitim ve test verileri `newdataset/train` ve `newdataset/test` klasörlerine yerleştirilmiştir (bu klasör `.gitignore` ile dışlanmıştır).

## 🚀 Eğitim Komutu

python train.py --dataroot ./newdataset --name veriface_pix2pix --model pix2pix --direction AtoB --batch_size 4 --n_epochs 50 --n_epochs_decay 50 --gpu_ids 0 --display_id -1

> Eğitim tamamlandığında `./checkpoints/veriface_pix2pix/` klasörüne model ağırlıkları kaydedilir.

## 🧪 Test Komutu

python test.py --dataroot ./newdataset --name veriface_pix2pix --model pix2pix --direction AtoB --epoch 60 --gpu_ids 0

> Test çıktıları `./results/veriface_pix2pix/test_50/images/` klasörüne kaydedilir.

## 📊 Performans Ölçütleri (60 Epoch Eğitim Sonrası)

Aşağıdaki metrikler 60 epoch eğitim sonrası hesaplanmıştır.  
`performans.py` scripti ile SSIM ve PSNR değerleri elde edilmiştir.

| Metrik | Sonuç      |
|--------|------------|
| SSIM   | 0.4583     |
| PSNR   | 15.06 dB   |

## 📸 Örnek Çıktılar

> Aşağıdaki örnek test verisinden alınmıştır.


<p align="center">
  <img src="./demo_outputs/89_real_A.png" width="200"/>
  <img src="./demo_outputs/89_fake_B.png" width="200"/>
  <img src="./demo_outputs/89_real_B.png" width="200"/>
  <br>
  <i>Soldan sağa: Girdi (eskiz) | Üretilen Görsel | Gerçek Görsel</i>
</p>


> Daha fazla çıktı için `results/veriface_pix2pix/test_20/images/` klasörüne bakabilirsiniz.

## 🛠 Gereksinimler

torch  
torchvision  
opencv-python  
scikit-image  
tqdm  

Tüm kütüphaneleri tek seferde kurmak için:

pip install -r requirements.txt

## 📌 Notlar

- Bu proje sadece eğitim ve araştırma amaçlı geliştirilmiştir.
- Yüksek kaliteli çıktı için daha fazla epoch, veri büyütme ve stil kaybı (perceptual loss) gibi eklemeler yapılabilir.
- Eğitim verisi GitHub’a yüklenmemiştir.

## 👩‍💻 Geliştiren

**Elif Rana Karabulut**  
3. sınıf Yapay Zeka Mühendisliği Öğrencisi  
Ostim Teknik Üniversitesi
