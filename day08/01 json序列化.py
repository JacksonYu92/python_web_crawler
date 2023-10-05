import json

# json.dumps()
# json.loads()

# data = {
#     1001: {"name": "yuan"},
#     1002: {"name": "rain"},
# }
#
# dataJson = json.dumps(data)
# # print(dataJson)
# print(dataJson,type(dataJson))
# print(repr(dataJson))

data = '{"1001": {"name": "yuan"}, "1002": {"name": "rain"}}'
res = json.loads(data)
print(res)
