# from bs4 import BeautifulSoup 第三方包 pip install bs4
# page = BeautifulSoup(resp.text, "html.parser")  指定html解析器
# 从bs对象拿数据
# find和find_all
# find找第一个，find_all找所有的

# find(标签，属性=值)
# find_all(标签，属性=值)

# table = page.find("table", class_ = "hq_table")  #class 是python的关键字，可以在class后面加一个下划线
# table = page.find("table", attrs = {"class":"hq_table"}) #一样的意思
# trs = table.find_all("tr")[1:]
# for tr in trs:
#     tds = tr.find_all("td")
#     tds[0].text  表示拿到被标签标记的内容
#     print(a.get("href")) 通过get直接可以拿到属性的值
# xml = """
# blablablablablablbal
# blablablablbalblabla
# """

# from lxml import etree
# tree = etree.XML(xml)
# tree = etree.parse(b.html)
# tree = etree.html(resp.text)

# result = tree.xpath("/book/name/text()")  text()拿标记的文本
# result = tree.xpath("/book/author//nick/text()")  //找所有的后代
# result = tree.xpath("/book/author/*/nick/text()")  *：通配符，任意的节点
# result = tree.xpath("/book/name[1]/text()")  text()拿标记的文本,[]表示索引
# result = tree.xpath("/book/name[@href = "blabla"]/text()")  text()拿标记的文本,@href取属性
# li.xpath("./a/@href") 相对路径


