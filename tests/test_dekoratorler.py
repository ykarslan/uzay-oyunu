"""
test_dekoratorler.py - testler.
"""
from uzay_oyunu.dekoratorler import sure_olc, say
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


from functools import lru_cache


def test_say_dekoratoru_ve_sirasi():
    """Görev 2: Fibonacci fonksiyonunun 3 farklı dekoratör dizilimi için çağrı sayılarını test eder."""

    #1. Durum: Yalnızca @say
    @say
    def fib1(n):
        if n < 2:
            return n
        return fib1(n - 1) + fib1(n - 2)

    fib1(20)
    assert fib1.cagri == 21891

    #2. Durum: @say üstte, @lru_cache altta
    @say
    @lru_cache(maxsize=None)
    def fib2(n):
        if n < 2:
            return n
        return fib2(n - 1) + fib2(n - 2)

    fib2(20)
    assert fib2.cagri == 39

    #3. Durum: @lru_cache üstte, @say altta
    @lru_cache(maxsize=None)
    @say
    def fib3(n):
        if n < 2:
            return n
        return fib3(n - 1) + fib3(n - 2)

    fib3(20)
    assert fib3.__wrapped__.cagri == 21