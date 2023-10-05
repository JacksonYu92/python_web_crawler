import re

s = "666.tool.chinaz.com|888; china"

# ret = re.findall("china", s)
# ret = re.findall("\d+", s) #['666', '888']
# ret = re.findall("\w+", s) #['666', 'tool', 'chinaz', 'com', '888', 'china']
ret = re.findall("[a-z]+", s) #['tool', 'chinaz', 'com', 'china']
print(ret)