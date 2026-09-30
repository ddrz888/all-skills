# Príloha: Segmentové moduly AiOS

## Účel a postavenie prílohy

Táto príloha zhŕňa **osem navrhovaných odvetvových modulov**, ktoré môžu nasledovať až po validácii internej pracovnej aplikácie AiOS. Nejde o osem súbežných vývojov ani osem nezávislých technických základov. Jednotlivé moduly sa neskôr môžu predávať ako samostatné klientské riešenia. Ich funkciou je ukázať, ako sa môže overený spoločný základ prispôsobiť konkrétnemu pracovnému postupu bez toho, aby sa z neho stal univerzálny no-code nástroj. Vychádza zo spoločného zadania AiOS; podrobnosti predstavujú navrhovaný rozsah na overenie. [1]

Spoločným východiskom je pracovná aplikácia s identitou a oprávneniami, organizáciami a kontaktmi, pracovným prípadom, vlastníkmi a úlohami, súkromnými dokumentmi, návrhmi AI so zdrojmi, schvaľovaním, explicitným zdieľaním v portáli, auditnou stopou, meraním a exportom. Pre prvých externých klientov sa uvažuje oddelené nasadenie a databáza, nie improvizovaný zdieľaný multi-tenant model. Táto príloha nemení hlavný interný produktový plán; nezaoberá sa cenou, harmonogramom, dopytom trhu ani technickou implementáciou.

## Spoločné hranice bezpečnej prevádzky

Každý modul musí striktne oddeľovať interné poznámky od údajov viditeľných klientovi. Prístup sa viaže na identitu, rolu a prípad; portál zobrazí iba explicitne schválený obsah. Zdroje údajov, verzie, zmeny, schválenia, zdieľanie a export sa zapisujú do auditnej stopy. Pri citlivých prípadoch sa pred použitím AI vykoná ľudská kontrola údajov, zmluvných podmienok a retenčných pravidiel.

AI môže štruktúrovať dodané údaje, označovať medzery a navrhovať otázky alebo text. Každé tvrdenie musí mať dohľadateľný zdroj. Neznámy údaj zostáva **neznámy**: z fotografie sa nesmie vydávať presný rozmer, materiál, model, technická vlastnosť, diagnóza ani bezpečnostný záver. Rozpor alebo nečitateľný podklad je blokujúca neistota, nie podnet na domýšľanie.

V úvodných pilotoch sú externé správy návrhmi na kontrolu. Cena alebo jej zmena, prísľub termínu, potvrdenie rezervácie, zdieľanie citlivého súboru a citlivé rozhodnutie vyžadujú konkrétne ľudské schválenie. Po vyhodnotení testov možno samostatne povoliť úzko vymedzené automatické odpovede na bežné otázky podľa schválených pravidiel, najmä v module guest; nejde o všeobecné oprávnenie AI konať. Návrh slotu nie je potvrdená dostupnosť. Dostupnosť sa smie potvrdiť až po kontrole konfliktov a autoritatívneho zdroja; žiaden modul nepredstiera živé prepojenie, ak neexistuje. Právny modul neposkytuje autonómnu právnu radu, nevypočítava právne lehoty, nerozhoduje konfliktové otázky a nepredstavuje garanciu právneho súladu. Uvedené číselné prahy a lehoty KPI sú pracovné návrhy, nie dosiahnuté výsledky či záväzné SLA. Nulový incident v testovacej sade je podmienka prijatia, nie dôkaz nemožnosti budúcej chyby.

| ID | Modul | Prvý predajný výsledok | Nová doménová zložitosť |
|---|---|---|---|
| service | AiOS Servisný systém | Kompletná servisná karta a človekom schválený návrh termínu | Vozidlo, symptómy, bezpečnostná poznámka |
| realty | AiOS Realitný systém | Schválený shortlist a návrh obhliadky | Rozpočet, lokalita, kvalifikácia, obhliadka |
| guest | AiOS Systém pre hostí | Overené FAQ odpovede a odovzdanie výnimiek | Platnosť obsahu, výnimky, eskalácia majiteľovi |
| studio | AiOS Ateliér | Úplné zadanie, balík a návrh termínu | Foto-dopyt, balíky, predprodukčné inštrukcie |
| furniture | AiOS Nábytkový systém | Kompletné zadanie pre odborné posúdenie | Merania, väzba fotografií, montážne obmedzenia |
| visual | AiOS Vizuálny systém | Schválené projektové zadanie priestoru | Kontext priestoru, mierka, interiér/exteriér |
| restore | AiOS Renovačný systém | Renovačná karta pre odborné posúdenie | Patina, poškodenie, pôvod, logistický krok |
| legal | AiOS Právny systém | Bezpečný prvotný podnet a checklist podkladov | Matter-level prístup, strany, procesné dokumenty |

## 1. AiOS Servisný systém (`service`)

Modul pre autoservis premieňa prijatý dopyt na servisnú kartu pripravenú na odborné posúdenie. Povinné polia pokrývajú kontakt a organizáciu, značku, model a ročník vozidla, opis prejavov a času vzniku, zákazníkom uvedenú urgenciu, preferovaný kontakt a čas. EČV alebo VIN sú voliteľné a zapisujú sa len pri poskytnutí zákazníkom. Každý údaj nesie zdroj a čas; neznámy model alebo ročník sa nepokúša doplniť.

Tok začína zachytením dopytu v pracovnom prípade. AI navrhne doplňujúce otázky a normalizáciu len ako návrh. Pracovník opraví neistoty, vytvorí kartu a po overení proti autoritatívnemu zdroju môže schváliť návrh jedného či viacerých slotov. Pred odoslaním potvrdí údaje, interpretáciu závady, naliehavosť, cenu, termín i prípadné zdieľanie súborov. **Jadro** je spoločná karta, dokumenty, schvaľovanie a audit; **prírastok** tvorí karta vozidla, slovník značiek/modelov/ročníkov a šablóny symptómov.

Modul nestanovuje diagnózu ani bezpečnostné rozhodnutie a bez zdroja nepotvrdzuje cenu, dostupnosť alebo rezerváciu. Ak dopyt obsahuje nejasný model, rozporné termíny a nečitateľnú fotografiu, musí označiť neistoty, pripraviť otázku na objasnenie a zablokovať nepodložené potvrdenie termínu; doplňujúca komunikácia sa nezablokuje. KPI je miera úplných servisných kariet po prvom preskúmaní, medián času po schválený návrh termínu a počet neoprávnených potvrdení; cieľ posledného ukazovateľa je nula. Pilot vyžaduje reprezentatívne interné testy bez falošnej rezervácie alebo diagnózy, audit opráv a písomné prijatie postupu servisným tímom.

## 2. AiOS Realitný systém (`realty`)

Realitný modul pripravuje kvalifikovaný profil záujemcu, shortlist a návrh obhliadky bez tvrdenia o živej dostupnosti. Záznam obsahuje meno a kontakt, rozpočet s menou a toleranciou, lokalitu, typ nehnuteľnosti, minimálne požiadavky, časový horizont a zdroj dopytu. Financovanie sa doplní iba v potrebnom rozsahu; nejde o overovanie úveruschopnosti. Identita sa overí pri prístupe do portálu. Účel a pravidlá spracovania kontaktu sa stanovia v audite, nie automatickým vyžadovaním súhlasu na každý úkon.

Po prijatí sa označia chýbajúce polia. AI navrhne otázky a zhrnie odpovede so zdrojmi. Maklér schvaľuje profil, prioritu, shortlist, ceny a text správ. Následne systém pripraví kandidátne sloty; maklér pred schválením odoslania overí podmienky, konflikt a autoritatívnu dostupnosť. Po obhliadke sa uloží výsledok, ďalšia úloha a schválený portálový obsah. **Jadro** tvoria spoločné identity, karta, dokumenty, portál a audit; **prírastok** predstavuje profil preferencií, vysvetliteľné kvalifikačné skóre, triedenie ponúk a checklist obhliadky.

Nie je dovolená automatická kúpa, rezervácia, cenové vyjednávanie ani právne posúdenie. Pri neúplnom profile, rozpore rozpočet–ponuka alebo neoverenom slote vznikne úloha na objasnenie pre makléra, nie nepodložené potvrdenie obhliadky. KPI sleduje podiel dopytov kvalifikovaných do jedného pracovného dňa, čas po schválený shortlist, dokončené obhliadky a opravy návrhov podľa zdroja dopytu. Pilot predpokladá testovateľné oddelenie dát, úplné blokovanie neoverenej dostupnosti a akceptačný test maklérov.

## 3. AiOS Systém pre hostí (`guest`)

Tento modul nie je samostatný chatbot ani rezervačný systém. Prvým výsledkom sú odpovede na bežné otázky so schváleným zdrojom, dátumom kontroly, platnosťou a eskalačnou cestou. Pilot najprv pripravuje návrhy človeku; po overení môže automaticky vybavovať nízkorizikové FAQ o parkovaní, raňajkách a check-ine podľa vopred schválených pravidiel. Dostupnosť izieb sa bez aktuálneho zdroja neuvádza. Karta penziónu obsahuje zodpovedného majiteľa, schválený obsah každej témy, pravidlá, definíciu dostupnosti a jej zdroj, kontakt na výnimku, vlastníka a termín revízie.

Interný tím vloží zdrojovaný obsah a AI navrhne odpoveď len z aktuálne schváleného zdroja. Človek schvaľuje zdrojové fakty, pravidlá automatických odpovedí a ich platnosť; počas úvodného pilotu aj jednotlivé odpovede. Nejasná, výnimočná alebo konfliktná otázka sa zmení na úlohu majiteľovi. Pri rezervácii môže systém navrhnúť slot, avšak kontrola zdroja a potvrdenie zostávajú na človeku. **Jadro** je obsahovo riadená pracovná karta, prístupy, schvaľovanie a portál; **prírastok** zahŕňa štyri tematické šablóny, stavy koncept/schválená/expirovaná/pozastavená a pravidlá výnimiek.

Ak je dostupný iba interný obsah pravidiel a PMS nie je pripojený, systém nesmie tvrdiť dostupnosť ani odoslať potvrdenie. Musí uviesť, že dostupnosť nie je overená, vyžiadať preferovaný dátum a vytvoriť úlohu majiteľovi; nesmie vymyslieť voľný slot. KPI je podiel kvalifikovaných otázok v štyroch témach zodpovedaných z aktuálneho zdroja bez opravy po odoslaní; osobitne sa merajú eskalácie, expirovaný obsah a nepovolené tvrdenia. Pilot vyžaduje tento negatívny test, potvrdenie obsahu a retencie majiteľom a manuálne pozastavenie pri incidente.

## 4. AiOS Ateliér (`studio`)

Ateliér zjednocuje dopyt, voľbu balíka, inštrukcie a návrh termínu. Povinné polia zahŕňajú kontakt, účel fotenia, požadovaný výstup a rozsah, preferovaný dátum a flexibilitu, lokalitu alebo výjazd, balík, rekvizity a obmedzenia, referenčné podklady a nastavenie viditeľnosti súborov. Podmienky spracovania kontaktu sa určia podľa účelu.

Pracovný prípad deduplikuje kontakt a označí medzery. AI môže pripraviť otázky, zhrnutie a kandidátny balík, no pri fotografiách zapisuje neznáme rozmery alebo materiály ako neisté. Človek schváli rozsah, cenu a inštrukcie. Systém navrhne termín z dostupných overených podkladov alebo vyžiada preferenciu klienta; termín sa potvrdí až po kontrole konfliktu a autoritatívneho zdroja. **Jadro** pozostáva z verziovanej karty, súborov, portálu, schválení a exportu; **prírastok** je štruktúra foto-dopytu, katalóg balíkov a predprodukčný checklist.

Nie je tu live kalendár, platba, garantovaný termín ani automatický súhlas. Pri nejasných podkladoch, prekrývajúcom sa okne a následnej zmene klienta test vyžaduje označiť neznáme, odhaliť konflikt, zachovať starú verziu a zablokovať nepodložené potvrdenie termínu. KPI je týždenná miera úplnosti dopytov po prvom internom preskúmaní, čas po pripravený návrh a počet manuálnych opráv. Pilot môže nasledovať až po úspešnom end-to-end teste, funkčnom logu a schválení šablón a konfliktového postupu.

## 5. AiOS Nábytkový systém (`furniture`)

Nábytkový modul vytvára kompletizované stolárske zadanie pre odborné posúdenie, nie automatickú ponuku. Požaduje kontakt, oprávnené osoby na zdieľanie, typ a účel nábytku, fotografie v pôvodnej kvalite, rozmery s jednotkami a označením merané/odhadnuté, preferencie materiálu a povrchu, štýl, funkčné požiadavky, orientačný rozpočet, horizont a lokalitu s montážnymi obmedzeniami.

Systém založí kartu a priradí vlastníka. AI iba označí neistoty so zdrojom a navrhne otázky. Človek kontroluje fotografie, rozmery, materiál, štýl a rozpočet; až potom vytvorí internú úlohu na odborné posúdenie. Správa, cena, obhliadka alebo rezervácia zostávajú návrhom až do ľudského schválenia. **Jadro** je prípad, prístupy, súbory, audit a portál; **prírastok** je stolárska šablóna, kontrola úplnosti meraní, väzba fotografia–časť priestoru a fronta posúdenia.

AI nesmie z perspektívnej fotografie vyhlásiť presný rozmer, materiál ani realizovateľnosť. Negatívny test s odhadom rozmeru z fotografie musí ponechať hodnotu ako neoverenú, vyžiadať potvrdenie a zablokovať prechod na ponuku. KPI je miera kariet pripravených na odborné posúdenie bez dopĺňania, čas po schválenie a počet opráv neistôt. Pilot vyžaduje funkčné oddelenie poznámok, audit verzií, blokovanie ponuky a zdokumentovaný manuálny fallback.

## 6. AiOS Vizuálny systém (`visual`)

Vizuálny modul pripravuje schválené zadanie dekorácie interiéru alebo exteriéru. Záznam obsahuje typ, účel, lokalitu a fázu priestoru, želaný výsledok a štýl, fotografie alebo pôdorys s miestnosťou, perspektívou a dátumom, rozmery s jednotkami a spôsobom merania, materiály a údržbové obmedzenia, rozpočet, termín želania, kontakt, pravidlá jeho spracovania a prevádzkové riziká.

AI môže vytvoriť štruktúrovaný brief iba z dodaných podkladov. Človek označí položky ako potvrdené, odhadnuté alebo neznáme a uloží verziu. Klient môže v portáli explicitne schváliť zadanie alebo vrátiť pripomienky. Z briefu následne vznikajú interné úlohy; von ide len človekom schválená správa, cena alebo termín. **Jadro** sú identity, pracovný prípad, súbory, zdrojované návrhy, portál a audit; **prírastok** je priestorová šablóna, fotografický a pôdorysný checklist a rozlíšenie interiérových a exteriérových podmienok.

Modul nerobí statické, bezpečnostné ani realizačné posúdenie. Pri fotografii bez mierky a s nejasným povrchom musí obe hodnoty označiť ako neznáme, vyžiadať meranie alebo potvrdenie a zablokovať ich použitie v ponuke. KPI je podiel prípadov, ktoré do dvoch pracovných dní dosiahnu schválené zadanie bez viac než jednej spätnej výzvy; cieľ v pilote je aspoň 80 % a nula kritických porušení neistoty. Pred pilotom sa testuje desať po sebe idúcich interných zadaní a nulový neautorizovaný výstup.

## 7. AiOS Renovačný systém (`restore`)

Renovačný modul formuje auditovateľnú kartu pre reštaurátora. Obsahuje kontakt a pravidlá zdieľania podkladov, typ, približný vek alebo pôvod a počet kusov, fotografie celku, poškodenia, zadnej či spodnej časti a spojov, klientsky opis poškodenia, materiál alebo explicitné „Neznáme“, očakávaný výsledok a patinu, nezáväzný rozpočet, logistické obmedzenia a zdroj, dátum a stav každého údaja.

Klient dodá formulár a fotografie; systém zistí medzery. AI zhrnie iba dodané tvrdenia a vyznačí nejasnosti. Reštaurátor potvrdzuje identifikáciu, rozsah poškodenia, neznáme materiály, vhodnosť ďalšieho kroku a citlivé poznámky. Potom môže pripraviť návrh otázok, obhliadky, odovzdania alebo cenového podkladu; nič sa neodosiela automaticky. **Jadro** zahŕňa prístup na úrovni prípadu, kartu, verzie, dokumenty, portál a audit; **prírastok** tvorí štruktúra fotodokumentácie, taxonómia poškodenia a patiny, checklist originality a logistický návrh.

Fotografia, ktorá vyzerá ako masívne drevo, nesmie viesť k istému materiálu, diagnóze, cene ani potvrdenému termínu. Test vyžaduje stav „Neznáme“, ľudskú úlohu a blokovanie nepodloženého odborného záveru; návrh otázky zákazníkovi zostáva povolený. KPI je miera kariet pripravených na posúdenie bez opakovaného získavania základných údajov, medián času po tento stav a počet neautorizovaných odoslaní s cieľom nula. Pilot predpokladá desať anonymizovaných prípadov, aspoň 80 % pripravených kariet pri prvej kontrole a písomné prijatie postupu reštaurátorom.

## 8. AiOS Právny systém (`legal`)

Právny modul slúži len na bezpečný prvotný zber podnetu a dokumentácie pred odborným posúdením advokátom. Povinné polia zahŕňajú identitu, kontakt a preferovaný kanál, typ veci, klientsky opis skutkov a strán, klientom uvedené dátumy, lehoty a naliehavosť, dokumenty s pôvodom a čitateľnosťou, dôvernosť, obmedzenie prístupu a stav kontroly dát, zmluvných podmienok a retencie pred použitím AI.

Po overení odosielateľa dostane prípad vlastníka a matter-level prístup. Portál môže potvrdiť prijatie bez právneho záveru. Systém deduplikuje a chronologicky triedi súbory, označí ich typ a čitateľnosť a navrhne chýbajúce podklady s odkazom na zdroj. Poverený pracovník preverí citlivé či konfliktné položky, advokát schváli klasifikáciu, checklist, externú správu a prechod na odborné posúdenie. **Jadro** je bezpečná prípadová karta, dokumenty, explicitné zdieľanie, audit a schvaľovanie; **prírastok** predstavuje bezpečnostná trieda prípadu, právna intake taxonómia a oddelenie „klient uvádza“ od „advokát overil“.

Modul nevytvára právny záver, nevypočítava lehotu, nerobí konflikt clearance ani nerozhoduje o prijatí veci. Test s podobnými prípadmi a citlivým dokumentom vyžaduje stopercentné zablokovanie neoprávneného zobrazenia či vyhľadávania, nezamenenie strán a žiadne externé zdieľanie návrhu bez schválenia. KPI je podiel prípadov so schváleným checklistom a stavom pripravené na odborné posúdenie do jedného pracovného dňa bez incidentu. Platený pilot prichádza až po úspešnom teste matter-level prístupov, aspoň 95 % správne zachytených polí, úplnej blokácii neoprávneného prístupu a nulovom neschválenom externom odoslaní.

## Záver

Spoločná hodnota týchto návrhov je opakovateľný, auditovateľný prechod od neúplného dopytu k **človekom schválenému ďalšiemu kroku**. Rozdiel medzi modulmi neleží v sľuboch autonómie, ale v presne vymedzených poliach, slovníkoch, checklistoch a blokujúcich testoch danej práce. O zaradení ktoréhokoľvek modulu po internej validácii má rozhodovať preukázané zvládnutie jeho akceptačného testu, meranie uvedeného KPI a prijatie pracovného postupu zodpovedným človekom.

## Referencie

[1]: /home/ubuntu/aios-product-plan/brief.json "Spoločný brief AiOS — interné zadanie a odvetvové východiská"
