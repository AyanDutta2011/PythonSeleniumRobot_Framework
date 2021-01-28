# method overloading
# define a method in such a way that there are multiple ways to call it.

class Human:
    def mobile(self,name=None):
        if name == "iPhone":
            print("ios")
        if name == None:
            print("Android")


obj = Human()

obj.mobile()
obj.mobile("iPhone")

