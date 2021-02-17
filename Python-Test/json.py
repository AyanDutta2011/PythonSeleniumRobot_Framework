import json

x = '{"name":"Ayan Dutta", "Email":"ayand777@gmail.com", "age":24}'
y = json.loads(x)
print(y["age"])

a = {"name":"Aparna Dutta", "Email":"aparna@gmail.com", "age":50}
b = json.dumps(a)
c = json.loads(b)
print(c["age"])

#############################################################
import json

# Opening JSON file
f = open('data.json', )

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['emp_details']:
    print(i)

# Closing file
f.close()


