#program1
str = "hello"
print(str)
str2 = "gaurav"
print(str2)

#program2
x = "python programming"
print(x[:])
print(x[0:])
print(x[2:5])
print(x[::-1])
print(x[-5:-3])
print(x[-6:-4])

#program3
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for index, name in enumerate(names):
    print(f"Index: {index}, Name: {name}")
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

#program4
import copy
list1 = [1, [2, 3], 4]
list2 = list1.copy() 
list3 = copy.deepcopy(list1) 
list1[0] = 10 
list1[1][0] = 20 
print("list1:", list1)
print("list2:", list2) 
print("list3:", list3) 

#program5
sum = 0
newlist = []
size = int(input('Enter size of the list: '))
for i in range(size):
    a = int(input('Enter a number: '))
    newlist.append(a)
for x in newlist:
    sum += x
print('Sum =', sum)

#program6
squares = [i * i for i in range(10)]
print(squares)

#program7
cubes = []
for i in range(1, 11):
    cubes.append(i ** 3)
print(cubes)

#program8
nums=[i for i in range(1, 21)]
print(nums)
