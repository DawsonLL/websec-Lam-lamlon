import requests
from PIL import Image
import pytesseract
import re
from io import BytesIO
from bs4 import BeautifulSoup

# Define the site URL
site = "0a5e00b0039cb54380af627c002d009f.web-security-academy.net"  # Replace with the actual site

# Define the post URL (where the comment with the avatar is located)
post_url = f"https://{site}/post?postId=2"  # Replace with the actual URL of the blog post

# Create a session
s = requests.Session()

# Make a request to get the post content
resp = s.get(post_url)
soup = BeautifulSoup(resp.text, 'html.parser')

# Find the avatar image URL (PNG format)
avatar_path = soup.find_all('img', src=re.compile(r'png$'))[0].get('src')
avatar_url = f'https://{site}{avatar_path}'
print(f'Avatar URL: {avatar_url}')

# Use OCR package (Tesseract) to extract hostname from the avatar image
hostname = pytesseract.image_to_string(Image.open(BytesIO(s.get(avatar_url).content)))

# Clean up the extracted hostname
hostname = hostname.strip()
print(f'Exfiltrated hostname: {hostname}')

# Submit the extracted hostname as the solution
solution_url = f'https://{site}/submitSolution'  # Replace with actual solution submission URL
solution_data = {
    'answer': hostname
}
response = s.post(solution_url, data=solution_data)

# Print the response from the solution submission
print(response.text)
