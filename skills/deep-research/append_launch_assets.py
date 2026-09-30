from pathlib import Path

path = Path('/home/ubuntu/RAVID_AI_30_dnovy_launch_playbook.md')
text = path.read_text()
marker = '\n## 19. Strategický záver\n'
insert = r'''
## 18.5 Launch asset checklist: čo musí existovať pred prvým predajom

Stratégia je pripravená až vtedy, keď sa dá vykonať bez ďalšieho vymýšľania. Pred prvým oslovením musí mať RAVID AI pripravených päť hmatateľných podkladov a jednu dennú rutinu.

### 1. Akvizičná databáza 30–50 firiem

Na prvú kampaň sa vyberie jeden primárny segment. Odporúčanie je začať autoservisami alebo renovátormi nábytku, nie všetkými segmentmi naraz.

| Pole | Obsah |
|---|---|
| Názov firmy | oficiálny názov |
| Segment | autoservis, renovácie, penzión a podobne |
| Mesto/región | geografická relevancia |
| Web | verejná stránka |
| Hlavný kanál | e-mail, telefón, Instagram, Facebook alebo LinkedIn |
| Rozhodovateľ | majiteľ, manažér alebo prijímací technik |
| Pozorovaný signál | konkrétny dôvod oslovenia |
| Pravdepodobný problém | dopyty, termíny, ponuky, obsah alebo follow-up |
| Prvý kontakt | dátum a kanál |
| Stav | nový, oslovený, odpovedal, hovor, audit, ponuka, vyhraný, stratený |
| Ďalší krok | presná akcia a dátum |
| Poznámka | relevantný kontext, nie citlivé osobné údaje |

**Pravidlo kvality:** každý kontakt musí mať jednu personalizačnú poznámku. Nekupovať veľký zoznam a neposielať neosobný spam. Pri e-mailovej a telefonickej komunikácii treba dodržať príslušné pravidlá ochrany osobných údajov a elektronickej komunikácie.

### 2. Vizuálny prototyp jednej obrazovky

Pred prvým buildom stačí jeden klikateľný alebo statický prototyp. Nemusí byť napojený na reálne dáta. Musí však ukázať, ako klient pracuje.

**Minimálny prototyp pre ServiceOS:**

1. horný panel s KPI: nové dopyty, čakajúce schválenia, dohodnuté termíny,
2. hlavná karta dopytu: meno, vozidlo, problém, fotografie, VIN alebo chýbajúce údaje,
3. karta „AI pripravilo“: sumarizácia a návrh ďalšieho kroku,
4. tlačidlá: **Schváliť odpoveď**, **Vyžiadať údaje**, **Priradiť technikovi**, **Odoslať na manuálne riešenie**,
5. stav zákazky: nový dopyt, čaká na údaje, pripravené na termín, schválené, uzatvorené,
6. poznámka o tom, že konečné odborné rozhodnutie robí človek.

Prototyp má klientovi umožniť povedať: „Áno, toto by môj tím vedel používať.“ Nemá predstierať, že produkčný systém je hotový za niekoľko minút.

### 3. Infrastructure Audit: 10 diagnostických otázok

Tieto otázky sa použijú počas 20-minútového rozhovoru. Odpovede sa zapisujú do auditnej karty.

1. Aký výsledok chcete zlepšiť v najbližších 90 dňoch?
2. Odkiaľ dnes prichádzajú dopyty a požiadavky?
3. Kto ich prijíma, triedi a prideľuje?
4. Ktoré informácie musíte od zákazníka opakovane doháňať?
5. Kde dnes vzniká najväčšie zdržanie alebo strata?
6. Koľko dopytov alebo prípadov riešite za týždeň?
7. Koľko času denne alebo týždenne zaberá tento proces?
8. Aké nástroje, tabuľky, kalendáre, CRM alebo úložiská už používate?
9. Čo môže AI pripraviť a čo musí vždy schváliť človek?
10. Podľa čoho o 30 dní spoznáme, že pilot funguje?

**Doplňujúce otázky podľa segmentu:**

- Autoservis: značka, model, ročník, VIN, fotografie, typ problému a požadovaný termín.
- Renovácie nábytku: typ kusu, rozmery, materiál, poškodenie, fotografie a očakávaný výsledok.
- Penzión: termín, počet hostí, typ izby, dostupnosť, pravidlá a spôsob potvrdenia.
- Reality: lokalita, rozpočet, typ nehnuteľnosti, časový horizont a stav leadu.
- Právnici: oblasť prípadu, dokumenty, termíny a oprávnenie na prístup k údajom.
- Nábytok: produkt, rozmery, materiál, dostupnosť, doprava a rozpočet.
- Fotoateliér: typ fotenia, termín, balík, počet osôb a výstup.
- Dekorácie: priestor, rozmery, štýl, materiál, rozpočet a fotografie.

### 4. Jednostranová ponuka na Audit a Blueprint

#### RAVID AI Infrastructure Audit

**Pre koho:** [segment a typ firmy]  
**Problém:** [konkrétny proces, ktorý spôsobuje stratu času, dopytov alebo prehľadu]  
**Cieľ auditu:** zmapovať tok dopytov, dát, rozhodnutí a zodpovedností a vybrať prvý AI OS modul s merateľným KPI.

**Výstup:**

- 60–90-minútový rozhovor alebo dva kratšie rozhovory,
- mapa súčasného procesu,
- mapa dát a nástrojov,
- tri prioritné príležitosti,
- odporúčané KPI a baseline,
- návrh prvej obrazovky,
- rozsah a riziká pilotu,
- odporúčanie: pokračovať, zúžiť rozsah alebo nezačínať.

**Trvanie:** 2–5 pracovných dní.  
**Cena:** 250–750 € podľa rozsahu.  
**Čo audit nezahŕňa:** produkčné napojenie, rozsiahly vývoj ani automatické rozhodovanie v mene klienta.

#### RAVID AI OS Blueprint

**Cieľ:** premeniť audit na zrozumiteľný návrh systému, ktorý klient schváli pred implementáciou.

**Výstup:**

- návrh obrazoviek a používateľských rolí,
- cieľový tok dát,
- návrh AI funkcií a ľudského schválenia,
- integračný návrh,
- bezpečnostné a fallback pravidlá,
- testovací plán,
- rozsah prvého pilota,
- harmonogram a rozpočet.

**Trvanie:** 1–2 týždne.  
**Cena:** 750–2 500 €.  
**Garancia:** RAVID AI garantuje dodanie dohodnutého výstupu v dohodnutom termíne. Negarantuje obchodný výsledok bez baseline, spolupráce klienta a reálneho používania tímom.

### 5. Objednávkový rámec

Každá objednávka auditu alebo blueprintu musí obsahovať:

- názov a cieľ projektu,
- presný rozsah,
- výstupy,
- počet stretnutí a revízií,
- povinnosti klienta,
- prístupy a údaje potrebné na prácu,
- cenu, splatnosť a termín,
- čo je mimo rozsahu,
- pravidlá nakladania s dátami,
- spôsob akceptácie výstupu,
- podmienky pokračovania do pilota,
- spôsob ukončenia.

Pri prvých klientskych projektoch sa odporúča vyhnúť nejasnej formulácii „AI systém podľa potreby“. Rozsah má byť definovaný obrazovkami, procesmi, dátami, KPI a konkrétnymi odovzdávacími bodmi.

### 6. Founder OS

Zakladateľský čas sa v prvých 30 dňoch rozdelí medzi tri piliere. Rozdelenie 1/3–1/3–1/3 je východiskový rámec, nie dogma. Počas prvého predaja môže mať Business Model väčší podiel.

| Pilier | Hlavné aktivity | Denný výstup |
|---|---|---|
| Business Model | research firiem, outreach, follow-up, rozhovory, ponuky | nové kontakty, rozhovor alebo ponuka |
| Personal Brand | ukážky prototypov, vysvetlenie AI infraštruktúry, príbehy z auditov | jeden užitočný verejný alebo poloverejný výstup |
| Deep Work | blueprint, prototyp, dátový tok, SOP, delivery | dokončená časť systému alebo podkladu |

**Denný blok:**

- 90–120 minút Business Model,
- 30–60 minút Personal Brand,
- 120–180 minút Deep Work,
- 15 minút aktualizácia pipeline a lessons learned.

### 7. Launch gate: podmienky na odoslanie prvej kampane

Kampaň je pripravená, ak existuje:

- jeden primárny segment,
- jeden problém a jedno hlavné KPI,
- zoznam minimálne 30 firiem,
- 10 personalizovaných prvých správ,
- jeden vizuálny prototyp,
- 10 auditných otázok,
- jednostranová ponuka na Audit alebo Blueprint,
- pipeline s dátumom ďalšieho kroku,
- pripravená odpoveď na päť najčastejších námietok.

Ak niektorý z týchto bodov chýba, RAVID AI nemá ďalší týždeň plánovať. Má ho doplniť v ten istý deň.

'''
if marker not in text:
    raise SystemExit('Marker not found')
text = text.replace(marker, '\n' + insert + marker, 1)
path.write_text(text)
print(f'Updated {path}')
print(f'Lines: {len(text.splitlines())}')
