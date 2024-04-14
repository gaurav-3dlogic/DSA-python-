import json


a = '{"a": "apple", "b": "banana", "c": "kiwi"}'

y = json.loads(a)


print(y['b'])

