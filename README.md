# 🎓 HesaplaGeç - Üniversite Not Hesaplayıcı ve Tahmin Aracı

Öğrencilerin "Acaba dersten geçecek miyim?", "Finalde kaç almam lazım?" veya "FF gelir mi?" gibi stresli sorularına son veren, interaktif ve dinamik bir not hesaplama aracıdır. Başta **Yönetim Bilişim Sistemleri (MIS)** öğrencileri olmak üzere tüm üniversite öğrencilerinin kullanımına uygundur.

## 🌟 Özellikler

* **🌍 Çoklu Dil Desteği:** Türkçe, Arapça ve İngilizce arayüz seçenekleri.
* **📊 İstatistiksel Analiz:** Z-Score mantığı kullanılarak vize notu ve sınıf ortalamasına göre tahmini sınıf sıralaması hesaplama.
* **🎯 Hedef Odaklı Hesaplama:** İstenen dönem sonu notuna (örneğin CC veya AA) ulaşmak için finalde alınması gereken minimum notu bulma.
* **🤔 "What-If" (Tahmin) Senaryoları:** Finalde alınması beklenen nota göre genel ortalamayı önceden görme.
* **📥 Sonuç İndirme:** Hesaplanan notları ve durumu şık bir PNG raporu olarak cihaza kaydetme.

## 🛠️ Kullanılan Teknolojiler

Proje tamamen **Python** ile geliştirilmiş olup aşağıdaki kütüphaneleri kullanmaktadır:
* `Streamlit`: Dinamik ve etkileşimli web arayüzü için.
* `SciPy`: Sınıf içi tahmini başarı sıralamasının (yüzdelik dilim) hesaplanması için.
* `Matplotlib`: Sonuç raporunun görsel (PNG) olarak oluşturulması için.

## 🚀 Kurulum ve Çalıştırma (Lokalde)

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1.  **Depoyu Klonlayın:**
    ```bash
    git clone [https://github.com/KULLANICI_ADINIZ/hesaplagec.git](https://github.com/KULLANICI_ADINIZ/hesaplagec.git)
    cd hesaplagec
    ```

2.  **Gerekli Kütüphaneleri Yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Uygulamayı Başlatın:**
    ```bash
    streamlit run app.py
    ```
    *(Uygulama otomatik olarak `http://localhost:8501` adresinde tarayıcınızda açılacaktır.)*

## 💡 Geliştirici
**Mohamed Said** *Bu proje, öğrencilerin akademik hayatını kolaylaştırmak ve streslerini azaltmak amacıyla açık kaynaklı olarak geliştirilmiştir.*
