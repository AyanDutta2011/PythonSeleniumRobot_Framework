SearchMe = "The apple is red and the berry is blue!"
print(SearchMe.find("is"))
print(SearchMe.rfind("is"))
print(SearchMe.count("is"))
print(SearchMe.startswith("The"))
print(SearchMe.endswith("The"))
print(SearchMe.replace("apple", "car"))


word = "is"
if word in SearchMe:
    print("Pass")

s = "0123456789"

print("Even:", s[0::2])
print("Odd", s[1::2])

i = 0
print("Even")
while i < len(s):
    print(s[i])
    i = i + 2

i = 1
print("Even")
while i < len(s):
    print(s[i])
    i = i + 2


