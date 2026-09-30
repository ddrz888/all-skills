from pathlib import Path
import json
import re

root = Path('/home/ubuntu/aios-overview')
inv = json.loads((root / 'inventory.json').read_text())
report = root / 'PREHLAD-AIOS-SYSTEMS.md'
tree = root / 'STRUKTURA-AIOS-SYSTEMS.txt'
for path in (report, tree):
    if not path.exists() or path.stat().st_size == 0:
        raise SystemExit(f'MISSING OR EMPTY: {path}')
text = report.read_text()
tree_text = tree.read_text()
combined = text + '\n' + tree_text
missing = [name for name in inv['top_level_directories'] if name.strip() not in combined]
missing_children = [f'{folder}/{name}' for folder, names in inv['container_directories'].items() for name in names if name not in combined]
headings = re.findall(r'^# .+$', text, re.M)
references = set(re.findall(r'^\[(\d+)\]:', text, re.M))
used_refs = set(re.findall(r'(?<!\!)\[(\d+)\](?!:)', text))
placeholders = re.findall(r'\b(?:TODO|TBD|lorem ipsum|PLACEHOLDER)\b', text, re.I)
result = {
    'files': [{'path': str(p), 'bytes': p.stat().st_size} for p in (report, tree)],
    'root_directory_count_including_hidden': len(inv['top_level_directories']),
    'visible_root_directory_count': len([x for x in inv['top_level_directories'] if not x.startswith('.')]),
    'code_projects_direct_children': len(inv['container_directories']['Code_Projects']),
    'missing_root_directories': missing,
    'missing_direct_children': missing_children,
    'h1_count': len(headings),
    'unresolved_numeric_references': sorted(used_refs - references),
    'code_fences_balanced': text.count('```') % 2 == 0,
    'placeholder_matches': placeholders,
    'report_word_count': len(text.split()),
    'tree_line_count': len(tree_text.splitlines()),
}
print(json.dumps(result, ensure_ascii=False, indent=2))
(root / 'validation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
if missing or missing_children or len(headings) != 1 or used_refs - references or placeholders or text.count('```') % 2:
    raise SystemExit(1)
