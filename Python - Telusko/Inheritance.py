class A:
    def feature1(self):
        print("1 is working...")

    def feature2(self):
        print("2 is working...")

class B(A):     #Single Level
    def feature3(self):
        print("3 is working...")

class C(B):        #Multi level
    def feature4(self):
        print("4 is working...")
class E:        #Multi level
    def feature6(self):
        print("6 is working...")

class D(A,E):        #Multiple
    def feature5(self):
        print("5 is working...")

d1 = D()

d1.feature6()