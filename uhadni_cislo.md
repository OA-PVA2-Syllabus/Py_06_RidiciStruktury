# PVA2 - Programování a vývoj aplikací
## Cvičení 06: Řídící struktury - Pokročilé

## Uhádni číslo
Naprogramujte jednoduchou aplikaci, která umožní uživateli hádat tajné číslo. Program bude využívat cyklus s podmínkami a nabídne několik možností, jak pokračovat podle vstupu uživatele. Tento příklad pomůže procvičit práci s cykly, podmínkami a vstupy od uživatele.

1. **Tajné číslo**: Program si náhodně vygeneruje tajné číslo v rozsahu 1 až 100.
2. **Hádaní čísla**:
   - Uživatel má celkem **10 pokusů** k uhádnutí čísla.
   - Po každém pokusu program řekne uživateli, zda je jeho odhad **příliš vysoký**, **příliš nízký**, nebo **správný**.
3. **Možnosti po každém pokusu**:
   - Pokud je hádání špatné, program odečte jeden pokus a nabídne možnost pokračovat v hádání.
   - Uživatel může kdykoli zadat příkaz „stop“, aby ukončil program, nebo se může rozhodnout pokračovat až do vyčerpání pokusů.
4. **Vyhodnocení**:
   - Pokud uživatel uhodne tajné číslo, program ukončí cyklus a zobrazí zprávu o výhře.
   - Pokud uživatel neuhodne během 10 pokusů, zobrazí zprávu o prohře a prozradí tajné číslo.
5. **Nápověda**: Po třech špatných pokusech nabídněte uživateli nápovědu, zda je číslo sudé nebo liché.
6. **Rozšíření**: Po ukončení programu nabídněte možnost začít novou hru nebo ukončit aplikaci.
7. **Rozšíření**: Zapracujte do programu listinu nejlepších pokusů. Do seznamu uložte jméno hráče a počet pokusů. Výsledkovou listinu zobrazte uživateli.

## Příklad průběhu programu
Vítejte ve hře "Hádání čísla"! Mám tajné číslo mezi 1 a 100. Máte 10 pokusů uhodnout.

Zadejte svůj odhad: 50 Příliš nízké! Zbývá 9 pokusů.

Zadejte svůj odhad: 75 Příliš vysoké! Zbývá 8 pokusů.

Zadejte svůj odhad: 63 Gratulujeme! Uhodl/a jste správné číslo 63!


## Tipy
- Použijte `while` nebo `for` cyklus pro počítání pokusů.
- Využijte podmínky `if`, `elif` a `else` pro vyhodnocení odhadu a kontroly příkazů uživatele.
- Nezapomeňte ošetřit vstupy od uživatele, aby program nezhavaroval při nesprávném zadání.

