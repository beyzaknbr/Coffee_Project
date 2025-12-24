import pandas as pd

#En yoğun saatler
def en_yogun_saat(df):
    enYogun = df.groupby('hour')['money'].sum()
    return enYogun.sort_values(ascending = False)

#En çok satılan kahveler
def en_cok_satilan_kahve(df):
    return df['coffee_name'].value_counts().sort_values(ascending =False)
    

#En çok kazandıran kahveler
def en_yuksek_kahve_fiyat(df):
    return df.groupby('coffee_name')['money'].sum().sort_values(ascending = False)
    
#En yoğun gün
def en_yogun_gun(df):
    return df.groupby('day_name')['money'].sum()

#Haftasonu mu
def haftasonu(df):
    return df[df['day_name'].isin(['Saturday', 'Sunday'])]['money'].sum()


#Haftaiçi
def haftaici(df):
    return df[~df['day_name'].isin(['Saturday', 'Sunday'])]['money'].sum()

#Toplam Satış
def toplam_ciro(df):
    return df['money'].sum()
    
#Ödeme Türüne Göre
def odeme_turu_analizi(df):
    return df.groupby('cash_type')['money'].mean()