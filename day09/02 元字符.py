import re
"""re.findall(正则模式, 文本)  基于正则模式查找所有匹配的文本内容"""
# part1: 通配符->.  字符集-> []
# ret1 = re.findall("a", "a,b,c,d,e")
# ret1 = re.findall(".", "a,b,c,d,e")
# ret1 = re.findall("a.b", "a,b,c,d,e, acb,ab, abb, a\nb, a\tb")
# ret1 = re.findall("[ace]", "a,b,c,d,e")
# ret1 = re.findall("a[bce]f", "af,abf,abbf,acef,aef")
# ret1 = re.findall("[a-z]", "a,b,c,d,e")
# ret1 = re.findall("[a-zA-Z]", "a,b,c,d,e,A,B")
# ret1 = re.findall("[0-9]", "1,2,3,4,5")
# ret1 = re.findall("\d", "1,2,3,4,5")
# ret1 = re.findall("[a-zA-Z0-9]", "a,b,2,d,6,8,B,C")
# ret1 = re.findall("\w", "a,b,2,d,6,8,B,C")
# ret1 = re.findall("[0-9a-z]", "1,a,2,b,3")
# ret1 = re.findall("[^a-z]", "1,a,2,b,3")
# ret1 = re.findall("[^0-9,]", "1,a,2,b,3")
# print(ret1)

# part2:重复元字符-> + * {} ?
# ret2 = re.findall("\d", "a,b,234,d,6,888")   #['2', '3', '4', '6', '8', '8', '8']
# ret2 = re.findall("\d\d", "a,b,234,d,6,888")   #['23', '88']
# ret2 = re.findall("\d+", "a,b,234,d,6,888") #['234', '6', '888']
# ret2 = re.findall("\d+?", "a,b,234,d,6,888")
# ret2 = re.findall("[0-9a-zA-Z]", "apple,banana,orange,melon")
# ret2 = re.findall("\w", "apple,banana,orange,melon")
# ret2 = re.findall("\w+", "apple,banana,orange,melon")
# ret2 = re.findall("\w+?", "apple,banana,orange,melon")  # 取消贪婪匹配
# ret2 = re.findall("\w*", "apple,banana,orange,melon")
# ret2 = re.findall("abc*", "abc,abcc,abe,ab")
# ret2 = re.findall("\w{6}", "apple,banana,orange,melon")
# print(ret2)

# part3: 位置元字符-> ^ $
# ret3 = re.findall("^\d+", "peach,34,banana,255,orange,65536")
# ret3 = re.findall("\w+$", "peach,34,banana,255,orange,65536")
# ret3 = re.findall("/goods/food/\d+", "/goods/food/1001")
# ret3 = re.findall("/goods/food/\d+", "app01/goods/food/1001")
# ret3 = re.findall("/goods/food/\d+", "app01/goods/food/1001/aaa/bbb")
# ret3 = re.findall("^/goods/food/\d+$", "app01/goods/food/1001/aaa/bbb")
# ret3 = re.findall("^\w{5}", "apple,banana,peach,orange,melon")
# ret3 = re.findall("\w{5}$", "apple,banana,peach,orange,melon")
# ret3 = re.findall("^\w{5}$", "apple,banana,peach,orange,melon")
# print(ret3)

# part4:
# | 指定原子或正则模式进行二选一或多选一
# () 具备模式捕获的能力，也就是优先提取数据的能力，通过(?:) 可以取消模式捕获
# ret4 = re.findall(",\w{5},", ",apple,banana,peach,orange,melon,")  # 筛选出5个字符的单词
# ret4 = re.findall("\w{5}", ",apple,banana,peach,orange,melon,")
# ret4 = re.findall(",(\w{5}),", ",apple,banana,peach,orange,melon,")  # 筛选出5个字符的单词
# ret4 = re.findall(",(?:\w{5}),", ",apple,banana,peach,orange,melon,")

# ret4 = re.findall("\w+@163.com", "123abc@163.com,....234xyz@qq.com,....")
# ret4 = re.findall("\w+@\w+\.com", "123abc@163.com,....234xyz@qq.com,....")
# ret4 = re.findall("(\w+)@qq\.com", "123abc@163.com,....234xyz@qq.com,....")
# ret4 = re.findall("(?:\w+)@(?:qq|163)\.com", "123abc@163.com,....234xyz@qq.com,....")
# print(ret4)

# part5:  转义符-> \d \D  \w \W      \n    \s \S  \b \B
""" \b 1个单词边界原子 """
# ret = re.findall("\(abc\)", "(abc)....")
txt = "my name is nana. nihao,nana"
# ret = re.findall(r"na", txt)
# ret = re.findall(r"\bna", txt)
ret = re.findall(r"\bna\w{2}", txt)
print(ret)  # ['na', 'na', 'na']