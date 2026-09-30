from pathlib import Path
import re,json
p=Path('/home/ubuntu/aios-site-audit/evidence/routes.js')
s=p.read_text()
patterns=['onSubmit:',r'preventDefault\(\)',r'fetch\(',r'new FormData',r'/api/',r'setTimeout',r'mailto:',r'auditRequests',r'formSubmit',r'emailjs']
result={}
for pattern in patterns:
    matches=list(re.finditer(pattern,s))
    result[pattern]={'count':len(matches),'samples':[s[max(0,m.start()-500):m.end()+1100] for m in matches[-4:]]}
out=Path('/home/ubuntu/aios-site-audit/evidence/submit-handler.json')
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
