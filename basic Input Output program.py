'''
1.Write a Python program to print "Hello, World!
print("Hello, world")

2.Write a Python program to take two integers as input and print their sum.
num1 = 100
num2 = 200
total = num1+num2
print("the sum is:",total)
       or
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
total = num1+num2
print("the sum is:",total)

3.Write a program to calculate the area of a rectangle.
length=float(input("enter the length of the rectangle:"))
width=float(input("enter the width of the rectangle:"))
Area=length*width
print("the area of the rectangle is:",Area)

4.Write a Python program to check if a number is even or odd.
num=int(input("enter a number:"))
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")

5.Write a Python program to take a string as input and print it in reverse order.
string = input("enter a string:")
for i in string[::-1]:
    print(i,end= '')

6.Write a Python program to convert temperature from Celsius to Fahrenheit.
celsius = int(input("Enter temperature in Celsius: "))
fahrenheit = (celsius*9/5)+32
print("temperature in fahrenheit:",fahrenheit)

7.Write a program to take a list of numbers and print their sum.
li = [21,47,25,67,37,75,32]
from functools import reduce
add = lambda a,b:a+b
result = reduce(add,li)
print(result)


8.Write a Python program to swap two variables without using a temporary variable.
a = 7
b = 5
a = a+b
b = a-b
a = a-b
print("a:",a)
print("b:",b)

9.Write a Python program to find the length of a string.
string = input("enter a string:")
print("The length of the string is:",len(string))


10.Write a program that reads an integer and prints its multiplication table.
num = int(input("enter a number:"))
for i in range(1,11):
    print(num*i)

'''


