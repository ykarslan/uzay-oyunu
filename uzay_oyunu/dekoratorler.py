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
    """Fonksiyonun kaç kez çağrıldığını sayan dekoratör."""
    @wraps(fonk)
    def sarmalayici(*args, **kwargs):
        sarmalayici.cagri_sayisi += 1
        return fonk(*args, **kwargs)

    sarmalayici.cagri_sayisi = 0
    return sarmalayici


def log_cagri(fonk):
    """
    Her çağrıdan önce fonksiyon adını ve argümanlarını (konumsal ve adlı),
    çağrıdan sonra ise dönüş değerini yazdırır.
    """

    @wraps(fonk)
    def sarmalayici(*args, **kwargs):
        konumsal = [repr(a) for a in args]
        adli = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        tum_argumanlar = ", ".join(konumsal + adli)
        print(f"-> {fonk.__name__}({tum_argumanlar})")

        sonuc = fonk(*args, **kwargs)
        print(f"<- {fonk.__name__} = {repr(sonuc)}")
        return sonuc

    return sarmalayici

def sinirla(alt: float, ust: float):
    """
    Dekore edilen fonksiyonun ilk argümanının [alt, ust] aralığında olup olmadığını
    denetleyen, aralık dışındaysa ValueError fırlatır.
    """
    def dekorator(fonk):
        @wraps(fonk)
        def sarmalayici(*args, **kwargs):
            if args:
                deger = args[0]
            else:
                # Argüman isimli (keyword) olarak geçildiyse ilk parametreyi al
                deger = next(iter(kwargs.values()))

            if not (alt <= deger <= ust):
                raise ValueError(f"{fonk.__name__}: {deger} değeri {alt}-{ust} aralığında değil")
            return fonk(*args, **kwargs)

        return sarmalayici

    return dekorator