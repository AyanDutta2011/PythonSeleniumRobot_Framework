foo = "P00U2W-B2R = Conexant High Definition Audio Driver for Slice 2.0"
rep = foo[-2:]
print(rep)
a = foo.replace(rep, "zz")
print(a)