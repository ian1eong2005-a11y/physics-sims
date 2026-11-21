"""Test harness pages for the N(T) applets: .harness/nt-<name>.html (explore) and .harness/nt-<name>-inq.html (investigation).

Adds an error recorder, a manual clock (__advance) and a canvas snapshot (__snap) like the main harness.
Run from the repo root:  python nt/tools/wrap.py
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from ntsci.embed import SIMS, build  # noqa: E402

OUT = ROOT / ".harness"
OUT.mkdir(exist_ok=True)
REC = """<script>window.__errs=[];addEventListener('error',e=>__errs.push(e.message+' @'+(e.lineno||'')));
window.__q=[];window.__now=0;window.requestAnimationFrame=cb=>{__q.push(cb);return __q.length};performance.now=()=>__now;
window.__advance=sec=>{const n=Math.round(sec*60);for(let i=0;i<n;i++){__now+=1000/60;const q=__q;__q=[];q.forEach(cb=>{try{cb(__now)}catch(e){__errs.push(e.message)}})}return __now};
window.__runInq=()=>{const nt=__nt,cfg=nt.cfg,q=s=>document.querySelector(s),out=[];__advance(0.3);
for(let k=0;k<(cfg.inquiry||[]).length;k++){const inq=cfg.inquiry[k];if(cfg.inquiry.length>1)q('[data-inq="'+k+'"]').click();
q('[data-guess="'+(inq.guessAns||0)+'"]').click();q('[data-act=next]').click();
inq.same.forEach(v=>{const c=[...document.querySelectorAll('[data-same]')].find(e=>e.dataset.same===v);c.checked=true;c.dispatchEvent(new Event('change',{bubbles:true}));});
q('[data-act=same]').click();const sameOK=nt.state().sameOK;q('[data-act=next]').click();
const c=cfg.controls.find(c=>c.id===inq.change),tests=inq.tests||c.options.map(o=>o[0]);
for(const v of tests){nt.api.set(inq.change,v);const go=q('#ntGo');if(go){go.click();__advance(40);}else __advance(0.5);q('[data-act=rec]').click();}
const tbl=[...document.querySelectorAll('.nt-tbl tr')].map(r=>[...r.cells].map(c=>c.innerText).join(' = ')).join(' | '),chart=!!q('.nt-chart');q('[data-act=next]').click();
inq.foundAns.forEach((a,i)=>{const sel=q('[data-found="'+i+'"]');sel.value=String(a);sel.dispatchEvent(new Event('change',{bubbles:true}));});
const sent=inq.found.map(x=>typeof x==='string'?x:'['+x[inq.foundAns[inq.found.filter(y=>typeof y!=='string').indexOf(x)]]+']').join('');
q('[data-act=found]').click();out.push({k,sameOK,tbl,chart,found:nt.state().foundOK,sent,locked:Object.keys(inq.fix||{})});}return out;};
window.__each=async(prefix,frac)=>{const nt=__nt,cfg=nt.cfg,q=s=>document.querySelector(s),out=[];let n=0;__advance(0.3);
const def=Object.assign({},nt.s);
for(const c of (cfg.controls||[])){const vals=c.options?c.options.map(o=>o[0]):[c.min,c.max];for(const v of vals){Object.keys(def).forEach(k=>{if(k[0]!=='_'&&nt.s[k]!==def[k])nt.api.set(k,def[k]);});nt.api.set(c.id,v);const go=q('#ntGo');
if(go){go.click();if(frac){const d=typeof cfg.go.time==='function'?cfg.go.time(nt.s):cfg.go.time;__advance(d*frac);await __snap(prefix+'_'+(n++));}__advance(40);}else __advance(1.3);
await __snap(prefix+'_'+(n++));out.push(c.id+'='+v+' :: '+[...document.querySelectorAll('.nt-rd')].map(e=>e.innerText.split(String.fromCharCode(10)).join(' ')).join(', ')+' :: '+q('.nt-say').innerText);}}
if(!(cfg.controls||[]).length){const go=q('#ntGo');if(go){go.click();__advance(40);}else __advance(1.3);await __snap(prefix+'_'+(n++));}return {n,out};};
window.__playMatch=()=>{const nt=__nt,cfg=nt.cfg,ids=cfg.bins.map(b=>b.id),bad=cfg.cards.filter(c=>![].concat(c.bin).every(b=>ids.includes(b))).map(c=>c.t);let guard=0;
while(nt.state().card&&guard++<200){const c=nt.state().card;document.querySelector('[data-bin="'+[].concat(c.bin)[0]+'"]').click();}
const st=document.querySelector('.nt-star');return {cards:cfg.cards.length,bins:ids.length,bad,end:st?st.innerText:'NOT FINISHED'};};
window.__snap=async(name,w=720)=>{const c=document.querySelector('canvas');const o=document.createElement('canvas');o.width=w;o.height=Math.round(c.height*w/c.width);const g=o.getContext('2d');g.fillStyle='#fff';g.fillRect(0,0,o.width,o.height);g.drawImage(c,0,0,o.width,o.height);const r=await fetch('/save?name='+name,{method:'POST',body:o.toDataURL('image/jpeg',0.8)});return r.text()};</script>"""
n = 0
for f in sorted(SIMS.glob("*.html")):
    for suffix, opts in (("", {}), ("-inq", {"inq": 1})):
        html = build(f.stem, opts).replace("<head>", "<head>" + REC, 1)
        (OUT / f"nt-{f.stem}{suffix}.html").write_text(html, encoding="utf-8")
    n += 1
print("wrapped", n)
RUNNER = """<!doctype html><meta charset="utf-8"><title>runner</title><iframe id="f" style="width:1100px;height:900px;border:0"></iframe><script>
async function load(src){const f=document.getElementById('f');await new Promise(r=>{f.onload=r;f.src=src+'?'+Date.now();});return f.contentWindow;}
async function run(names,frac){const out={};for(const n of names){let w=await load('nt-'+n+'.html'),ex,inq=null;const errs=[];
try{ex=w.__nt.cfg.draw?await w.__each(n,frac):w.__playMatch();}catch(e){ex='ERR '+e.message;}errs.push(...w.__errs);
if(w.__nt&&w.__nt.cfg.inquiry){w=await load('nt-'+n+'-inq.html');try{inq=w.__runInq();}catch(e){inq='ERR '+e.message;}errs.push(...w.__errs);}
out[n]={ex,inq,errs};}return out;}
async function brief(names,frac){const r=await run(names,frac),L=[];for(const n in r){const o=r[n];let ex=typeof o.ex==='string'?o.ex:o.ex.end?('match '+o.ex.cards+' cards, '+o.ex.bins+' bins, bad='+o.ex.bad.length+', '+o.ex.end):('shots '+o.ex.n);
let iq=o.inq===null?'no inq':typeof o.inq==='string'?o.inq:o.inq.map(q=>(q.sameOK&&q.found&&q.chart?'OK':'FAIL same='+q.sameOK+' found='+q.found+' chart='+q.chart)+' ['+q.tbl.split(' | ').slice(1).map(x=>x.split(' = ').slice(1).join('/')).join(', ')+']').join(' ; ');
L.push(n+' :: '+ex+' :: '+iq+' :: errs '+JSON.stringify(o.errs));}return L.join(String.fromCharCode(10));}
</script>"""
(OUT / "nt-runner.html").write_text(RUNNER, encoding="utf-8")
