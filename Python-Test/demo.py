import json

f = open('demo.json', )
data = json.loads(f)

for i in data['name']:
    print(i)