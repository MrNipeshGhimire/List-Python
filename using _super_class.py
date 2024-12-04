# Using super() keyword

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printData(self):
        print(self.fname, self.lname)

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname,lname)

p = Student("Binayak", "Dhungana")
p.printData()