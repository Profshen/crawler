# 难度：Moderate
# 从`https://unsplash.com`上下载高清壁纸，用了一个批量的方法，下载高清大图
# 使用PhantomJS后，设定了一个JS代码执行，模拟向下滚屏，`window.scrollTo(0, document.body.scrollHeight)`

import re
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

class getImages():

    def __init__(self):
        self.url = 'https://unsplash.com/'
        self.folder_path = 'Users/lyndon/PycharmProjects/imgs'

    def image(self, url):
        # 使用Selenium的PhantomJS来进行网络请求
        driver = webdriver.PhantomJS()
        driver.get(self.url)
        # 执行7次网页下拉操作
        self.scroll_down(driver = driver, times = 7)
        content = BeautifulSoup(driver.page_source, 'lxml')
        links = re.findall('class=\"cV68d\" src=\"(.*?)\" style=', str(content))
        for link in links:
            path = self.folder_path + '/' + str(link).split('?')[0].split('photo-')[-1] + '.jpg'
            self.saveImage(link, path)

    def getImage(self, link):
        return requests.get(link)

    def saveImage(self, url, path):
        img = self.getImage(url)
        f = open(path, 'ab')
        f.write(img.content)
        f.close()

    def scroll_down(self, driver, times):
        for i in range(times):
            # 执行一段JS代码
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(20)

unsplash = getImages()
unsplash.image('https://unsplash.com/')
