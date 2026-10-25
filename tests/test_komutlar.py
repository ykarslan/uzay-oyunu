from pathlib import Path
import sys
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from uzay_oyunu.komutlar import KOMUTLAR, komut, komut_yardim, komut_envanter, komut_harita


def test_komut_kayit_ve_mukerrer_hata():
    @komut("test_cmd", aciklama="test aciklamasi")
    def ornek_fonk(durum):
        return "ok"

    assert "test_cmd" in KOMUTLAR
    assert KOMUTLAR["test_cmd"][1] == "test aciklamasi"

    with pytest.raises(ValueError):
        @komut("test_cmd")
        def ikinci_ornek(durum):
            pass


def test_komut_yardim():
    cikti = komut_yardim({})
    assert "yardim" in cikti or "yardım" in cikti
    assert "envanter" in cikti
    assert "harita" in cikti


def test_komut_envanter():
    durum = {"credits": True, "engines": False, "copilot": True}
    cikti = komut_envanter(durum)
    assert "True" in cikti
    assert "False" in cikti


def test_komut_harita():
    durum = {
        "konum": "dünya",
        "baglantilar": {"dünya": ["centauri", "sirius"]},
    }
    cikti = komut_harita(durum)
    assert cikti == "centauri, sirius"