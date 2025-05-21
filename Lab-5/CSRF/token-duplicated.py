import requests
from bs4 import BeautifulSoup

site = '0a89003704c1460080a1039900ff0079.web-security-academy.net'
'''
def getHeadersFromSearch(search_term):
    resp = requests.get(f"https://{site}/?search={search_term}")
    for header in resp.headers.items():
        print(header)

getHeadersFromSearch("lamlon\nSet-Cookie: foo=bar")
'''

s = requests.Session()
login_url = f'https://{site}/login'
resp = s.get(login_url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')
print(f' csrf field in form field: {csrf}')
for header in resp.headers.items():
    print(header)

for cookie in s.cookies.items():
    print(cookie)

s.cookies.clear()
logindata = {
    'csrf' : csrf,
    'username' : 'wiener',
    'password' : 'peter'
}
resp = s.post(login_url, data=logindata)
print(f"HTTP status code {resp.status_code} with text {resp.text}")