import requests
from lxml import etree

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
# }
# url = 'http://www.cip.cc/'
#
# page_text = requests.get(url, headers=headers).text
# tree = etree.HTML(page_text)
# print(tree)
# text = tree.xpath('/html/body/div/div/div[3]/pre/text()')[0]
# print(text.split('\n')[0])

str = 'a/b/c'
ret1 = str.split('/')[0]
ret2 = str.split('/')[-3]
print(ret1,ret2)