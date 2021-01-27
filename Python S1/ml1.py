import re
id = str("P00RE2-")
edit = str("B2Q")

regx = re.compile(id)
temp = ""
with open("C:\\ML\\18WWS2IK6AG.ini",'r') as f:
    newlines = []
    mystr = ""

    for "Build-ID=" in f.readlines():

        newlines.append(line.replace(rep, "zz"))

    for line in f.readlines():
        c = 0
        j = 0
        d = 0
        k = 0
        i = 0
        #rep    = id[7:11:]

        mystr = str(line)
        c = len(mystr)
        for char in line:
            i = i + 1
            if char == id[j]:
                j = j+1
                d=1
            else:
                d=0
            if j != 0 and d==0:
                break
            if j == len(id) :
                k=i
                break
        if id in line and j == len(id):
            temp = line[k:k+3:]
            newlines.append(line.replace(temp,edit,3))
        else:
            newlines.append(line)
with open("C:\\ML\\ZZ.ini", 'w') as f:
    for line in newlines:
        f.write(line)
