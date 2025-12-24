☕ Kahve Satış Analizi Projesi

Bu proje, bir kahve dükkanına ait satış verilerinin Python ve Pandas kullanılarak analiz edilmesini amaçlamaktadır.
Ham verilerden anlamlı sonuçlar çıkarılarak satış davranışları incelenmiş, sonuçlar konsol tabanlı bir veri analizi uygulaması aracılığıyla kullanıcıya sunulmuştur.

Proje, modüler bir yapı ile geliştirilmiş olup; veri yükleme, analiz ve ana uygulama mantığı ayrı dosyalarda ele alınmıştır.

📁 Proje Yapısı
├── data/
│   └── coffee_sales.csv
├── analiz.py          # Veri analiz fonksiyonları
├── veri_yukleyici.py  # Veri okuma ve ön işleme
├── main.py            # Menü ve uygulama akışı
└── coffeeSales.ipynb  # Keşifsel Veri Analizi (EDA)

🛠️ Kullanılan Teknolojiler

Python 3

Pandas

CSV veri işleme

Konsol tabanlı kullanıcı menüsü


🚀 Projede Yapılan Analizler

📊 Toplam ciro hesaplama

⏰ En yoğun satış saatlerinin analizi

☕ En çok satılan kahve türleri (adet bazlı)

💰 En çok ciro getiren kahve türleri

📅 Günlere göre satış yoğunluğu

🗓️ Hafta içi ve hafta sonu satış karşılaştırması


📊 Veriden Çıkarılan Temel İçgörüler

Ciro Lideri: Latte, adet bazında en çok satılan ürün olmamasına rağmen, birim fiyat etkisiyle toplam ciroda en yüksek paya sahiptir.

Operasyonel Verimlilik: Satışların en yoğun gerçekleştiği saat 10:00 olarak tespit edilmiştir. Bu zaman aralığı, personel planlaması ve stok yönetimi için kritik öneme sahiptir.

Popüler Ürün: Americano with Milk, adet bazında en çok satılan kahve türüdür ve müşteri tercihlerini anlamada önemli bir göstergedir.

Ödeme Alışkanlıkları: Nakit ve kart ile yapılan ödemeler karşılaştırılmış; ödeme yöntemlerine göre harcama eğilimleri analiz edilerek operasyonel süreçlerin optimize edilebileceği görülmüştür.
