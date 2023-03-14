from bs4 import BeautifulSoup

# 获取本地文件对象
soup = BeautifulSoup(open('bs4.html', encoding='utf-8'), 'lxml')

# （1）根据标签名查找节点
# print(soup.a)
print(soup.a.attrs)
# print(soup.span.name)

# （2）函数
# print(soup.find('a'))
# print(soup.find_all('a'))
# print(soup.select('li')
# print(soup.select('.l1'))
# print(soup.select('#d1'))
# print(soup.select('li[class]'))
# print(soup.select('li[id="l1"]'))
# print(soup.select('div li'))
# print(soup.select('div>ul>li'))
# print(soup.select('li, a'))

# 节点信息
obj = soup.select('span')[0]
# print(obj.string)
# print(obj.get_text())
# print(obj.name)
# print(obj.attrs)
# print(obj.attrs.get('title'))
# print(obj.get('title'))
# print(obj['title'])