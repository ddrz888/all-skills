from pathlib import Path

path = Path('/home/ubuntu/RAVID_AI_30_dnovy_launch_playbook.md')
text = path.read_text()
marker = '\n## 19. Strategický záver\n'
insert = r'''
## 18.1 B2B akvizičný engine: Sell by Chat

AI infraštruktúra sa nepredá tým, že klientovi pošleme odkaz na web. Najprv treba otvoriť relevantnú konverzáciu, pochopiť súčasný stav a až potom ukázať budúce pracovné rozhranie.

Akvizičný engine RAVID AI má dve odlišné roly:

| Rola | Úloha | Výsledok |
|---|---|---|
| Opener | Otvorí prirodzenú konverzáciu a odhalí rozdiel medzi dnešným a želaným stavom | kvalifikovaný záujem |
| Closer | Prehĺbi problém, spojí ho s KPI a ponúkne audit alebo blueprint | diagnostický hovor alebo platený audit |

### A. Zdroje príležitostí

Kontakty sa vyhľadávajú v Google Mapách, na webových stránkach, Instagrame, LinkedIne, v lokálnych podnikateľských zoznamoch, členských zoznamoch asociácií a verejných katalógoch. Každý kontakt musí mať konkrétny dôvod oslovenia. RAVID AI nemá posielať masové správy bez kontextu.

Minimálne údaje v pipeline:

- názov firmy,
- segment,
- mesto alebo región,
- meno rozhodovateľa,
- web a hlavný komunikačný kanál,
- pozorovaný signál alebo problém,
- dátum prvého kontaktu,
- stav konverzácie,
- ďalší krok,
- poznámka o GDPR a oprávnenom obchodnom kontakte.

### B. Metóda A-B

**Stav A** opisuje, ako klient proces rieši dnes.  
**Stav B** opisuje, čo by chcel dosiahnuť.

Opener sa nepýta: „Chcete automatizáciu?“ Pýta sa:

> „Ako u vás dnes spracovávate dopyty z webu a sociálnych sietí? Chodí to všetko na majiteľa, alebo to rieši prijímací technik?“

Následná otázka:

> „Koľko ďalších zákaziek by ste vedeli prijať, ak by tím nemusel denne ručne dopĺňať neúplné správy a naháňať chýbajúce údaje?“

Čísla, napríklad percento stratených dopytov alebo počet ušetrených hodín, sa nesmú tvrdiť bez klientových dát. Majú byť predmetom auditu a baseline merania.

### C. Úloha Openera

Opener má vyvolať mikro-interakciu, nie uzatvoriť zákazku. Jeho pracovný postup:

1. nájsť konkrétny signál,
2. položiť jednu ľahko zodpovedateľnú otázku,
3. zistiť, ako firma proces rieši dnes,
4. zaznamenať odpoveď,
5. odovzdať kontakt Closerovi iba vtedy, keď existuje relevantný problém alebo záujem.

### D. Úloha Closera

Closer preberie konverzáciu a zistí:

- koľko dopytov firma prijíma,
- cez aké kanály prichádzajú,
- kto ich spracúva,
- kde sa strácajú údaje alebo čas,
- aké KPI chce firma zlepšiť,
- čo musí zostať pod kontrolou človeka,
- aké nástroje už firma používa,
- kto rozhoduje a aký je vhodný termín.

Closer nepredáva n8n, Make ani chatbot. Ponúka **Infrastructure Audit** alebo **AI OS Blueprint** s vizuálnym návrhom pracovného rozhrania.

---

## 18.2 Copy-paste akvizičné skripty

Skripty sú východiskové šablóny. Každá správa sa musí upraviť podľa konkrétnej firmy a verejne viditeľného signálu.

### A. Autoservisy: ServiceOS

**Prvý kontakt:**

> Dobrý deň, [meno]. Všimol som si, že máte [konkrétne hodnotenie/službu/aktivitu] v [mesto]. Chcel som sa spýtať jednu krátku vec: spracúvate dopyty a objednávanie termínov cez správy a e-maily Vy osobne, alebo to rieši prijímací technik?

**Kvalifikačná nadväznosť:**

> Pýtam sa preto, lebo v servisoch sa často opakujú otázky na značku, model, ročník, problém, fotografie a VIN. Keď tieto údaje chýbajú, pracovník musí dopyt viackrát doháňať. Je to u vás podobné, alebo vám chodia dopyty väčšinou kompletné?

**Prechod na audit:**

> RAVID AI vám nechce predávať ďalší chatbot. Navrhujeme pre autoservisy pracovné rozhranie ServiceOS, kde tím vidí dopyt, chýbajúce údaje, návrh ďalšieho kroku a schvaľuje odpoveď. Môžeme si dať 20-minútový Infrastructure Audit a zistiť, či by to vo vašom servise malo návratnosť?

### B. Renovácie nábytku: RestoreOS

> Dobrý deň, [meno]. Pri renováciách zákazníci často pošlú fotografiu bez rozmerov, typu materiálu alebo predstavy o rozsahu práce. Ako dnes získavate údaje potrebné na predbežné posúdenie zákazky?

> RAVID AI navrhuje RestoreOS: zákazník dostane správne otázky, vy vidíte kompletný dopyt a konečné odborné posúdenie zostáva vždy u vás. Má zmysel ukázať vám jednoduchý návrh obrazovky?

### C. Penzióny: GuestOS

> Dobrý deň, [meno]. Ako dnes riešite opakované otázky hostí na parkovanie, príchod, raňajky, izby a voľné termíny? RAVID AI buduje GuestOS, ktorý spojí overené informácie, dopyty, úlohy a prehľad pre majiteľa do jedného pracovného rozhrania. Môžeme si overiť, či by vám to znížilo manuálnu komunikáciu bez zmeny rezervačného systému?

### D. Reality: RealtyOS

> Dobrý deň, [meno]. Pri realitných dopytoch často rozhoduje rýchlosť reakcie a kvalita follow-upu. Ako dnes viete, ktorým leadom sa má maklér venovať ako prvým? RAVID AI navrhuje RealtyOS, ktorý spojí dopyty, nehnuteľnosti, ďalší krok a KPI konverzie do jedného pracovného panela. Môžeme vám ukázať návrh na 20-minútovom audite?

### E. Právne kancelárie: LegalDesk

> Dobrý deň, [meno]. RAVID AI pomáha právnym kanceláriám zjednodušiť administratívny príjem nových dopytov, triedenie dokumentov a interné úlohy. Nejde o automatické právne rady. Ide o pracovné rozhranie, ktoré pripraví podklady na kontrolu právnikom. Máte dnes proces, ktorý by sa dal bezpečne zjednotiť?

### F. Nábytok, fotoateliéry a dekorácie

Pre tieto segmenty sa používa rovnaká štruktúra:

1. odkaz na konkrétny produkt, realizáciu alebo službu,
2. otázka na dnešný spôsob spracovania dopytu,
3. otázka na chýbajúce údaje, termíny alebo follow-up,
4. predstavenie segmentového AI OS,
5. pozvanie na Infrastructure Audit.

Príklad pre nábytok:

> Ako dnes spracúvate otázky zákazníkov na rozmery, materiály, dostupnosť a dopravu? RAVID AI FurnitureOS by spojil katalóg, dopyty, návrh odpovede a follow-up do jedného panela. Nechceme meniť váš obchodný proces naslepo. Najprv ho zmapujeme a ukážeme vám prototyp.

---

## 18.3 Objection Handling SOP

Námietku netreba pretláčať. Treba ju pochopiť, potvrdiť a preformulovať cez konkrétny rozsah a bezpečný ďalší krok.

| Námietka | Skrytá obava | Odpoveď RAVID AI |
|---|---|---|
| „Nemáme čas na nový systém.“ | Tím čaká ďalšia komplikovaná práca. | „Rozumiem. Preto nezačíname veľkou platformou. Navrhneme jeden pracovný panel pre jeden proces, zaškolenie a testovanie. Najprv vám ukážeme obrazovku, až potom sa rozhodnete.“ |
| „Máme Excel, WhatsApp a e-mail.“ | Súčasný spôsob je pohodlný a známy. | „To je v poriadku. RAVID AI ich nemusí hneď nahradiť. Pridá nad ne prehľad, ktorý ukáže, čo prišlo, čo chýba a kto má urobiť ďalší krok.“ |
| „AI nám nevypočíta presnú cenu.“ | Obava zo straty odbornej kontroly. | „Presne. A ani to nesľubujeme. AI zozbiera podklady a pripraví návrh. Konečnú cenu a odborné rozhodnutie schvaľujete Vy.“ |
| „Nechceme chatbot.“ | Klient si spája AI s neosobným robotom. | „Ani my nechceme začínať chatbotom. Začíname pracovným rozhraním pre váš tím. Zákaznícka komunikácia je iba jedna možná vrstva.“ |
| „AI nám môže poškodiť reputáciu.“ | Strach z nesprávnej odpovede. | „Preto je v návrhu schválenie človekom, znalostná báza, obmedzený rozsah odpovedí a manuálny režim. Najprv testujeme na interných alebo kontrolovaných prípadoch.“ |
| „Nevieme, či sa nám to vráti.“ | Nejasná hodnota a riziko investície. | „Preto začíname KPI a baseline. Pred buildom si dohodneme, čo meriame: čas odpovede, počet termínov, hodiny alebo konverziu. Bez merania pilot neškálujeme.“ |
| „Je to drahé.“ | Klient porovnáva riešenie s lacným skriptom. | „Je to iný typ produktu než jednorazová automatizácia. Ak audit ukáže malú hodnotu, odporučíme menší zásah alebo nezačneme. Najprv musí sedieť ekonomika.“ |

---

## 18.4 Outbound SOP na prvých 30 dní

### Denný objem

| Aktivita | Denné minimum |
|---|---:|
| Nové kvalifikované firmy | 10 |
| Personalizované prvé kontakty | 10 |
| Follow-up správy | 5 |
| Kvalifikačné rozhovory | 1 |
| Aktualizácia pipeline | 1 blok |
| Obsah alebo ukážka infraštruktúry | 1 krátky výstup |

### Týždenné ciele

- 50 nových kvalifikovaných firiem,
- 50 personalizovaných prvých kontaktov,
- 25 follow-upov,
- 3–5 kvalifikačných rozhovorov,
- 2–3 Infrastructure Audity,
- 1–2 ponuky na platený audit alebo blueprint.

Tieto čísla sú pracovné ciele, nie garancia. RAVID AI ich má po prvom týždni upraviť podľa kvality segmentu a kapacity.

### Pipeline fázy

1. Identifikovaný kontakt.
2. Prvý kontakt odoslaný.
3. Odpoveď prijatá.
4. Problém potvrdený.
5. Kvalifikačný rozhovor.
6. Audit naplánovaný.
7. Audit uskutočnený.
8. Blueprint ponúknutý.
9. Pilot schválený.
10. Zákazka odovzdaná.
11. Infrastructure Care ponúknutý.

### Pravidlo follow-upu

Follow-up má priniesť nový kontext, nie iba „pripomínam sa“.

- **Po 2–3 dňoch:** doplniť konkrétnu otázku k procesu.
- **Po 5–7 dňoch:** poslať krátky príklad obrazovky alebo KPI.
- **Po 10–14 dňoch:** uzavrieť slučku a ponechať možnosť návratu.

Posledná správa:

> „Dobrý deň, [meno]. Uzavriem to z mojej strany, aby som vás nerušil. Ak budete niekedy riešiť, ako zjednotiť dopyty, podklady a follow-up bez výmeny celého systému, rád vám ukážem náš Infrastructure Audit. Prajem úspešný týždeň.“

### Akvizičný dashboard

| KPI | Cieľ | Skutočnosť | Poznámka |
|---|---:|---:|---|
| Nové firmy | 50/týždeň |  |  |
| Prvé kontakty | 50/týždeň |  |  |
| Odpovede | podľa baseline |  |  |
| Kvalifikované rozhovory | 3–5/týždeň |  |  |
| Audity | 2–3/týždeň |  |  |
| Ponuky | 1–2/týždeň |  |  |
| Predaje | podľa fázy |  |  |
| Priemerná hodnota | podľa produktu |  |  |

Nevyhodnocuj iba počet odpovedí. Sleduj kvalitu kontaktov, podiel rozhovorov, počet auditov, konverziu auditu na blueprint alebo pilot a čas zakladateľa potrebný na delivery.

---

'''
if marker not in text:
    raise SystemExit('Marker not found')
text = text.replace(marker, '\n' + insert + marker, 1)
path.write_text(text)
print(f'Updated {path} with acquisition engine sections')
print(f'Lines: {len(text.splitlines())}')
