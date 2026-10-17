##Görev 4 - Önbellekli Rota Sayacı Performans Analizi

`galaksi.json` bağlantı grafiği üzerinden "dünya" başlangıç gezegeni ve `adim=20` değeri için yapılan süre karşılaştırması ve önbellek istatistikleri:

- **Hesaplanan Toplam Rota Sayısı**: 4315343
- **Önbelleksiz Süre (adim=20)**: 1.167203 saniye
- **Önbellekli Süre (adim=20)**: 0.000079 saniye
- **cache_info() Çıktısı**: `CacheInfo(hits=47, misses=51, maxsize=None, currsize=51)`

> `@lru_cache` kullanımı sayesinde tekrarlayan alt rota hesaplamaları önbellekten çekilmiş ve çalışma süresi yaklaşık 14.000 kat hızlanmıştır.