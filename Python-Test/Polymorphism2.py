#method overloading

class Human:
    def mobile(self,name=None):
        if name == "iPhone":
            print("ios")
        if name == None:
            print("Android")


obj = Human()

obj.mobile()
obj.mobile("iPhone")

