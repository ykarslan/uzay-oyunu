from typing import Callable, Dict, Tuple

KOMUTLAR: Dict[str, Tuple[Callable, str]] = {}


def komut(ad: str, aciklama: str = ""):
    def dekorator(fonk: Callable):
        if ad in KOMUTLAR:
            raise ValueError(f"'{ad}' adinda bir komut zaten kayitli!")
        KOMUTLAR[ad] = (fonk, aciklama)
        return fonk

    return dekorator


@komut("yardim", aciklama="komutları listeler")
def komut_yardim(durum: dict) -> str:
    satirlar = []
    for ad, (_, aciklama) in sorted(KOMUTLAR.items()):
        satirlar.append(f"{ad:<10} {aciklama}")
    return "\n".join(satirlar)


@komut("envanter", aciklama="eşyalarını gösterir")
def komut_envanter(durum: dict) -> str:
    credits = durum.get("credits", False)
    engines = durum.get("engines", False)
    copilot = durum.get("copilot", False)
    return f"Krediler: {credits}, Motorlar: {engines}, Yardimci Pilot: {copilot}"


@komut("harita", aciklama="gidebileceğin gezegenleri gösterir")
def komut_harita(durum: dict) -> str:
    konum = durum.get("konum", "")
    baglantilar = durum.get("baglantilar", {})
    komsular = baglantilar.get(konum, [])
    return ", ".join(komsular)