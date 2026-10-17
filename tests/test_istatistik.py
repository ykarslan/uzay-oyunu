"""
test_istatistik.py - istatistik modülü birim testleri.
"""
import json
from pathlib import Path
import sys

#Proje kök dizinini Python yoluna ekleme
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from uzay_oyunu.istatistik import (
    buyuk_harfli_gezegenler_map,
    buyuk_harfli_gezegenler_comp,
    en_az_iki_baglanti_filter,
    en_az_iki_baglanti_comp,
    toplam_baglanti_reduce,
    toplam_baglanti_sum,
    yolculuk,
    hizli_yolculuk,
)


def yukle_galaksi():
    yol = Path(__file__).resolve().parent.parent / "uzay_oyunu" / "galaksi.json"
    with open(yol, "r", encoding="utf-8") as f:
        return json.load(f)


def test_buyuk_harfli_gezegenler():
    galaksi = yukle_galaksi()
    gezegenler = galaksi["gezegenler"]
    beklenen = ["DÜNYA", "CENTAURI", "SIRIUS", "ORION", "KARA_DELIK"]

    assert buyuk_harfli_gezegenler_map(gezegenler) == beklenen
    assert buyuk_harfli_gezegenler_comp(gezegenler) == beklenen


def test_en_az_iki_baglanti():
    galaksi = yukle_galaksi()
    baglantilar = galaksi["baglantilar"]
    beklenen = ["dünya", "centauri", "sirius", "orion"]

    assert en_az_iki_baglanti_filter(baglantilar) == beklenen
    assert en_az_iki_baglanti_comp(baglantilar) == beklenen


def test_toplam_baglanti():
    galaksi = yukle_galaksi()
    baglantilar = galaksi["baglantilar"]
    beklenen = 10

    assert toplam_baglanti_reduce(baglantilar) == beklenen
    assert toplam_baglanti_sum(baglantilar) == beklenen


def test_hizli_yolculuk_partial():
    assert yolculuk(30, 3) == 10.0
    assert hizli_yolculuk(30) == 10.0
    assert hizli_yolculuk(9) == 3.0