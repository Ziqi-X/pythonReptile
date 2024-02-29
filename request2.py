import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

# 发送登陆处理接口的url地址
url = 'https://passport.17k.com/ck/user/login'
# 传递给服务器端的数据
data = {
    'loginName': '15027900535',
    'password': 'bobo328410948'
}
session = requests.Session()
session.post(url, headers=headers, data=data)

# 抓取登录后的数据:书架页面
# url = 'https://user.17k.com/www/bookshelf/'
# 书架页面的图书信息
url = 'https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919'
res = requests.get(url, headers=headers)

# 获取书架上的所有书籍
shelf_books = res.json()
print(shelf_books)
