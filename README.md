☕ Kahve Satış Analizi Projesi
Bu proje, bir kahve dükkanına ait satış verilerinin Python ve Pandas kullanılarak analiz edilmesini amaçlamaktadır. Ham verilerden anlamlı sonuçlar çıkarılarak satış davranışları incelenmiş, sonuçlar konsol tabanlı bir veri analizi uygulaması aracılığıyla kullanıcıya sunulmuştur.

Proje, modüler bir yapı ile geliştirilmiş olup; veri yükleme, analiz ve ana uygulama mantığı ayrı dosyalarda ele alınmıştır.


📁 Proje Yapısı

├── data/
│   └── coffee_sales.csv    # Ham satış verileri
├── analiz.py               # Veri analiz fonksiyonları ve hesaplamalar
├── veri_yukleyici.py       # Veri okuma, temizleme ve ön işleme
├── main.py                 # Menü yönetimi ve uygulama akışı
└── coffeeSales.ipynb       # Keşifsel Veri Analizi (EDA) ve Grafik Çalışmaları



🛠️ Kullanılan Teknolojiler
Python 3

Pandas Library (Veri manipülasyonu)

CSV Data Processing

Console-Based UI (Kullanıcı etkileşimi)



🚀 Projede Yapılan Analizler
📊 Toplam Ciro Hesaplama: İşletmenin genel finansal performansının ölçülmesi.

⏰ En Yoğun Satış Saatleri: Müşteri trafiğinin gün içindeki dağılımı.

☕ En Çok Satılan Ürünler: Adet bazlı popülerlik analizi.

💰 En Çok Kazandıran Ürünler: Ürün bazlı gelir katkısı analizi.

📅 Günlük Satış Yoğunluğu: Haftalık performans takibi.

🗓️ Hafta İçi / Hafta Sonu Kıyaslaması: Dönemsel trend analizi.



📊 Veriden Çıkarılan Temel İçgörüler (Business Insights)
Ciro Lideri: Latte, adet bazında en çok satılan ürün olmamasına rağmen, birim fiyat etkisiyle toplam ciroda yaklaşık 27.866 TL ile en yüksek paya sahiptir.

Operasyonel Verimlilik: Satışların en yoğun gerçekleştiği saat 10:00 olarak tespit edilmiştir. Bu zaman aralığı, personel planlaması ve stok yönetimi için kritik bir içgörü sunar.

Popüler Ürün: Americano with Milk, 824 adet ile en çok tercih edilen kahve türüdür; müşteri sadakatini ölçmede önemli bir göstergedir.

Ödeme Alışkanlıkları: Nakit ve kart ödemeleri analiz edilerek, müşteri ödeme tercihlerine göre kasa operasyonlarının hızı ve verimliliği üzerine stratejiler geliştirilmiştir.
