#görev1 devamı
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