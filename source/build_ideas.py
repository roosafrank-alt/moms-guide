import json,sys,re,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,'.')
import importlib, ideas_data as D
importlib.reload(D)
COIN=getattr(D,'COIN',[])
s=open('packet.html').read()
if "k: 'ideas'" not in s:
    s=s.replace("    { k: 'me', l: 'Mine'","    { k: 'ideas', l: 'Ideas', name: 'Ideas', c: '#7a4e8a', d: 'Classes and places with no fixed dates' },\n    { k: 'me', l: 'Mine'",1)
s=re.sub(r"\n  // IDEAS BEGIN.*?// IDEAS END","",s,flags=re.S)
def rows(L): return L
def page(title,sub,lead,L,chunks):
    out=[]
    for ci,ch in enumerate(chunks):
        out.append((title,sub,lead if ci==0 else '',ch))
    return out
js="\n  // IDEAS BEGIN\n  (function(){\n  var IH='<tr><th style=\"width:19%\">Who</th><th style=\"width:19%\">Address and drive</th><th style=\"width:20%\">Contact</th><th style=\"width:28%\">What and how it works</th><th style=\"width:14%\">Cost</th></tr>';\n  function R(a){return '<tr><td><b>'+a[0]+'</b><br><span style=\"color:var(--soft);font-weight:400\">'+a[1]+'</span></td><td>'+a[2]+'</td><td>'+a[3]+'</td><td>'+a[4]+'</td><td>'+a[5]+'</td></tr>';}\n  function P(sec,lead,rows,ttl,hdr){var h=head('Fall 2026 – Winter 2027 · Wurtsboro, NY and nearby',ttl,sec,lead);return h+'<table class=\"t\" style=\"table-layout:fixed;font-size:8.4pt\">'+(hdr||IH)+rows.map(R).join('')+'</table>';}\n"
def emit(sec,lead,L,split,key='ideas'):
    global js
    parts=[L[:split],L[split:]] if split else [L]
    for i,p in enumerate(parts):
        if not p: continue
        js+="  add('%s',P(%s,%s,%s,%s));\n"%(key,json.dumps(sec+(' (cont.)' if i else '')),json.dumps(lead if i==0 else ''),json.dumps(p),json.dumps('Ideas' if key=='ideas' else 'Walks and Runs'))
L1='<p class="lead">No fixed dates. Call first to ask about the next class and to confirm price. Drive times are estimates.</p>'
emit('arts and crafts',L1,D.ARTS,0)
emit('gardening',L1,D.GARD,0)
RR=[[x[1],x[0],x[2],x[5],x[3],x[4]] for x in D.RACES]
IHR_JS = '''  var IHR='<tr><th style=\\"width:19%\\">Event and date</th><th style=\\"width:19%\\">Address and drive</th><th style=\\"width:20%\\">Sign up or contact</th><th style=\\"width:28%\\">Times and details</th><th style=\\"width:14%\\">Cost</th></tr>';\n  function P('''
js=js.replace("  function P(", IHR_JS, 1)
js+="  add('walk',P('walks and 5Ks with set dates','<p class=\"lead\">5Ks with a walk option, through November. None found yet for December to March. Costs include sign-up fees. Drive times are estimates.</p>',%s,'Walks and Runs',IHR));\n"%json.dumps(RR)
emit('walking groups and clubs','<p class=\"lead\">Groups that meet on a regular day. Call to confirm the next meeting and the start place.</p>',D.GROUP,0,'walk')
emit('places to hike','<p class=\"lead\">Trails to walk any day. Some have guided hikes. Call first for those.</p>',D.HIKE,0,'walk')
L2='<p class="lead">No coin club in this area turned up in the search. Ask the shops below if one meets nearby. Call to confirm before going.</p>'
pass
js+="  })();\n  // IDEAS END"
s=s.replace("\n  add('host', head(",js+"\n  add('host', head(",1)
open('packet.html','w').write(s)
