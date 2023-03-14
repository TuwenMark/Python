from selenium import webdriver

# (1) 创建浏览器对象
path = 'msedgedriver.exe'
browser = webdriver.Edge(path)

# (2) 访问url
url = 'https://www.jd.com/?country=USA'
# url = 'https://www.baidu.com'
browser.get(url)

content = browser.page_source
print(content)


