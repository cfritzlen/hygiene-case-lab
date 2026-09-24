# Builds the two GitHub Pages versions from case-lab.html (the artifact source).
#   index.html  = web version: original side-by-side layout
#   phone.html  = phone version: phone layout forced at every width
import re

src = open('case-lab.html', encoding='utf-8').read()

def skeleton(body, theme_color='#FFF5F8'):
    head = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="{theme_color}">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Case Lab">
<style>html{{color-scheme:light}}body{{margin:0;font:14px system-ui,sans-serif;background:#fafafa}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
'''
    i = body.index('<style>')
    title, rest = body[:i], body[i:]
    j = rest.rindex('</style>') + len('</style>')
    return head + title + rest[:j] + '\n</head>\n<body>\n' + rest[j:] + '\n</body>\n</html>\n'

# Device detection on the main URL: phones go to phone.html unless the viewer
# chose the web version (?web or a remembered choice). Runs before anything paints.
DETECT = '''<script>
(function(){try{
  var q=location.search;
  if(q.indexOf("web")>-1){localStorage.setItem("hcl-ver","web");return;}
  if(localStorage.getItem("hcl-ver")==="web")return;
  var phone=Math.min(screen.width,screen.height)<768||/Android|iPhone|iPad|iPod|Mobile/i.test(navigator.userAgent);
  if(phone)location.replace("phone.html"+location.hash);
}catch(e){}})();
</script>
'''
NO_TAP_ZOOM = '<style>button,a,input,select,textarea{touch-action:manipulation}</style>\n'

# ---- web: drop the phone block entirely, link to phone version
web = src
web = re.sub(r'@media \(max-width:820px\)\{/\*PHONE-BLOCK\*/.*?\n\}\n', '', web, count=1, flags=re.S)
web = web.replace('<!--VERSIONLINK-->', '<a class="verlink" href="phone.html">Phone version →</a>')
web = web.replace('<style>', DETECT + NO_TAP_ZOOM + '<style>', 1)
open('index.html', 'w', encoding='utf-8').write(skeleton(web))

# ---- phone: make the phone block apply at every width, cap the page width, link back
phone = src
phone = phone.replace('@media (max-width:820px){/*PHONE-BLOCK*/', '@media (min-width:0px){/*PHONE-BLOCK*/')
phone = phone.replace('.wrap{max-width:1080px;', '.wrap{max-width:600px;')
phone = phone.replace('<!--VERSIONLINK-->', '<a class="verlink" href="./?web">Web version →</a>')
phone = phone.replace('<style>', '<script>try{localStorage.removeItem("hcl-ver")}catch(e){}</script>\n' + NO_TAP_ZOOM + '<style>', 1)
open('phone.html', 'w', encoding='utf-8').write(skeleton(phone))

print('built index.html (web) and phone.html (phone)')
