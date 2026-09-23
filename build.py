# Builds index.html (GitHub Pages) from case-lab.html (artifact source).
src=open('case-lab.html',encoding='utf-8').read()
head='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#FFF5F8">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Case Lab">
<style>html{color-scheme:light}body{margin:0;font:14px system-ui,sans-serif;background:#fafafa}img{max-width:100%}[hidden]{display:none!important}</style>
'''
i=src.index('<style>')
title=src[:i]; rest=src[i:]
j=rest.index('</style>')+len('</style>')
open('index.html','w',encoding='utf-8').write(head+title+rest[:j]+'\n</head>\n<body>\n'+rest[j:]+'\n</body>\n</html>\n')
print('index.html built')
