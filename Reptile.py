import requests

# 1.指定url
url = 'https://code.51.com/jh/tg1/i11/ld2j29ic.html'

# 2.发起请求
# get会返回一个响应对象。
response = requests.get(url=url)

# 3.获取响应数据
page_text = response.text  # text表示获取字符串形式的响应数据
# print(page_text)

# 4.持久化存储
with open('51game.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
