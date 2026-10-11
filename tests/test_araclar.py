from uzay_oyunu.araclar import hamle_sayaci, en_bagli_gezegenler, sure_olc


def test_hamle_sayaci():
    sayac = hamle_sayaci()
    assert sayac() == 1
    assert sayac() == 2
    assert sayac() == 3

    # Yeni bir sayaç bağımsız başlamalı
    yeni_sayac = hamle_sayaci()
    assert yeni_sayac() == 1


def test_en_bagli_gezegenler():
    galaksi = {
        "gezegenler": ["dunya", "mars", "sirius", "orion"],
        "baglantilar": {
            "dunya": ["mars"],
            "mars": ["dunya", "sirius", "orion"],
            "sirius": ["mars", "dunya"],
            "orion": ["mars", "dunya"]
        }
    }
    # mars (3 bağlantı) en başta olmalı.
    # sirius ve orion (2 bağlantı): alfabetik olarak orion önce gelmeli.
    # dunya (1 bağlantı) en sonda olmalı.
    sirali = en_bagli_gezegenler(galaksi)
    assert sirali == ["mars", "orion", "sirius", "dunya"]


def test_sure_olc():
    @sure_olc
    def topla(a, b):
        return a + b

    assert topla(3, 5) == 8