# to restrict access to method and variables. Making private
# private methods can be access only within method

class myClass:
    def __display(self):
        print("Ayan")
    def display2(self):
        print("Dutta")
        self.__display()

obj = myClass()

#obj.__display()   #not correct

obj.display2()