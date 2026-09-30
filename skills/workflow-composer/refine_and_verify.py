from pathlib import Path
import csv,json,re
root=Path('/home/ubuntu/aios-product-plan')
main=root/'PLAN-AIOS-CONTROL-ROOM.md'
s=main.read_text().replace('V repozitári budú postupne vzniknúť','V repozitári budú postupne vznikať')
main.write_text(s)
p=root/'SEGMENTOVE-MODULY-AIOS.md'
s=p.read_text()
s=s.replace('Nie sú to osem bezprostredných projektov, samostatné produkty ani záväzný plán implementácie.', 'Nejde o osem súbežných vývojov ani osem nezávislých technických základov. Jednotlivé moduly sa neskôr môžu predávať ako samostatné klientské riešenia.')
s=s.replace('Vychádza z spoločného zadania AiOS a z návrhov segmentov v tejto prílohe.[1]', 'Vychádza zo spoločného zadania AiOS; podrobnosti predstavujú navrhovaný rozsah na overenie. [1]')
s=s.replace('Externá správa, cena alebo jej zmena, prísľub termínu, potvrdenie rezervácie, zdieľanie citlivého súboru a citlivé rozhodnutie vyžadujú konkrétne ľudské schválenie.', 'V úvodných pilotoch sú externé správy návrhmi na kontrolu. Cena alebo jej zmena, prísľub termínu, potvrdenie rezervácie, zdieľanie citlivého súboru a citlivé rozhodnutie vyžadujú konkrétne ľudské schválenie. Po vyhodnotení testov možno samostatne povoliť úzko vymedzené automatické odpovede na bežné otázky podľa schválených pravidiel, najmä v module guest; nejde o všeobecné oprávnenie AI konať.')
s=s.replace('Moduly neposkytujú právnu radu, nevypočítavajú právne lehoty, nerozhodujú konfliktové otázky a netvrdia právny súlad.', 'Právny modul neposkytuje autonómnu právnu radu, nevypočítava právne lehoty, nerozhoduje konfliktové otázky a nepredstavuje garanciu právneho súladu. Uvedené číselné prahy a lehoty KPI sú pracovné návrhy, nie dosiahnuté výsledky či záväzné SLA. Nulový incident v testovacej sade je podmienka prijatia, nie dôkaz nemožnosti budúcej chyby.')
s=s.replace('Schválený balík odpovedí pre hostí', 'Overené FAQ odpovede a odovzdanie výnimiek')
s=s.replace('musí označiť neistoty, vyžiadať objasnenie a zablokovať správu aj rezerváciu.', 'musí označiť neistoty, pripraviť otázku na objasnenie a zablokovať nepodložené potvrdenie termínu; doplňujúca komunikácia sa nezablokuje.')
s=s.replace('Záznam obsahuje overenú identitu a kontaktné oprávnenie, rozpočet vrátane meny, zdrojov financovania a tolerancie, lokalitu a prípustný rozsah, typ a účel, minimálne požiadavky, časový horizont, zdroj dopytu, súhlas s kontaktovaním a oddelené interné poznámky.', 'Záznam obsahuje meno a kontakt, rozpočet s menou a toleranciou, lokalitu, typ nehnuteľnosti, minimálne požiadavky, časový horizont a zdroj dopytu. Financovanie sa doplní iba v potrebnom rozsahu; nejde o overovanie úveruschopnosti. Identita sa overí pri prístupe do portálu. Účel a pravidlá spracovania kontaktu sa stanovia v audite, nie automatickým vyžadovaním súhlasu na každý úkon.')
s=s.replace('vznikne blokujúca úloha pre makléra, nie správa alebo potvrdenie obhliadky.', 'vznikne úloha na objasnenie pre makléra, nie nepodložené potvrdenie obhliadky.')
s=s.replace('Prvým výsledkom je schválený balík odpovedí na parkovanie, raňajky, check-in a dostupnosť so zdrojom, dátumom kontroly, platnosťou a eskalačnou cestou.', 'Prvým výsledkom sú odpovede na bežné otázky so schváleným zdrojom, dátumom kontroly, platnosťou a eskalačnou cestou. Pilot najprv pripravuje návrhy človeku; po overení môže automaticky vybavovať nízkorizikové FAQ o parkovaní, raňajkách a check-ine podľa vopred schválených pravidiel. Dostupnosť izieb sa bez aktuálneho zdroja neuvádza.')
s=s.replace('Človek kontroluje faktickosť, rozsah zdieľania a platnosť pred publikovaním.', 'Človek schvaľuje zdrojové fakty, pravidlá automatických odpovedí a ich platnosť; počas úvodného pilotu aj jednotlivé odpovede.')
s=s.replace('Musí uviesť neznáme, navrhnúť len slot a vytvoriť úlohu majiteľovi.', 'Musí uviesť, že dostupnosť nie je overená, vyžiadať preferovaný dátum a vytvoriť úlohu majiteľovi; nesmie vymyslieť voľný slot.')
s=s.replace('referenčné podklady a súhlas s kontaktovaním a viditeľnosťou súborov.', 'referenčné podklady a nastavenie viditeľnosti súborov. Podmienky spracovania kontaktu sa určia podľa účelu.')
s=s.replace('Systém navrhne najvhodnejší slot;', 'Systém navrhne termín z dostupných overených podkladov alebo vyžiada preferenciu klienta;')
s=s.replace('identitu, súhlas so zdieľaním, typ a účel nábytku', 'kontakt, oprávnené osoby na zdieľanie, typ a účel nábytku')
s=s.replace('kontaktný súhlas a prevádzkové riziká.', 'kontakt, pravidlá jeho spracovania a prevádzkové riziká.')
s=s.replace('identitu a súhlas klienta, typ, približný vek', 'kontakt a pravidlá zdieľania podkladov, typ, približný vek')
s=s.replace('Pri nejasnej fotografii, prekrývajúcom sa okne a následnej zmene klienta test vyžaduje označiť neznáme, odhaliť konflikt, zachovať starú verziu a zablokovať externé odoslanie.', 'Pri nejasných podkladoch, prekrývajúcom sa okne a následnej zmene klienta test vyžaduje označiť neznáme, odhaliť konflikt, zachovať starú verziu a zablokovať nepodložené potvrdenie termínu.')
s=s.replace('Test vyžaduje stav „Neznáme“, ľudskú úlohu a blokovanie externého výstupu.', 'Test vyžaduje stav „Neznáme“, ľudskú úlohu a blokovanie nepodloženého odborného záveru; návrh otázky zákazníkovi zostáva povolený.')
s=s.replace('a žiadny návrh bez schválenia.', 'a žiadne externé zdieľanie návrhu bez schválenia.')
s=s.replace('file:///home/ubuntu/', '/home/ubuntu/')
p.write_text(s)
with (root/'BACKLOG-AIOS-CONTROL-ROOM.csv').open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
calc=json.loads((root/'evidence/planning-calculations.json').read_text())
assert len(rows)==31
assert sum(int(r['Zaklad_hodin']) for r in rows)==200
assert calc['total_hours']==250
ids={r['ID'] for r in rows}
assert all(not r['Zavislosti'] or r['Zavislosti'] in ids for r in rows)
for name in ['PLAN-AIOS-CONTROL-ROOM.md','SEGMENTOVE-MODULY-AIOS.md']:
    text=(root/name).read_text()
    assert len(re.findall(r'^# ',text,re.M))==1
    assert text.count('```')%2==0
    defined=set(re.findall(r'^\[(\d+)\]:',text,re.M))
    used=set(re.findall(r'\[(\d+)\](?!:)',text))
    assert not used-defined,(name,used-defined)
    print(name,'words',len(text.split()),'bytes',(root/name).stat().st_size)
    for url in re.findall(r'^\[\d+\]: (/[^ ]+)',text,re.M):
        assert Path(url).exists(),url
assert all(f'`{seg}`' in p.read_text() for seg in ['service','realty','guest','studio','furniture','visual','restore','legal'])
report={'verified':True,'files':[str(root/n) for n in ['PLAN-AIOS-CONTROL-ROOM.md','SEGMENTOVE-MODULY-AIOS.md','BACKLOG-AIOS-CONTROL-ROOM.csv']],'tasks':len(rows),'base_hours':200,'total_hours':250,'all_in_prices':[pkg['full_project_including_audit_blueprint'] for pkg in calc['packages'][2:]]}
(root/'evidence/validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
diagram=re.search(r'```mermaid\n(.*?)\n```',main.read_text(),re.S).group(1)
(root/'evidence/customer-flow.mmd').write_text(diagram+'\n')
