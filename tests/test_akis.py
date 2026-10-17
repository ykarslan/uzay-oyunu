"""test_akis.py - akis modülü birim testleri."""

import itertools
from pathlib import Path
import sys

# Projenin kök dizinini Python arama yoluna dahil et
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from uzay_oyunu.akis import fibonacci


def test_fibonacci():
    #1. next() ile ilk üç değer: (0, 1, 1)
    g1 = fibonacci()
    assert (next(g1), next(g1), next(g1)) == (0, 1, 1)

    #2. itertools.islice ile ilk 12 değer
    ilk_12 = list(itertools.islice(fibonacci(), 12))
    beklenen = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert ilk_12 == beklenen

    #3. itertools.takewhile ile 100'den küçük değerler
    kucuk_100 = list(itertools.takewhile(lambda x: x < 100, fibonacci()))
    assert kucuk_100 == beklenen

    #4. Üretecin tek kullanımlık olduğunu doğrulama
    g2 = fibonacci()
    dilim_1 = list(itertools.islice(g2, 5))
    dilim_2 = list(itertools.islice(g2, 5))
    assert dilim_1 == [0, 1, 1, 2, 3]
    assert dilim_2 == [5, 8, 13, 21, 34]
    assert dilim_1 != dilim_2