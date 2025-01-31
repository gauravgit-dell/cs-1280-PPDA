#1st practice question
n=5
for i in range (1, n + 1):
	for j in range(i):
		print("*",end="")
	print()
	
for i in range(n - 1, 0, -1):
	for j in range(i):
		print("*", end="")
	print()
	
#2nd practice question
a, b = 0, 1
n = int(input("enter the number of terms: "))
if n == 1:
    print(a)
elif n == 2:
    print(a)
    print(b)
else:
    print(a)
    print(b)
    count = 2
    while count < n:
        c = a + b
        print(c)
        a, b = b, c
        count += 1

#3rd practice question

def greet(name):
    print(f"Hello,{name}!")
    
greet ("alice")

def print_parameters(a,b,c):
    print("1st parameter:", a)
    print("2nd parameter:", b)
    print("3rd parameter:", c)

print_parameters(a=1, c=3, b=9)

#4th practice question
def outer_function():
    a=20   
    print("a=",a)
a=10
outer_function()
print("global value of a is = ",a)

#5th practice question

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else :
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
        
num = int(input("enter a number: "))
print(f"factorial of {num} is {factorial (num)}")

