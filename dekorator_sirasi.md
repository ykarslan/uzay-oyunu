# Gorev 2 - Cagri Sayaci ve Dekorator Sirasi Analizi

- **Yalnizca @say (21891):** Onbellek yoktur; dallardaki tum alt problemler bastan sona tekrar hesaplanir.
- **@say ustte, @lru_cache altta (39):** Ozyinelemeli cagrilar distaki @say katmanina her carptiginda sayac artar, ardindan @lru_cache sonucu onbellekten dondurerek dallanmayi durdurur.
- **@lru_cache ustte, @say altta (21):** Onbellekte olan cagrilar dogrudan en dis katmandan doner; icteki @say katmanina yalnizca onbellekte olmayan benzersiz 21 deger (0'dan 20'ye) icin girilir.
