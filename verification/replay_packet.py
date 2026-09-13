"""Replay reviewed finite checks in a disposable copy; preserve original bytes."""
from pathlib import Path
import argparse, hashlib, json, shutil, subprocess, sys, tempfile
from verify_source_packet import verify

ROOT=Path(__file__).resolve().parents[1]
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--receipt',type=Path);args=parser.parse_args()
    integrity=verify();m=json.loads((ROOT/'verification/source-packet.json').read_text(encoding='utf-8'))
    source=ROOT/m['packet_path'];fiber=(source/'verify_round4.py').exists()
    script='verify_round4.py' if fiber else 'verify_erdos500_packet.py'
    adaptations=[]
    with tempfile.TemporaryDirectory(prefix='math-packet-replay-') as td:
        work=Path(td)/'packet';shutil.copytree(source,work)
        if fiber:
            substitutions={
                '/mnt/data/ERDOS-595-SELF-GROWTH-THEOREM-CARDS-2026-08-04.jsonl':'ERDOS-595-SELF-GROWTH-THEOREM-CARDS-2026-08-04.jsonl',
                '/mnt/data/HIGH-GEAR-SELF-GROWTH-ROUND-2-2026-08-04/HIGH-GEAR-THEOREM-CARDS.jsonl':'HIGH-GEAR-THEOREM-CARDS.jsonl',
                '/mnt/data/RELATIONAL-SELF-GROWTH-ROUND-3-2026-08-04/RELATIONAL-THEOREM-CARDS.jsonl':'RELATIONAL-THEOREM-CARDS.jsonl'}
            text=(work/script).read_text(encoding='utf-8')
            for old,name in substitutions.items():
                target=ROOT/'verification/seed-dependencies'/name
                assert text.count(old)==1 and target.is_file()
                text=text.replace(old,target.as_posix())
                adaptations.append({'original_literal':old,'dependency':'verification/seed-dependencies/'+name})
            (work/script).write_bytes(text.encode('utf-8'))
        proc=subprocess.run([sys.executable,'-X','utf8','-S',str(work/script)],cwd=work,capture_output=True,encoding='utf-8',timeout=180)
        assert proc.returncode==0,(proc.returncode,proc.stderr[-2000:])
        output='FINAL-VERIFICATION.json' if fiber else 'ERDOS-500-VERIFICATION-RECEIPT.json'
        result=json.loads((work/output).read_text(encoding='utf-8'))
        assert result.get('passed') is True if fiber else result.get('status')=='PASS'
    verify()
    receipt={'ok':True,'source_script':m['packet_path']+'/'+script,'source_script_sha256':hashlib.sha256((source/script).read_bytes()).hexdigest(),'invocation':['python','-X','utf8','-S',script],'source_integrity':integrity,'path_adaptations_in_temporary_copy':adaptations,'scope':'Bundled finite/source checks rerun. No global conjecture closure, Lean certificate or novelty claim. Site packages disabled; optional SciPy MILP is not part of this replay.','result':result}
    if args.receipt:
        args.receipt.parent.mkdir(parents=True,exist_ok=True);args.receipt.write_bytes((json.dumps(receipt,indent=2)+'\n').encode())
    print(json.dumps({'ok':True,'script':script,'path_adaptations':len(adaptations)}))
if __name__=='__main__': main()
