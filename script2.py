#görev1
celsius = float(input("Sıcaklık (C):"))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius} C = {fahrenheit} F")

#görev2
PI=3.14159
yarıcap = float(input("Yarıcap"))
yukseklik = float(input("Yükseklik"))
taban_alani = PI * (yarıcap ** 2) #üs almak için ** kullanılır
hacim = taban_alani * yukseklik
print(f"Taban alanı: {taban_alani}")
print(f"Hacim: {hacim}")

#görev3
toplam_saniye = int(input("Saniye:"))
gun = toplam_saniye // 86400
kalan = toplam_saniye % 86400
saat = kalan // 3600
kalan = kalan % 3600
dakika = kalan // 60
saniye= kalan % 60
print(f"{toplam_saniye} saniye= {gun} gün {saat} saat {dakika} dakika {saniye} saniye")

#görev4
sayi = int(input("Sayı (0-999): "))
birler = sayi % 10
onlar = (sayi // 10) % 10
yuzler = sayi // 100
toplam = yuzler + onlar + birler
print (f"Rakamlar toplamı: {toplam}")

#görev5
anapara = float(input("Anapara (TL): "))
yillik_faiz = float(input("Yıllık faiz (%): "))
sure = float(input("Süre (yıl): "))
gelecekteki_deger = anapara * (1 + yillik_faiz / (12*100)) ** (12* sure)
sonuc = round (gelecekteki_deger, 2)
print(f"Gelecekteki değer: {sonuc} TL")