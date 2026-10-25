"""
test_dekoratorler.py - testler.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from uzay_oyunu.dekoratorler import sure_olc


def test_sure_olc_sonuc_ve_cikti(capsys):
    """1. Test: Fonksiyonun gercek donus degerini degistirmeden dondurdugunu ve ekrana dogru formatta yazdigini test eder."""
    @sure_olc
    def topla(a, b):
        return a + b

    sonuc = topla(15, 25)
    assert sonuc == 40

    yakalanan = capsys.readouterr()
    assert "topla:" in yakalanan.out
    assert "sn" in yakalanan.out


def test_sure_olc_adli_argumanlar():
    """2. Test: Fonksiyonun adli argumanlarla (kwargs) dogru sekilde calistigini dogrular."""
    @sure_olc
    def kisi_karsila(ad, selamlama="Merhaba"):
        return f"{selamlama}, {ad}!"

    cikti1 = kisi_karsila("Gezgin", selamlama="Hos geldin")
    assert cikti1 == "Hos geldin, Gezgin!"

    cikti2 = kisi_karsila(ad="Kaptan", selamlama="Gunaydin")
    assert cikti2 == "Gunaydin, Kaptan!"


def test_sure_olc_metadata_korunumu():
    """3. Test: wraps sayesinde __name__ ve __doc__ niteliklerinin korundugunu dogrular."""
    @sure_olc
    def ornek_fonksiyon(x):
        """Bu ornek fonksiyonun belgelendirme metnidir."""
        return x * 2

    assert ornek_fonksiyon.__name__ == "ornek_fonksiyon"
    assert ornek_fonksiyon.__doc__ == "Bu ornek fonksiyonun belgelendirme metnidir."