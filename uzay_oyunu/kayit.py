#görev2
def gorev_kaydi(baslik: str, *adimlar: str, oncelik: str = "normal" , **ekler: str) -> None:
    """Görev detaylarını ve ek bilgileri ekrana basar."""
    print(f"[{oncelik.upper()}] {baslik}")
    for i, adim in enumerate (adimlar, start=1):
        print(f"{i}. {adim}")
    for anahtar, deger in ekler.items() :
        print(f"{anahtar}: {deger}")

if __name__ == "__main__":
    #normal çağrı
    gorev_kaydi("Kara deliğe atla", "Kredi kazan", "Pilot bul", oncelik="YÜKSEK", sorumlu="Ayşe")

# * ve ** ile liste{sözlük açarak çağrı
    adim_listesi = ["Kredi kazan", "Pilotu bul", "Hiperdrive al"]
    ek_bilgiler = {"sorumlu": "Ayşe"}
    gorev_kaydi("Kara deliğe atla", *adim_listesi, oncelik="YÜKSEK", **ek_bilgiler)
