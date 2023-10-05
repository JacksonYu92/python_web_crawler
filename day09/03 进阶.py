import re

# text = '<12> <xyz> <!@#$%> <1a!#e2> <>'
#
# ret = re.findall("<\d+>", text)
# ret = re.findall("<\w+>", text)
# ret = re.findall("<.+>", text)
# ret = re.findall("<.+?>", text)
# ret = re.findall("<.*?>", text)

# print(ret)


text = """
<12
>

 <x
 yz> 

 <!@#$%> 

 <1a!#
 e2> 

 <>
"""

# ret = re.findall("<.*?>", text)
ret = re.findall("<.*?>", text, re.S)

print(ret)