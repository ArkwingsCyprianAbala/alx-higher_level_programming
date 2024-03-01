#!/usr/bin/python3
#fetching urls
import urllib.request

req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
   the_page = response.read().decode('utf-8')

for line in the_page.splitlines():
    print(f"- {line}")
