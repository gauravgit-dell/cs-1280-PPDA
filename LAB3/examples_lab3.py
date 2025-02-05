#example1
text=input("enter a string ")
for char in text:
    print(char,end=" " )

#example2
text = input("Enter a string: ")
def is_palindrome(string):
    left, right = 0, len(string) - 1
    while right >= left:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True
print(is_palindrome(text))

#example3
import time, sys
start = time.time()
squares = [x ** 2 for x in range(1,1000001)]
end = time.time()
print("List comprehension time:",end - start)
print(sys.getsizeof(squares)) 

start = time.time()
squares = []
for x in range(1, 1000001):
    squares.append(x ** 2)
end = time.time()
print("For loop time:", end -start)
print(sys.getsizeof(squares))
