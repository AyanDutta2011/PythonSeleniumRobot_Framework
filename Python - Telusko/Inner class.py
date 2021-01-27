
class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def show(self):
        print(self.name,self.roll)

    class Laptop:
        def __init__(self):
            self.brand = 'HP'

s1 = Student("Ayan", 2359915)

s1.show()

lap = Student.Laptop()