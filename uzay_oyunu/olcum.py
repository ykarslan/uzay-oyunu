import json
from pathlib import Path
import time
from uzay_oyunu.akis import rota_sayaci

#galaksi.json dosyasını oku
with open("uzay_oyunu/galaksi.json", "r", encoding="utf-8") as f:
    galaksi = json.load(f)

baglantilar = galaksi["baglantilar"]


#1. Önbelleksiz Fonksiyon
def rota_sayisi_onbelleksiz(gezegen: str, adim: int) -> int:
    if adim == 0:
        return 1
    return sum(
        rota_sayisi_onbelleksiz(komsu, adim - 1)
        for komsu in baglantilar.get(gezegen, [])
    )


#Önbelleksiz süre ölçümü (adim=20)
baslangic = time.perf_counter()
sonuc_onbelleksiz = rota_sayisi_onbelleksiz("dünya", 20)
sure_onbelleksiz = time.perf_counter() - baslangic

#2. Önbellekli Fonksiyon (@lru_cache)
say_onbellekli = rota_sayaci(baglantilar)

#Önbellekli süre ölçümü (adim=20)
baslangic = time.perf_counter()
sonuc_onbellekli = say_onbellekli("dünya", 20)
sure_onbellekli = time.perf_counter() - baslangic

#Bilgileri ekrana yazdır
print(f"Sonuç: {sonuc_onbellekli}")
print(f"Önbelleksiz Süre (adim=20): {sure_onbelleksiz:.6f} saniye")
print(f"Önbellekli Süre (adim=20)  : {sure_onbellekli:.6f} saniye")
print(f"cache_info() Çıktısı       : {say_onbellekli.cache_info()}")