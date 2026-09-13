"""Verify preserved source bytes and record counts without certifying claims."""
from pathlib import Path
import collections, hashlib, json

ROOT=Path(__file__).resolve().parents[1]
def sha(b): return hashlib.sha256(b).hexdigest()
def verify():
    m=json.loads((ROOT/'verification/source-packet.json').read_text(encoding='utf-8'))
    for f in m['files']:
        p=(ROOT/f['public_path']).resolve();assert p.is_relative_to(ROOT.resolve())
        b=p.read_bytes();assert len(b)==f['bytes'] and sha(b)==f['sha256'],f['public_path']
    record_file=ROOT/m['records_path'];s=record_file.read_text(encoding='utf-8')
    records=json.loads(s) if record_file.suffix=='.json' else [json.loads(l) for l in s.splitlines() if l.strip()]
    assert len(records)==m['record_count']
    assert dict(collections.Counter(str(r['status']) for r in records))==m['status_counts']
    original=ROOT/m['packet_path']/'MANIFEST.json';n=0
    if original.exists():
        for name,value in json.loads(original.read_text(encoding='utf-8'))['files'].items():
            p=(original.parent/name).resolve();assert p.is_relative_to(original.parent.resolve())
            expected=value['sha256'] if isinstance(value,dict) else value
            assert sha(p.read_bytes())==expected;n+=1
    assert n==m['original_manifest_entries_verified']
    dependencies=ROOT/'verification/seed-dependencies/manifest.json'
    if dependencies.exists():
        for f in json.loads(dependencies.read_text(encoding='utf-8'))['files']:
            b=(dependencies.parent/f['file']).read_bytes();assert len(b)==f['bytes'] and sha(b)==f['sha256']
    return {'ok':True,'source_files':len(m['files']),'source_records':len(records),'original_manifest_entries':n,'scope':'Source integrity and structure; not independent theorem certification.'}
if __name__=='__main__': print(json.dumps(verify(),sort_keys=True))
