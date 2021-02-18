import json

f = open("C:\\Users\HP\Desktop\Imp\demo.json", "r")

print(f.read())

b = json.load(f)

print(b["name"])

