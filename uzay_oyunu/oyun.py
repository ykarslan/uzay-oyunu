import json

def envanter_metni(credits: bool,engines: bool, copilot: bool)->str:
    """Sahip olunan esyaları listeler; hiçbiri yoksa boş metin döndürür."""
    esyalar = []
    if credits:
        esyalar.append("bol kredi")
    if engines:
        esyalar.append("güçlü motorlar")
    if copilot:
        esyalar.append("yetenekli bir pilot")

    return f"Sende: {', '.join(esyalar)}" if esyalar else ""
def hedef_menusu(hedefler: list[str]) -> str:
    """Gidilebilecek hedefleri numaralandırılmış metni menüsü olarak döndürür."""
    satirlar = ["Nereye gitmek istersin?"]
    for i, hedef in enumerate(hedefler, start=1):
         satirlar.append(f"[{i}] {hedef}")
    return "\n".join(satirlar)

def galaksi_kur(gezegenler: list[str], baglantilar: dict[str, list[str]], baslangic: str, **kwargs) -> dict:
    """Galaksi haritasını doğrular ve oyun başlangıç durumunu kurar."""
    if baslangic not in gezegenler:
        raise ValueError(f"Başlangıç gezegeni ({baslangic}) listede yok!")
    yakit = kwargs.get("yakit", 50)
    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit,
        **kwargs
    }
def travel(galaksi: dict, planet: str) -> list[str]:
    """Belirtilen gezegenden gidilebilecek bağlantılı gezegenlerin listesini döner."""
    return galaksi["baglantilar"][planet]