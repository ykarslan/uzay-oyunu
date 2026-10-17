"""
istatistik.py - map, filter, reduce ve functools.partial fonksiyonel programlama modülü.
"""
from functools import partial, reduce
from typing import Dict, List


#1. Gezegen adlarının büyük harfli listesi
def buyuk_harfli_gezegenler_map(gezegenler: List[str]) -> List[str]:
    """map kullanarak gezegen adlarını büyük harfe çevirir."""
    return list(map(str.upper, gezegenler))


def buyuk_harfli_gezegenler_comp(gezegenler: List[str]) -> List[str]:
    """Liste üreteci (comprehension) kullanarak gezegen adlarını büyük harfe çevirir."""
    return [g.upper() for g in gezegenler]


#2. En az iki bağlantısı olan gezegenler
def en_az_iki_baglanti_filter(baglantilar: Dict[str, List[str]]) -> List[str]:
    """filter kullanarak en az 2 komşusu/bağlantısı olan gezegenleri seçer."""
    return list(filter(lambda g: len(baglantilar[g]) >= 2, baglantilar.keys()))


def en_az_iki_baglanti_comp(baglantilar: Dict[str, List[str]]) -> List[str]:
    """Liste üreteci kullanarak en az 2 komşusu/bağlantısı olan gezegenleri seçer."""
    return [g for g, komsular in baglantilar.items() if len(komsular) >= 2]


#3. Toplam bağlantı sayısı
def toplam_baglanti_reduce(baglantilar: Dict[str, List[str]]) -> int:
    """reduce kullanarak grafikteki toplam bağlantı sayısını hesaplar."""
    uzunluklar = [len(komsular) for komsular in baglantilar.values()]
    return reduce(lambda x, y: x + y, uzunluklar, 0)


def toplam_baglanti_sum(baglantilar: Dict[str, List[str]]) -> int:
    """sum fonksiyonu kullanarak grafikteki toplam bağlantı sayısını hesaplar."""
    return sum(len(komsular) for komsular in baglantilar.values())


#4. functools.partial ile yolculuk fonksiyonu
def yolculuk(mesafe: float, hiz: float) -> float:
    """Verilen mesafe ve hız ile yolculuk süresini hesaplar."""
    return mesafe / hiz


#hiz=3 parametresi sabitlenmiş yeni fonksiyon
hizli_yolculuk = partial(yolculuk, hiz=3)