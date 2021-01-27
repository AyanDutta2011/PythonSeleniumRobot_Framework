#id = input("Enter id of Part no")
#edit = input("Enter build of Part no")

with open("C:\\ML\\18WWS2IK6AG.ini",'r') as f:
    newlines = []
    for line in f.readlines():
        newlines.append(line.replace('ZRS', 'Orange'))
with open("C:\\ML\\ZZ.ini", 'w') as f:
    for line in newlines:
        f.write(line)

