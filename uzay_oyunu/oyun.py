from uzay_oyunu.dekoratorler import log_cagri, sinirla
from uzay_oyunu.komutlar import KOMUTLAR

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
@log_cagri
def hedef_menusu(hedefler: list[str]) -> str:
    ...
def hedef_menusu(hedefler: list[str]) -> str:
    """Gidilebilecek hedefleri numaralandırılmış metni menüsü olarak döndürür."""
    satirlar = ["Nereye gitmek istersin?"]
    for i, hedef in enumerate(hedefler, start=1):
         satirlar.append(f"[{i}] {hedef}")
    return "\n".join(satirlar)

@log_cagri
def galaksi_kur(gezegenler: list[str], baglantilar: dict[str, list[str]], baslangic: str, **kwargs) -> dict:
    ...
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
    """Belirtilen gezegenden gidilebilecek baglantili gezegenlerin listesini doner."""
    komsular = galaksi["baglantilar"][planet]

    while True:
        print("\nNereye gitmek istersin?")
        print(hedef_menusu(komsular))

        girdi = input("> ").strip()

        #Girdi bir komutsa (yardim, envanter, harita vb.) calistir ve ayni menuyu tekrar goster
        if girdi in KOMUTLAR:
            fonk, _ = KOMUTLAR[girdi]
            durum = {
                "konum": planet,
                "baglantilar": galaksi.get("baglantilar", {}),
                "credits": galaksi.get("credits", False),
                "engines": galaksi.get("engines", False),
                "copilot": galaksi.get("copilot", False),
            }
            sonuc = fonk(durum)
            print(sonuc)
            continue

        #Girdi bir komut değilse, eskisi gibi gezegen seçimi olarak komşuları dondürür
        return komsular

    @sinirla(0, 100)
    def yakit_harca(miktar: int, mevcut_yakit: int = 100) -> int:
        """Belirtilen miktarda yakıt harcar ve kalan yakıtı döner."""
        return mevcut_yakit - miktar