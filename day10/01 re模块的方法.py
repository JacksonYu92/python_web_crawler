import re

# ret = re.findall("\d+", "apple 122 peach 34")
# print(ret)
# ret = re.search("\d+", "apple 122 peach 34")
# print(ret)
# print(ret.span())
# print(ret.group())

# 有名分组
# ret = re.search("(?P<tel>1[3-9]\d{9}).*?(?P<email>\d+@qq\.com)", "我的手机号码是13928835900,我的邮箱是123@qq.com")
# print(ret.group())
# print(ret.group("tel"))
# print(ret.group("email"))

# match
# ret = re.match("1[3-9]\d{9}", "13928835900,我的女朋友的手机号是12312312356")
# print(ret.group())
# print(ret.group())

# split
# txt = "my name       is yuan"
#
# print(txt.split(" "))
#
# ret = re.split(r"\s+", txt)
# print(ret)

# sub/subn
# print("12 34 56 88".replace("88", "yuan"))
#
# s = "12 34 56 88"
# ret = re.sub(r"\d+", "yuan", s, 2)
# print(ret)

# compile
# s1 = "12 apple 34 peach 77 banana"
# ret = re.findall(r"\d+", s1)
# print(ret)
#
# s2 = "22 apple 33 peach 44 banana"
# ret = re.findall(r"\d+", s2)
# print(ret)

# s1 = "12 apple 34 peach 77 banana"
# s2 = "22 apple 33 peach 44 banana"
#
# reg = re.compile(r"\d+")
#
# print(reg.findall(s1))
# print(reg.findall(s2))

# raw-string

print("hello jackson")

