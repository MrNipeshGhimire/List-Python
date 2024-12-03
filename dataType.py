#Python Data Type

x = 3
print(type(x))  #integer type

y = 3.4
print(type(y))  #float 

name = "Arjun"
print(type(name))  #this is string type

p = 2j
print(type(p))  #complex

fruits = ["apple","banana","orange"]  #this is list  #python ma array lai list vaninxa
print(type(fruits))

fruits = {"apple","banana"}  #python ma object lai set bhaninxa
print(type(fruits))

#Dictionary

student = {
    "name" : "Ram",  #dictionary ma key and value hunxa for eg: name = key & Ram = value
    "age": 23,
    "address":"Itahari"
}
print(student)
print(type(student))

#tuple

name =("Ram","Shyanm","Hari")
print(name)
print(type(name))