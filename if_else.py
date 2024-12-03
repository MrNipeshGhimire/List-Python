# if else condition

print("Enter your age: ")
age = int(input())

if age >=16:
    print("Your are voter")
else:
    print("Not voter")


#if elif else

print("Enter num: ")
num = int(input())  #input() method le default string linxa

if(num > 10):
    print(f"{num} is greater than 10")
elif(num < 10):
    print(f"{num} is less than 10")
else:
    print(f"{num} is equal to 10")