import re, json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from playwright.sync_api import sync_playwright
src = open('packet.html').read()
src = re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis[^>]*>', '', src)
src = src.replace("--font-d: 'Bricolage Grotesque', 'Inter Display'", "--font-d: 'Inter Display'").replace("--font-b: 'Atkinson Hyperlegible', Inter", "--font-b: Inter")
open('packet_pdf.html','w').write('<!doctype html><html><head><meta charset="utf-8"></head><body>'+src+'</body></html>')

PAGINATE = r"""()=>{
 const LIM=995;
 const book=document.getElementById('book');
 let sheets=[...book.querySelectorAll('.sheet')];
 for(let si=0;si<sheets.length;si++){
  const sh=sheets[si];
  if(sh.querySelector('.flyer')) continue;
  const top=()=>sh.getBoundingClientRect().top;
  const kids=()=>[...sh.children].filter(c=>!/holes|tabs|foot/.test(c.className));
  const ks=kids();
  let cut=-1;
  for(let i=0;i<ks.length;i++){ if(ks[i].getBoundingClientRect().bottom-top()>LIM && i>2){cut=i;break;} }
  if(cut<0) continue;
  if(ks[cut-1] && ks[cut-1].tagName==='H3' && cut-1>2) cut--;
  const h1=sh.querySelector('h1'); const title=h1?h1.childNodes[0].textContent:'';
  const kick=sh.querySelector('.kicker'); 
  const n=document.createElement('section'); n.className='sheet';
  n.appendChild(sh.querySelector('.holes').cloneNode(true));
  n.appendChild(sh.querySelector('.tabs').cloneNode(true));
  const kp=document.createElement('p'); kp.className='kicker'; kp.textContent=kick?kick.textContent:''; n.appendChild(kp);
  const hh=document.createElement('h1'); hh.innerHTML=title+'<small>continued</small>'; n.appendChild(hh);
  const foot=sh.querySelector('.foot').cloneNode(true);
  for(let i=cut;i<ks.length;i++) n.appendChild(ks[i]);
  n.appendChild(foot);
  sh.after(n); sheets.splice(si+1,0,n);
 }
 const all=[...book.querySelectorAll('.sheet')];
 all.forEach((s,i)=>{ const sp=s.querySelectorAll('.foot span'); if(sp[1]) sp[1].textContent=(i+1)+' of '+all.length; });
 const first={};
 all.forEach((sh,i)=>{ const ts=[...sh.querySelectorAll('.tabs .tab')]; const k=ts.findIndex(t=>t.classList.contains('on')); if(k>=0 && !(k in first)) first[k]=i+1; });
 [...document.querySelectorAll('.toc > a > div')].forEach((d,k)=>{ const pgEl=d.querySelector('.pg'); if(pgEl&&first[k]) pgEl.textContent='p. '+first[k]; });
 return all.length;
}"""
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium') if False else p.chromium.launch()
    pg = b.new_page(viewport={'width':1000,'height':1200})
    msgs=[]; pg.on('console', lambda m: msgs.append(m.text)); pg.on('pageerror', lambda e: msgs.append(str(e)))
    pg.goto('file://' + os.path.abspath('packet_pdf.html'))
    pg.emulate_media(media='print')
    over = pg.evaluate('''()=>[...document.querySelectorAll('.sheet')].map((s,i)=>{const f=s.querySelector('.foot').getBoundingClientRect(); let mx=0; s.querySelectorAll('.item,table,h3,p,.lines,.box,ul').forEach(e=>{if(!e.closest('.foot')&&!e.closest('.tabs')){const r=e.getBoundingClientRect(); mx=Math.max(mx,r.bottom-s.getBoundingClientRect().top)}}); return [i+1, Math.round(mx/96*100)/100]})''')
    print('pages', pg.evaluate(PAGINATE))
    print(msgs)
    print('content bottom (in) per sheet; limit ~10.1:', over)
    open('render_result.json','w').write(json.dumps({'msgs': msgs}))
    pg.pdf(path='Moms_Activity_Packet.pdf', width='8.5in', height='11in', print_background=True, prefer_css_page_size=True)
    b.close()
