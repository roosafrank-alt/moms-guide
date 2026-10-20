"""Build the live site from source/packet.html. Run: python3 source/build_site.py
Steps: regenerate Ideas/Walks block, smoke-test the phone view, render the PDF,
write ../index.html (with phone-app tags), copy the PDF, bump the service-worker cache.
Exits non-zero (and changes nothing in the site) if a check fails."""
import os, re, subprocess, sys, json, shutil
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); os.chdir(HERE)
def run(*a):
    r = subprocess.run(a, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr
rc, out = run(sys.executable, 'build_ideas.py')
if rc: sys.exit('build_ideas failed:\n' + out)
src = open('packet.html').read()
# smoke test: phone view, no JS errors, planner present
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(); ctx = b.new_context(viewport={'width': 390, 'height': 844}, is_mobile=True, has_touch=True)
    pg = ctx.new_page(); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('file://' + os.path.join(HERE, 'packet.html')); pg.wait_for_timeout(600)
    n_btn = pg.evaluate("document.querySelectorAll('.addbtn').length")
    has_box = pg.evaluate("!!document.querySelector('#home .newbox')")
    pg.goto('file://' + os.path.join(HERE, 'packet.html') + '#my'); pg.wait_for_timeout(300)
    has_my = pg.evaluate("!!document.querySelector('#mine .seg')")
    b.close()
if errs or n_btn < 100 or not has_box or not has_my:
    sys.exit('smoke test failed: errors=%s buttons=%s box=%s my=%s' % (errs, n_btn, has_box, has_my))
rc, out = run(sys.executable, 'render.py')
m = re.search(r'pages (\d+)', out)
res = json.load(open('render_result.json'))
if rc or not m or not (50 <= int(m.group(1)) <= 70) or res['msgs']:
    sys.exit('render failed or page count out of range:\n' + out[:800])
pages = int(m.group(1))
tags = ('<title>Mom\'s Guide</title>\n<link rel="manifest" href="manifest.webmanifest">\n<meta name="theme-color" content="#2f6b4f">\n'
        '<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="mobile-web-app-capable" content="yes">\n'
        '<meta name="apple-mobile-web-app-title" content="Mom\'s Guide">\n<link rel="apple-touch-icon" href="icon-192.png">\n'
        "<script>if('serviceWorker' in navigator){navigator.serviceWorker.register('sw.js').catch(function(){});}</script>\n")
site = tags + src.replace("<title>Mom's Activity Packet</title>\n", '', 1)
open(os.path.join(ROOT, 'index.html'), 'w').write(site)
shutil.copy('Moms_Activity_Packet.pdf', os.path.join(ROOT, 'Moms_Activity_Packet.pdf'))
sw = open(os.path.join(ROOT, 'sw.js')).read()
v = re.search(r"moms-guide-v(\d+)", sw)
sw = sw.replace(v.group(0), 'moms-guide-v%d' % (int(v.group(1)) + 1))
open(os.path.join(ROOT, 'sw.js'), 'w').write(sw)
for f in ('packet_pdf.html', 'render_result.json', 'Moms_Activity_Packet.pdf'):
    try: os.remove(f)
    except OSError: pass
print('OK: site built, %d PDF pages, %d add buttons' % (pages, n_btn))
