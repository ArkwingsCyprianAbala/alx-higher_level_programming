"""Fetches https://alx-intranet.hbtn.io/status."""
from urllib.request import urlopen

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(url) as response:
        html_by = response.read()
        html_a = html_by.decode()
        print("- " + html_a.replace("\n", "\n\t-"))
