from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen, Request
from concurrent.futures import ThreadPoolExecutor
import json, re

root=Path('/home/ubuntu/aios-site-audit/evidence')
class Parser(HTMLParser):
    def __init__(self):
        super().__init__(); self.scripts=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='script' and a.get('src'): self.scripts.append(a['src'])
p=Parser(); p.feed((root/'index.html').read_text())
urls=list(dict.fromkeys(urljoin('https://aios.macaly.app',s) for s in p.scripts))
def fetch(item):
    i,url=item
    try:
        with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=20) as r:
            data=r.read(6000000).decode('utf-8','replace')
        file=root/f'public-script-{i:02}.js';file.write_text(data)
        relevant=any(x in data for x in ['Rezervovať vstupný','Najväčší procesný','name:"consent"','readiness'])
        snippets=[]
        if relevant:
            for pattern in ['onSubmit','preventDefault','fetch\\(','Ďakujeme','FormData','mailto:','/api/']:
                for m in list(re.finditer(pattern,data))[:5]:
                    snippets.append({'pattern':pattern,'snippet':data[max(0,m.start()-250):m.end()+850]})
        return {'url':url,'file':str(file),'chars':len(data),'relevant':relevant,'snippets':snippets}
    except Exception as e:return {'url':url,'error':str(e)}
with ThreadPoolExecutor(max_workers=4) as pool: result=list(pool.map(fetch,enumerate(urls)))
(root/'public-script-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
