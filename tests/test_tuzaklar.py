# (a) Hatalı fonksiyonun None kalıbıyla düzeltilmiş hali
def yakit_ekle(miktar: int, depo: list[int] = None) -> list[int]:
    """Varsayılan argüman olarak liste yerine None kullanılarak tuzak önlenmiştir."""
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo


def test_yakit_ekle_bagimsiz_cagrilar():
    # İlk çağrı bağımsız çalışır
    sonuc1 = yakit_ekle(10)
    assert sonuc1 == [10]

    # İkinci çağrıda eski liste tutulmamalı, yeni liste üretilmeli
    sonuc2 = yakit_ekle(20)
    assert sonuc2 == [20]


def test_yakit_ekle_var_olan_depo():
    # Dışarıdan açıkça verilen listeye ekleme yapabilmeli
    mevcut = [5, 10]
    sonuc = yakit_ekle(15, mevcut)
    assert sonuc == [5, 10, 15]