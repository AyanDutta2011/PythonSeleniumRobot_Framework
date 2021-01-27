class A:

    def __init__(self):
        print("For A")

    def feature1(self):
        print("1 is working...")

    def feature2(self):
        print("2 is working...")

class B(A):         #If child class doesn't have init method it will take from Super class by default

    def __init__(self):
        super().__init__()  # first it will execute B init, using Super we can access features of super class
        print("For B")

    def feature3(self):
        print("3 is working...")

#b1 = B()

#MRO = Method Resolution Order

class C:

    def __init__(self):
        print("For C")

    def feature1(self):
        print("C is working...")

class D(A,C):

    def __init__(self):
        super().__init__()
        print("For D")

    def feature1(self):
        print("D is working...")

d1 = D()

d1.feature1()   #From Left to Right it will start execute
