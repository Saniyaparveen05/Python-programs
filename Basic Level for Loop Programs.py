1. Write a program to print numbers from 1 to 20.
for i in range (21):
    print(i)


2. Print all even numbers between 1 and 50. 
for i in range (51):
    if i%2==0:
        print(i)


3. Print all odd numbers between 1 and 50.
for i in range (51):
    if i%2!=0:
        print(i)


4. Print the multiplication table of a given number (e.g., 7).
for i in range (1,11):
    a=7
    if  a*i:
        print(a*i)


5. Print the squares of numbers from 1 to 10. 
for i in range (1,11):
    if  i**2:
        print(i**2)


6. Calculate the sum of numbers from 1 to 100.
count=0
for i in range (1,101):
    count+=i
    print(count)


7. Calculate the sum of even numbers between 1 and 50.
count=0
for i in range (1,51):
    if i%2==0:
        count+=i
        print(count)


8. Calculate the sum of odd numbers between 1 and 50.
count=0
for i in range (1,51):
    if i%2!=0:
        count+=i
        print(count)








