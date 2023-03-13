from lxml import etree

tree = etree.parse('xpath.html')

print(tree)

# 获取内容
# li_list = tree.xpath('//ul/li/text()')

# 谓词查询
# li_list = tree.xpath('//li[@id="l1"]/text()')

# 属性查询
# li_list = tree.xpath('//li[@class="c2"]/text()')

# 模糊查询
# li_list = tree.xpath('//li[contains(@id, "l1")]/text()')
# li_list = tree.xpath('//li[starts-with(@id, "l")]/text()')

# 逻辑运算
# li_list = tree.xpath('//li[@id="l1" and @class="c1"]/text()')
li_list = tree.xpath('//li[@id="l1"]/text() | //li[@class="c2"]/text()')

print(len(li_list))
print(li_list)
