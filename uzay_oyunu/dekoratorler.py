"""
uzay_oyunu.dekoratorler - Özel fonksiyon dekoratörleri
"""
from functools import wraps
import time


def sure_olc(fonk):
    """
    Sarmalanan fonksiyonun çalısma süresini time.perf_counter() ile ölcer,
    '{fonksiyon_adi}: {sure:.4f} sn' biçiminde konsola yazdırır
    """
    @wraps(fonk)
    def sarmalayici(*args, **kwargs):
        baslangic = time.perf_counter()
        sonuc = fonk(*args, **kwargs)
        bitis = time.perf_counter()
        gecen_sure = bitis - baslangic
        print(f"{fonk.__name__}: {gecen_sure:.4f} sn")
        return sonuc

    return sarmalayici

def say(fonk):
    """
    Fonksiyonun toplam çağrılma sayısını 'cagri' niteliğinde tutan dekoratör.
    """
    @wraps(fonk)
    def sarmalayici(*args, **kwargs):
        sarmalayici.cagri += 1
        return fonk(*args, **kwargs)

    sarmalayici.cagri = 0
    return sarmalayici