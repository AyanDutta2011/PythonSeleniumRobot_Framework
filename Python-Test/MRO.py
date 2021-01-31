#Method Resolution Order always starts from left to right

class A:
    def __init__(self):
        print("Init of A")

    def feature1(self):
        print("feature1 of A")
    def feature2(self):
        print("feature2 of A")

class B:
    def __init__(self):
        print("Init of B")

    def feature1(self):
        print("feature1 of B")
    def feature2(self):
        print("feature2 of B")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("feature1 of C")

c1 = C()
c1.feature1()

