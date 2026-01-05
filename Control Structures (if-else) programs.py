1. Write a Python program to check whether a number is positive, negative, or zero.

num=int(input("enter number: "))
if num>0:
    print("positive number")
elif num<0:
    print("negative number")
else:
    print("zero")


2. Write a program to find the largest among three numbers. 

a = float(input("enter first number: "))
b = float(input("enter second number: "))
c = float(input("enter third number: "))
if a>=b and a>=c:
    print ("largest number is first")
elif b>=a and b>=c:
    print ("largest number is second")
else:
    print("largest number is third")

3. Write a Python program to print all even numbers between 1 and 50.

for i in range(1, 51):
    if i%2==0:
        print(i)

4.  Write a Python program to print the sum of all numbers in a given range.

start = int (input("enter starting number: "))
end = int(input("enter ending number: "))
sum=0
for i in range(start, end+1):
    sum+=i
    print("sum of number from",start,"to",end,"is:",sum)

or

sum=0
for i in range (1,11):
    sum+=i
    print("sum of number from 1 to 10 is:",sum)

5. Write a program to check if a year is a leap year.

year = int(input("enter a year: "))
if (year%400==0) or (year%4==0 and year%100!=0):
    print(year,"is leap year")
else:
    print(year,"is not a leap year")

















