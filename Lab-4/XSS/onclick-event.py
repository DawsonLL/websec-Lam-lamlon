import requests
from bs4 import BeautifulSoup

s = requests.Session()
site = '0af900b80436d23580cb03b500eb00eb.web-security-academy.net'
def try_post(name, website_link):
    blog_post_url = f'https://{site}/post?postId=1'
    resp = s.get(blog_post_url)
    soup = BeautifulSoup(resp.text,'html.parser')
    csrf = soup.find('input', {'name':'csrf'}).get('value')

    comment_url = f'https://{site}/post/comment'
    comment_data = {
        'csrf' : csrf,
        'postId' : '1',
        'comment' : 'tomato',
        'name' : name,
        'email' : 'lamlon@pdx.edu',
        'website': website_link
    }
    resp = s.post(comment_url, data=comment_data)

def main():
   try_post("single quote HTML encoded",'https://pdx.edu/&apos;')

if __name__ == "__main__":
    main()