import requests, re

# 匹配所有符合正则的内容。返回列表
# lst = re.findall(r"\d+", "wode dianhuahaoshi 10086")

# finditer 返回迭代器，效率高于列表, 从迭代器中取得数据用.group()
# it = re.finditer() it 是callable iterator
# for i in it:
#     print(i)  i是match object
#     print(i.group())

# search返回match object， search是全文检索，只要存在第一个结果就返回
# s = re.search() s是match object，用.group()拿数据

# match是从头匹配
# s = re.match() s是match object，用.group()拿数据

# 预加载
# obj = re.compile(r"\d+") 内存里有obj，表示这一段正则
# obj.finditer()/findall/search都有
# res = obj.finditer("asdlfjalsdjflaksdfasdf")  res是迭代器callable iterator，用循环，.group()

# 从正则里拿到内容
# obj = re.compile(r"balblablabla(?P<name>.*?)", re.S) 特殊规则：re.S让.能够匹配换行符
# obj.finditer(str)----->> match object .group("name")
