import time


def hamle_sayaci():
    """Her çağrıldığında 1 artan bir sayaç fonksiyonu döndürür (closure & nonlocal)."""
    sayac = 0

    def arttir():
        nonlocal sayac
        sayac += 1
        return sayac

    return arttir


def en_bagli_gezegenler(galaksi: dict) -> list[str]:
    """
    Gezegenleri bağlantı sayısına göre azalan,
    eşitlik durumunda alfabetik sırayla döndürür.
    """
    baglantilar = galaksi.get("baglantilar", {})
    gezegenler = list(galaksi.get("gezegenler", []))

    # Bağlantı sayısı azalan (-len), isim alfabetik artan (+isim)
    return sorted(gezegenler, key=lambda g: (-len(baglantilar.get(g, [])), g))


# Bonus
def sure_olc(fonksiyon):
    """Verilen fonksiyonun çalışma süresini ölçen bir sarmalayıcı döndürür."""
    def sarmalayici(*args, **kwargs):
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.perf_counter()
        gecen_sure = bitis - baslangic
        print(f"{fonksiyon.__name__} çalışma süresi: {gecen_sure:.6f} saniye")
        return sonuc

    return sarmalayici