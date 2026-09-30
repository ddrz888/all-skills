from pathlib import Path
import csv, json, math

root=Path('/home/ubuntu/aios-product-plan')
phases=[
 ('P0','Zadanie a hranice',[
  ('Potvrdiť pracovný proces a mimo-rozsah',4,'Spísaný vstup, vlastník, stavy, výstup a zoznam funkcií mimo v1.'),
  ('Pripraviť tri fiktívne firmy a scenáre',4,'Dva oddelené klientske účty a interná firma; žiadne produkčné osobné údaje.'),
  ('Schváliť obrazovky a akceptačné kritériá',4,'Klikateľný návrh hlavnej cesty; potvrdené rozhodnutie o stacku a prevádzke.')]),
 ('P1','Základ a oprávnenia',[
  ('Založiť privátny repozitár a prostredia',6,'Oddelený vývoj, test a produkcia; kontrola typov a automatické testy pri zmene.'),
  ('Prihlásenie, pozvánky a obnova prístupu',6,'Exspirujúca pozvánka; možnosť odobrať prístup; MFA správcu pred ostrou prevádzkou.'),
  ('Dátový model a serverové oprávnenia',6,'workspace_id odlíšené od customer_org_id; všetky operácie overujú rolu a vlastníctvo.'),
  ('Negatívne testy prístupov',6,'Klient A nedokáže čítať ani meniť kartu, súbor, export alebo AI kontext klienta B.')]),
 ('P2','Dopyty a CRM',[
  ('Register organizácií a kontaktov',8,'Vyhľadávanie, vlastník, poznámky; návrh duplicít nepresúva ani nespája dáta bez schválenia.'),
  ('Karta dopytu a povolené zmeny stavu',8,'Každý otvorený dopyt má vlastníka, ďalší krok a dátum; prechod sa overí na serveri.'),
  ('Ručný vstup a verejný formulár',6,'Serverové overenie vstupu a e-mailu, obmedzenie frekvencie, bezpečný zápis bez odhalenia údajov.'),
  ('Idempotentný príjem a front notifikácií',6,'Rovnaké request_id pri opakovaní vytvorí jednu kartu; nedoručený e-mail nezmaže dopyt.')]),
 ('P3','Audit a návrh ponuky',[
  ('Štruktúrovaná auditná karta',6,'Proces, dáta, systémy, riziká, baseline, vlastník a tri príležitosti s overenými podkladmi.'),
  ('Verziovaný rozsah a Blueprint',6,'In-scope, out-of-scope, predpoklady a kritériá prijatia majú konkrétnu verziu.'),
  ('Ponuka z riadených položiek',6,'Ceny vypočíta kód z položiek; AI nemôže doplniť záväznú cenu ani termín.'),
  ('Interné schválenie a export ponuky',6,'Po úprave vznikne nová verzia; pred publikovaním je schválená; export nezverejní interné náklady.')]),
 ('P4','Klientsky portál a súbory',[
  ('Portál s explicitným členstvom',8,'Klient vidí len priradené projekty; e-mailová doména automaticky neprideľuje prístup.'),
  ('Požiadavky na podklady a súkromné súbory',8,'Povolené typy a limity, kontrola obsahu/MIME a karanténa; prístup sa overí aj pri sťahovaní.'),
  ('Publikovanie a schválenie konkrétnej verzie',8,'Rozpracované poznámky sú súkromné; klient potvrdzuje konkrétnu verziu dokumentu.'),
  ('Portálová časová os a komentáre',8,'Interné a zdieľané udalosti majú oddelené payloady; test sa vykoná aj priamo cez API.')]),
 ('P5','Realizácia a odovzdanie',[
  ('Projekt, míľniky a úlohy',6,'Schválený rozsah sa prevedie do projektu bez straty zdrojovej verzie a vlastníka.'),
  ('Zmenové požiadavky',6,'Zmena má dopad na cenu a termín; neschválená zmena nemení platný rozsah.'),
  ('Odovzdávací protokol a servisná požiadavka',4,'Odovzdanie viazané na akceptačné testy; podpora je jednoduchý ticket, nie chat v reálnom čase.'),
  ('Dashboard a časové metriky',4,'Dashboard ukazuje otvorené a omeškané kroky; KPI vychádzajú z uložených časových udalostí.')]),
 ('P6','AI a integrácia webu',[
  ('AI sumarizácia a chýbajúce údaje',8,'Výstup podľa schémy, s odkazom na vstup; neisté údaje zostanú neznáme; bez globálneho vyhľadávania.'),
  ('Návrh odpovede a schvaľovací záznam',8,'Schválenie je viazané na hash/verziu obsahu, adresáta a operáciu; zmena vyžaduje nové schválenie.'),
  ('Napojenie existujúceho webového formulára',6,'Zdrojový projekt je najprv identifikovaný; testovací formulár vytvorí kartu a zachová dohodnutú notifikáciu.'),
  ('AI evaluačná sada, limity a fallback',6,'Najmenej 30 scenárov vrátane prompt injection a cudzieho klienta; výpadok AI neblokuje ručné spracovanie.')]),
 ('P7','Overenie a prevádzka',[
  ('E2E, bezpečnosť a mobilná použiteľnosť',10,'Pokryté hlavné cesty, súbežné zmeny, priame API útoky na prístupy a mobilné šírky.'),
  ('Zálohy databázy aj súborov a obnova',8,'Obnova do čistého testovacieho prostredia preukáže údaje, prílohy aj oprávnenia; výsledok zapísaný.'),
  ('Monitoring, náklady a prenositeľné nasadenie',8,'Neúspešné úlohy sú viditeľné, retry obmedzené; nasadenie zo zdrojov a návod fungujú mimo autorovho zariadenia.'),
  ('Interný pilot, návod a release gate',6,'Dva týždne interného používania s priebežným záznamom; nulové otvorené kritické chyby; rozhodnutie go/no-go.')])
]
rows=[]; previous_phase_last=''; idx=0
for phase,name,tasks in phases:
    phase_start_previous=previous_phase_last
    for n,(task,hours,acceptance) in enumerate(tasks,1):
        idx+=1
        ident=f'{phase}-{n:02}'
        deps=previous_phase_last if n>1 else phase_start_previous
        rows.append({'ID':ident,'Faza':phase,'Oblast':name,'Priorita':'P0' if phase in ['P0','P1','P2','P4','P7'] else 'P1','Uloha':task,'Zaklad_hodin':hours,'Zavislosti':deps,'Kriterium_prijatia':acceptance,'Vlastnik':'Zakladateľ AiOS; AI pomáha, človek overuje','Stav':'Navrhnuté'})
        previous_phase_last=ident
with (root/'BACKLOG-AIOS-CONTROL-ROOM.csv').open('w',newline='',encoding='utf-8-sig') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
base=sum(x['Zaklad_hodin'] for x in rows)
internal_rate=40
capacity=25
packages=[('Audit',8,0,690),('Blueprint',20,0,1590),('Úzky pilot',60,150,4900),('Štandard',100,250,8900),('Rozšírené riešenie',160,400,13900)]
pricing=[]
for name,hours,cash,price in packages:
    hours_budget=hours*1.25
    cost=hours_budget*internal_rate+cash
    pricing.append({'name':name,'base_hours':hours,'hours_with_25pct_reserve':hours_budget,'external_delivery_cost_allowance':cash,'internal_rate':internal_rate,'cost_including_founder_time':cost,'recommended_price_ex_vat':price,'contribution':price-cost,'contribution_pct':round((price-cost)/price*100,1)})
support=[]
for name,price,hours,cost_tools in [('Care Basic',149,1,20),('Care',299,3,20),('Care Growth',599,6,30)]:
    cost=hours*internal_rate+cost_tools
    support.append({'name':name,'price_ex_vat_per_month':price,'included_hours':hours,'direct_internal_cost':cost,'contribution':price-cost,'contribution_pct':round((price-cost)/price*100,1)})
result={'task_count':len(rows),'base_hours':base,'reserve_pct':25,'reserve_hours':base*.25,'total_hours':base*1.25,'hours_per_week_assumption':capacity,'effective_weeks':base*1.25/capacity,'weeks_at_15h':math.ceil(base*1.25/15),'founder_time_opportunity_cost':base*1.25*internal_rate,'phase_hours':{p:sum(x['Zaklad_hodin'] for x in rows if x['Faza']==p) for p,_,_ in phases},'packages':pricing,'support':support,'pilot_40_40_20':[4900*.4,4900*.4,4900*.2],'pilot_remaining_after_audit_blueprint':4900-690-1590,'three_month_operating_allowance_eur':[80*3,200*3]}
(root/'evidence/planning-calculations.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
assert base==200
assert result['total_hours']==250
assert len({r['ID'] for r in rows})==len(rows)
print('WROTE',root/'BACKLOG-AIOS-CONTROL-ROOM.csv')
