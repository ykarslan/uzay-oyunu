from pathlib import Path
import sys
import time
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from uzay_oyunu.dekoratorler import sure_olc, say, log_cagri, sinirla


def test_sure_olc(capsys):
    @sure_olc
    def ornek_fonk():
        time.sleep(0.01)
        return "bitti"

    sonuc = ornek_fonk()
    assert sonuc == "bitti"
    yakalanan = capsys.readouterr()
    assert "ornek_fonk çalisma süresi:" in yakalanan.out or "sürdü" in yakalanan.out or "sn" in yakalanan.out


def test_say():
    @say
    def faktoriyel(n):
        if n <= 1:
            return 1
        return n * faktoriyel(n - 1)

    assert faktoriyel(4) == 24
    assert faktoriyel.cagri_sayisi == 4


def test_log_cagri(capsys):
    @log_cagri
    def yolculuk(hedef, hiz=1):
        return f"{hedef} hiz={hiz}"

    sonuc = yolculuk("orion", hiz=3)
    assert sonuc == "orion hiz=3"
    yakalanan = capsys.readouterr()
    assert "-> yolculuk('orion', hiz=3)" in yakalanan.out
    assert "<- yolculuk = 'orion hiz=3'" in yakalanan.out


def test_sinirla_dekoratoru():
    @sinirla(0, 100)
    def yakit_harca(miktar, mevcut_yakit=100):
        return mevcut_yakit - miktar

    # Normal değer ve sınır değerleri (0 ve 100)
    assert yakit_harca(30) == 70
    assert yakit_harca(0) == 100
    assert yakit_harca(100) == 0

    # Aralık dışı üst sınır hatası (150)
    with pytest.raises(ValueError):
        yakit_harca(150)

    # Aralık dışı alt sınır hatası (-5)
    with pytest.raises(ValueError):
        yakit_harca(-5)
