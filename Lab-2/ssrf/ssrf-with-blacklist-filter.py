import requests

url = "https://0a2b009c04c5d3268243d48f0034006e.web-security-academy.net/"  # Replace with the target URL
response = requests.get(url, headers={'Referer': 'https://burpcollaborator.net'})

# Print the response to see if the request was successful
print(response.text)
