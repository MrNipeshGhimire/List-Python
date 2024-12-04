list = ["apple","banana","orange"]

l = iter(list)

print(next(l))
print(next(l))
print(next(l))
list.append("kera")
print(next(l))


