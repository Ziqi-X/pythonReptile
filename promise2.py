import requests
from lxml import etree
import os
import time
from threading import Thread # 线程模块

# 异步多线程

dirName = 'imgLibs'
if not os.path.exists(dirName):
    os.mkdir(dirName)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

stat = time.time()

for page in range(2, 3):
    url = 'https://www.pkdoutu.com/zz/list/?page=%d' % page
    page_text = requests.get(url, headers=headers).text
    tree = etree.HTML(page_text)
    # a_alist = tree.xpath('//*[@id="pic-detail"]/div/div[2]/div[2]/ul/li/div/div/a')
    a_alist = tree.xpath('//*[@id="making-list"]/div[2]/a')
    for a in a_alist:
        print(a)
        # 图片是滑动滚轮后单独加载出来的（图片懒加载）
        img_src = a.xpath('./img/@data-original')[0]
        img_title = img_src.split('/')[-1]
        img_path = dirName + '/' + img_title
        img_data = requests.get(img_src, headers=headers).content
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
        print(img_title, '：爬取保存成功！')

print('总耗时', time.time() - stat)
