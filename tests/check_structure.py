"""Deterministic packaging/coverage checks; never a substitute for behavior runs."""
import hashlib, json, re, sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
failures=[]
def check(condition,message):
    if not condition: failures.append(message)
skill=root/'SKILL.md'
check(root.name=='nova-ux-intelligence','Package folder must be nova-ux-intelligence')
check(skill.is_file(),'Missing skill entrypoint')
if skill.is_file():
    text=skill.read_text()
    check(text.startswith('---\nname: nova-ux-intelligence\ndescription: Use when'),'Invalid discovery frontmatter')
    check(len(text.split())<=1100,'Entrypoint exceeds 1100-word engineering budget')
    check(len(text.encode())<=10000,'Entrypoint exceeds byte budget')
    for marker in ('## Delivery surface','Chat / advisory','Code / implementation'):
        check(marker in text,f'Missing delivery mode: {marker}')
    for banned in ('Hello Krabi','Cairo','WhatsApp','navy/gold','/Users/'):
        check(banned.lower() not in text.lower(),f'Project-specific entrypoint: {banned}')
required=['README.md','MOBILE.md','PRIVACY.md','TERMS.md','SUPPORT.md','LICENSE','CONTRIBUTING.md','.gitignore','.github/workflows/validate.yml','references/domains.md','references/evidence.md','references/quality.md','references/materials.md','operations/diagnose.md','operations/design.md','operations/verify.md','agents/openai.yaml','tests/kernel-contract.json','tests/source/frozen-kernel.md','tests/traceability.json','submission/listing.md','submission/review-tests.json','submission/release-notes.md']
for path in required: check((root/path).is_file(),f'Missing {path}')
runtime=[skill,*root.glob('references/*.md'),*root.glob('operations/*.md')]
linked=set()
paragraphs={}
for path in runtime:
    if not path.exists(): continue
    text=path.read_text()
    for target in re.findall(r'\]\(([^)]+)\)',text):
        if '://' not in target:
            dest=(path.parent/target.split('#')[0]).resolve()
            check(dest.is_file(),f'Broken link {path.name}: {target}')
            linked.add(dest)
    for paragraph in text.split('\n\n'):
        if len(paragraph)>180 and not paragraph.startswith('#'):
            check(paragraph not in paragraphs,f'Duplicated substantial paragraph: {path.name}')
            paragraphs[paragraph]=path
for p in runtime[1:]: check(p.resolve() in linked,f'Unrouted module: {p.name}')
for path in [skill,root/'agents/openai.yaml']:
    if path.exists(): check('ui-ux-design-expert' not in path.read_text(),f'Legacy identity in {path.relative_to(root)}')
cases=json.loads((root/'tests/cases.json').read_text())
ids={c['id'] for c in cases}
check(set(f'T{i}' for i in range(1,14))<=ids,'Missing T1-T13')
check(set(f'A{i}' for i in range(1,9))<=ids,'Missing A1-A8')
check({f'FM-{i:02}' for i in range(1,19)}=={f for c in cases for f in c['failure_modes']},'Incomplete failure register coverage')
check(all(c['pass_criteria'] and c['prompt'] for c in cases),'Empty behavioral case')
contract=root/'tests/kernel-contract.json'
if contract.exists():
    data=json.loads(contract.read_text())
    source=root/'tests/source/frozen-kernel.md'
    check(source.exists() and hashlib.sha256(source.read_bytes()).hexdigest()==data['source_sha256'],'Frozen source changed without migration')
    trace=root/'tests/traceability.json'
    if trace.exists():
        mapping=json.loads(trace.read_text())
        check(set(mapping)==set(data['invariants']),'Frozen invariant missing from traceability')
        for key,paths in mapping.items():
            check(bool(paths) and all((root/p).exists() for p in paths),f'Unresolved invariant: {key}')
report={'kind':'structural-only','status':'FAIL' if failures else 'PASS','failures':failures,'case_count':len(cases),'failure_class_count':len({f for c in cases for f in c['failure_modes']})}
print(json.dumps(report,indent=2))
sys.exit(bool(failures))
