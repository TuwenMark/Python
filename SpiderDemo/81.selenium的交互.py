import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. 创建浏览器对象
path = 'msedgedriver.exe'
browser = webdriver.Edge(path)

# 2. 访问网页
url = 'https://www.baidu.com'
browser.get(url)

# 3. 输入“周杰伦”
text = browser.find_element(By.ID, 'kw')
text.send_keys('周杰伦')

time.sleep(2)

# 4. 点击“百度一下”
button = browser.find_element(By.XPATH, '//input[@id="su"]')
button.click()

time.sleep(2)

# 5. 滚到底部
js_script = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_script)

time.sleep(2)

# 6. 点击下一页
next = browser.find_element(By.CSS_SELECTOR, ".n")
next.click()

time.sleep(2)

# 7. 返回上一页并滚动到底部
browser.back()

time.sleep(2)

# 8. 回到下一页，并滚动到底部
browser.forward()

time.sleep(2)

# 9. 退出
browser.quit()
