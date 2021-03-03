string = "B3A1C2"
print(string)

alp = []
ch = []

for i in string:
    if i.isalpha():
        alp.append(i)
    else:
        ch.append(i)

print(alp)
print(ch)

output = " ".join(sorted(alp) + sorted(ch))
print(output)