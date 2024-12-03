#Lists in python
# list and array are same in python

list = ["Hari","Ram","Shyam"]
print(list)

list.append("Padam")  #last ma add hunxa
print(list)

list.insert(1,"Raj")  #afulai ja man lago tei insert garna
print(list)

list.insert(3,"Manoj")

#sort list
list.sort()  #alphabetically sort garna
print(list)

#copy list

list2 = list.copy()
print(list2)

list3 = list + list2  #Joining two lists
print(list3)

list.pop(1)  #pop le item delete garxa
print(list)
