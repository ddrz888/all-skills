import json
from pathlib import Path
p=Path('/home/ubuntu/aios-product-plan/evidence/planning-calculations.json')
data=json.loads(p.read_text())
audit=data['packages'][0]['recommended_price_ex_vat']
blueprint=data['packages'][1]['recommended_price_ex_vat']
for package in data['packages'][2:]:
    package['full_project_including_audit_blueprint']=audit+blueprint+package['recommended_price_ex_vat']
data.pop('pilot_remaining_after_audit_blueprint',None)
data['all_in_pilot_schedule_40_40_20']=[7180*.4,7180*.4,7180*.2]
p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
for package in data['packages'][2:]:
    print(package['name'], package['full_project_including_audit_blueprint'])
print('Implementation payment schedule',data['pilot_40_40_20'])
