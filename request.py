import requests

# 1.创建一个空白的session对象
session = requests.Session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}
main_url = 'https://xueqiu.com/'
# 2.使用session发起的请求，目的是为了捕获到cookie，且将其存储到session对象中
session.get(url=main_url, headers=headers)

url = 'https://xueqiu.com/statuses/hot/listV2.json'
param = {
    "since_id": "-1",
    "max_id": "522372",
    "size": "15",
}
response = session.get(url=url, headers=headers, params=param)
data = response.json()
print(data)
