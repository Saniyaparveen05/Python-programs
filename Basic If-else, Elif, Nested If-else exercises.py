1. Write a program to check if a given number is positive.
num=int(input("enter a number: "))
if num>0:
    print("positive number")


2. Write a program to check if a number is even. 
num=int(input("enter a number: "))
if num%2==0:
    print("Even number")

3. Write a program to check if a person is eligible to vote (age ≥ 18). 
age=int(input("enter a age: "))
if age>=18:
    print("eligible to vote")
else:
    print("not eligible to vote")


4. Write a program to check whether a number is even or odd. 
num=int(input("enter a number: "))
if num%2==0:
    print("Even number")
else:
    print("Odd number")

5. Write a program to check whether a person can drive (age ≥ 18), else print “Not eligible”.
age=int(input("enter a age: "))
if age>=18:
    print("Eligible")
else:
    print("Not eligible")


6. Write a program to check if a number is positive, negative, or zero. 
num=int(input("enter a number: "))
if num>0:
    print("positive number")
elif num<0:
    print("negative number")
else:
    print("zero")


7. Write a program to check if a student passed or failed (pass marks = 40). If passed, 
check if the student got first division (marks ≥ 60).
marks=int(input("enter marks: "))
if marks>=60:
    print("pass,first division")
elif marks>=40:
    print("pass")
else:
    print("fail")


8. Write a program to print the grade of a student based on marks: 
• 90 and above → A 
• 75–89 → B 
• 50–74 → C 
• Below 50 → Fail

marks=int(input("enter marks: "))
if marks>=90:
    print("A grade")
elif 75<= marks<=89:
    print("B grade")
elif 50<= marks<=74:
    print("C grade")
else:
    print("fail")


9. Write a program to check whether a given day number (1–7) is Monday, Tuesday … 
Sunday. 
num=int(input("enter number: "))
if num==1:
    print("Monday")
elif num==2:
    print("Tuesday")
elif num==3:
    print("Wednesday")
elif num==4:
    print("Thursday")
elif num==5:
    print("Friday")
elif num==6:
    print("Saturday")
elif num==7:
    print("Sunday")
else:
    print("wrong entered")


10. Write a program to calculate ticket price based on age: 
• Children (< 12) → 50 
• Teenagers (12–17) → 100 
• Adults (18–59) → 150 
• Seniors (60+) → 80 
age=int(input("enter age: "))
if age<=12:
    print("the price is 50rs")
elif 12<=age<=17:
    print("the price is 100rs")
elif  18<=age<=59:
    print("the price is 150rs")

else:
    print("the price is 80rs")









    

