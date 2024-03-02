#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
from urllib.request import urlopen

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(url) as response:
        html = response.read().decode('utf-8')

for line in html.splitlines():
    print(f"- {line}")
