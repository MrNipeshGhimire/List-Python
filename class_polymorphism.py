# Class Polymorphism

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def printData(self):
        print("Person")
    

class Student(Person):
    pass

class Doctor(Person):
    def printData(self):
        print("Check up Patient Health")


class Pilot(Person):
     def printData(self):
         print("Fly Plane")

s = Student("Nipesh",22)
d = Doctor("Hari",22)
p = Pilot("Ram",44)

for i in (s,d,p):
    print(i.name, i.age)
    i.printData()




    