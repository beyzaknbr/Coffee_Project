from veri_yukleyici import veri_yukle
from analiz import (
    en_yogun_saat,
    en_cok_satilan_kahve,
    en_yuksek_kahve_fiyat,
    en_yogun_gun,
    haftasonu,
    haftaici,
    toplam_ciro
)

def main():
    df = veri_yukle("data/coffee_sales.csv")

    if df is None:
        print("Veri yüklenemedi, program sonlandırılıyor.")
        return
    secim=""
    while secim !='q':
        print("\n--- KAHVE SATIŞ ANALİZİ ---\n")
        print("Lütfen yapmak istediğiniz işlemi seçin")
        print("1. Genel Toplam Ciro")
        print("2. En Yoğun Satış Saatleri")
        print("3. En Çok Satılan Ürünler (Adet)")
        print("4. En Çok Kazandıran Ürünler (Ciro)")
        print("5. Hafta İçi / Hafta Sonu Kıyaslaması")
        print("6. Günlük Yoğunluk Tablosu")
        print("q. Çıkış")
    
        secim  = input("Seçiminizi yapınız:")
        print("\n")
        if secim =="1":
            print(f"Toplam Ciro:{toplam_ciro(df):.2f} TL")
        elif secim =="2":
            print("En yoğun saatler:")
            print(en_yogun_saat(df))
        elif secim =="3":
            print("En çok satılan kahveler")
            print(en_cok_satilan_kahve(df))
        elif secim =="4":
            print("En çok ciro yapan ürünler")
            print(en_yuksek_kahve_fiyat(df))
        elif secim =="5":
            print(f"Haftaiçi Toplam:{haftaici(df):2f}")
            print(f"Haftasonu Toplam:{haftasonu(df):.2f}")
        elif secim =="6":
            print("Günlere göre yoğunluk:")
            print(en_yogun_gun(df))
        elif secim.lower() =='q':
            print("Çıkış yapılıyor")
            break
        else:
            print("Hatalı giriş yaptınız")

    


if __name__ == "__main__":
    main()
