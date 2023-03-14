import selenium.webdriver.common.by
from selenium import webdriver

# 获取浏览器对象
path = 'msedgedriver.exe'
browser = webdriver.Edge(path)

# 访问页面，获取数据
url = 'https://www.baidu.com'
browser.get(url)

# 元素定位并打印信息
button = browser.find_element(selenium.webdriver.common.by.By.XPATH, '//input[@id="su"]')
# print(button)
print(button.get_attribute('value'))
print(button.get_property('type'))
print(button.tag_name)
a = browser.find_element(selenium.webdriver.common.by.By.LINK_TEXT, '新闻')
print(a.text)
