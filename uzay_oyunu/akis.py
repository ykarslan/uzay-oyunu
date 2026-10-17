"""
akis.py - Üreteçler ve veri akış boru hattı modülü.
"""
from typing import Callable, Dict, Generator, Iterator, List, Tuple
from functools import lru_cache

def fibonacci() -> Generator[int, None, None]:
    """
    Sonsuz Fibonacci sayı dizisi üreten üreteç (generator).
    İlk değerler 0 ve 1 olarak başlar.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def yakit_gostergesi(yakit: int, tuketim: int) -> Generator[int, None, None]:
    """
    Her adımda yakıtı tüketim kadar azaltıp kalan yakıtı üreten üreteç.
    Yakıt 0'a inince veya altına düşünce 0 üretip durur.
    """
    kalan = yakit
    while kalan > 0:
        kalan = max(0, kalan - tuketim)
        yield kalan


def satirlari_oku(yol: str) -> Generator[str, None, None]:
    """
    Boş ve # ile başlayan satırları atlayarak dosya satırlarını üreten üreteç.
    """
    with open(yol, "r", encoding="utf-8") as f:
        for satir in f:
            temiz = satir.strip()
            if temiz and not temiz.startswith("#"):
                yield temiz


def ayristir(satirlar: Iterator[str]) -> Generator[Tuple[str, str, int], None, None]:
    """
    Her satırdan (kaynak, hedef, yakit) demeti üreten üreteç.
    """
    for satir in satirlar:
        parcalar = satir.split("->")
        if len(parcalar) == 2:
            kaynak = parcalar[0].strip()
            hedef_ve_yakit = parcalar[1].strip().rsplit(maxsplit=1)
            if len(hedef_ve_yakit) == 2:
                hedef = hedef_ve_yakit[0].strip()
                yakit = int(hedef_ve_yakit[1])
                yield (kaynak, hedef, yakit)


def uzun_yolculuklar(
    kayitlar: Iterator[Tuple[str, str, int]], esik: int
) -> Generator[Tuple[str, str, int], None, None]:
    """
    Yakıtı eşikten büyük olan yolculukları süzen üreteç.
    """
    for kaynak, hedef, yakit in kayitlar:
        if yakit > esik:
            yield (kaynak, hedef, yakit)

def rota_sayaci(baglantilar: Dict[str, List[str]]) -> Callable[[str, int], int]:
    """
    Gezegen bağlantılarını kullanarak verilen adımdaki rota sayısını hesaplayan
    önbellekli (@lru_cache) fonksiyon üretir.
    """
    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen: str, adim: int) -> int:
        if adim == 0:
            return 1
        komsular = baglantilar.get(gezegen, [])
        return sum(rota_sayisi(komsu, adim - 1) for komsu in komsular)

    return rota_sayisi