# method overriding

class Bank():
    def roi(self):
        return 5

class HDFC(Bank):
    def roi(self):
        return 8

obj = HDFC()
obj1 = Bank()
c = obj.roi()
print(c)

p = obj1.roi()
print(p)



