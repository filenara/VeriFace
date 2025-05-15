# 🎭 VeriFace – Tanık İfadesinden Şüpheli Yüz Eskizi Üreten Yapay Zekâ Sistemi

## 📌 Proje Tanımı
**VeriFace**, bir tanığın sözlü ifadesine dayanarak, olası şüphelinin yüzünü **karakalem eskiz tarzında** görselleştiren, tamamen yerel çalışan bir yapay zekâ sistemidir.

Bu proje, yapay zekâ destekli adli analiz uygulamalarının bir prototipidir ve *üretken yapay zekâ* tekniklerini kullanarak sözlü tariften görsel üretmeyi hedefler.

---

## 🎯 Projenin Amacı
- Kullanıcının verdiği tanık tarifinden AI destekli bir **şüpheli yüz eskizi** üretmek  
- Kısa sürede etkili bir demo ve teknik gösterim sunmak

---

## 🖥️ Kullanılan Teknolojiler
| Bileşen | Açıklama |
|--------|----------|
| **Stable Diffusion WebUI (yerel)** | Metinden görsel üretimi sağlar |
| **Prompt Yapılandırması** | Tanık ifadeleriyle uyumlu metin komutları hazırlanır |
| **Python** | Girdi okuma, çıktı yönetimi ve dosyalama |

---

## 🔧 Sistem Mimarisi
```
[Tanık Tarifi (Türkçe)] → [İngilizce Prompt'a Dönüştürme] → [Stable Diffusion WebUI] → [Eskiz.png]
```

---

## ✍️ Örnek Tanık İfadesi
```text
30'larında, kısa saçlı, kalın kaşlı, sinirli bakışlı bir adam
```

Çeviri sonrası prompt örneği:
```text
A man in his 30s with short hair, thick eyebrows, angry expression, pencil sketch style, grayscale
```

---

## 📂 Proje Klasör Yapısı
```
veriface/
├── ifadeler.txt              # Tanık tarifleri (Türkçe)
├── cevir_ve_uret.py          # Prompt çevirisi ve görsel üretimi
├── cikti_gorseller/          # Üretilen eskizler
├── stable-diffusion-webui/   # Yerel üretim arayüzü
├── README.md
└── requirements.txt          # Ortam bağımlılıkları
```

---


## 📊 Sonuçlar ve Yorum
VeriFace, tanık ifadelerinin yapay zekâ ile görselleştirilmesi konusunda ilk adım niteliğindedir.

Projede kullanılan yöntemler şunları göstermektedir:
- Kısa ve doğal tanık ifadeleri ile karakteristik yüzler üretilebilmektedir  
- Karakalem estetiği, şüpheliye dair genel bir fikir vermek için yeterlidir  
- Metin → görsel üretim hatları, sade ve güçlü uygulamalara dönüşebilir

---

## 🔮 Gelecekte Geliştirilebilecek Yönler
- Türkçe'den İngilizce'ye otomatik çeviri entegrasyonu  
- Aynı tariften birden fazla varyasyon üretimi  
- Farklı tanıklardan gelen tariflerin birleştirilmesi  
- Eskizden fotogerçekçi yüze geçiş modeli

---

## 🧑‍💻 Geliştirici
> Bu proje Elif Rana Karabulut tarafından, üretken yapay zekâ alanında bireysel araştırma ve demo amaçlı geliştirilmiştir.
