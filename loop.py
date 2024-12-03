#while loop

x =1
while x<10:
    print(x)
    x+=1


print("\nFor Loop ")
#for loop

x=0
for i in range(0,10):
    print(i)


#list items for loop 
print("\nList items iterate using for loop\n")

list = ['list1',"list2","list3","list4"]
for i in list:
    print(i)


#Nested for loop
product = [[1,2,3],[4,5,6],[1,2,34]]

for i in product:
    for j in i:
        print(j) 