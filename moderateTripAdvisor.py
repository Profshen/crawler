# 难度：Moderate
# 以猫途鹰网站（https://www.tripadvisor.cn/）为例来进行模拟登录，到达个人收藏页面
# 难点：使用selenium就相当于是用代码来模拟用户操作了，但是每次登录个人收藏都需要输入账号、密码，我这里选用微博账号登录，实现过程比较有趣，主要是恰如其分利用了Handle
# 最后在StackOverflow上发现竟然无法用Keys来启动Console，卡住了……心塞……

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://www.tripadvisor.cn/Saves/755502')

# 选择微博登录
weibo = driver.find_element_by_xpath('//span[@id="WeiboConnect"]/span[@class="textContainer"]').click()

# 出现新的Window，不是弹窗！也不是模态框，就是一个window。获取新的window对象，切换到新的window上
handles = driver.window_handles
driver.switch_to.window(handles[1])

# 输入账号、密码
account = driver.find_element_by_id('userId')
account.send_keys('xxxxxxxx')
pwd = driver.find_element_by_id('passwd')
pwd.send_keys('xxxxxxxx')
driver.find_element_by_xpath('//div[@id="outer"]/div/div[2]/form/div/div[2]/div/p/a[1]').click()
driver.switch_to_window(handles[0])

# 这一步打不开，本来的想法是用document方法来获取数据的……
ActionChains(driver).send_keys(Keys.COMMAND + Keys.ALT + 'i').perform()
# ActionChains(driver).send_keys(Keys.F10).perform()
