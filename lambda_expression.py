# def myFun(n):
#     return lambda a:a *n

# fun = myFun(4)
# print(fun(5))

class Parent:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname 
    
    def printData(self):
        print(self.fname, self.lname)
    
class Child(Parent):
    def __init__(self, fname, lname):
        super().__init__(fname,lname)

c = Child("Hari", "Sharma")
c.printData()