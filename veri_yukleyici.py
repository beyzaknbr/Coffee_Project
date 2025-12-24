import pandas as pd

def veri_yukle(dosya_yolu):
    try:
        df = pd.read_csv(dosya_yolu)
        df['datetime'] = pd.to_datetime(df['datetime']) #datetime i tarih yaptik
        df['card'] = df['card'].fillna('cash')
        df['hour'] = df['datetime'].dt.hour
        df['day_name'] = df['datetime'].dt.day_name()

        print("Veri başarıyla yüklendi")
        return df
    except FileNotFoundError:
        print("Dosya Bulunamadı")
        return None
    except Exception as e:
        print("Beklenmeyen hata oluştu",e)
        return None  
if __name__ == "__main__":
    df = veri_yukle("data/coffee_sales.csv")
    print(df.head())