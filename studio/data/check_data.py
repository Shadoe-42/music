"""Check studio data against studio/vocab.md. Run before every commit: python3 check_data.py"""
import csv, re, sys, pathlib
here = pathlib.Path(__file__).parent
vocab = set(re.findall(r'^\| `([^`]+)` \|', (here.parent / 'vocab.md').read_text(), re.M))
devices = list(csv.DictReader(open(here / 'devices.csv')))
conns = list(csv.DictReader(open(here / 'connections.csv')))
slugs = [d['slug'] for d in devices]
errs = []
if len(slugs) != len(set(slugs)): errs.append('duplicate device slug')
ids = [c['id'] for c in conns]
if len(ids) != len(set(ids)): errs.append('duplicate connection id')
for d in devices:
    for f in ('zone', 'basis'):
        if d[f] and d[f] not in vocab: errs.append(f"{d['slug']}: {f} '{d[f]}' not in vocab")
for c in conns:
    if c['id'][0] not in 'AMVPD': errs.append(f"{c['id']}: bad prefix")
    for f in ('signal', 'connector_from', 'connector_to', 'zone_from', 'zone_to', 'status', 'basis'):
        if c[f] and c[f] not in vocab: errs.append(f"{c['id']}: {f} '{c[f]}' not in vocab")
    for f in ('from', 'to'):
        if c[f] and c[f].split('.')[0] not in slugs: errs.append(f"{c['id']}: {f} '{c[f]}' is not a known device")
    if c['status'] == 'tested' and not c['verified']: errs.append(f"{c['id']}: tested without a verified date")
print('\n'.join(errs) if errs else f'OK: {len(devices)} devices, {len(conns)} connections')
sys.exit(1 if errs else 0)
