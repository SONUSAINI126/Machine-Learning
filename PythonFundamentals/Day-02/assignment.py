#Q1 Write a program that takes Salary as input. Using conditional statements,
'''calculate the final tax rate based on these rules:
• If salary < 30,000 → 5%
• If salary is 30,000–70,000 → 15%
• If salary > 70,000 → 25%'''

salary=(int)(input("Enter the salary : "))
if salary < 30000 : 
    tax=0.05*salary
    print("The tax to be paid is : ",tax)
elif salary >= 30000 and salary <= 70000:
    tax=0.15*salary
    print("The tax to be paid is : ",tax)
else:
    tax=0.25*salary
    print("The tax to be paid is : ",tax)

#q2 Write a function that takes two integers and and prints all even numbers between them (inclusive)

a=(int)(input("Enter the first number : "))
b=(int)(input("Enter the second number : "))
for num in range (a,b+1):
    if num % 2==0 :
        print(num)

#q3 Write a function that prints the digit of a number 

number = int(input("Enter the digit : "))

def digits(n):
    while n != 0:
        digi = n % 10
        print("digits of the number are :", digi)
        n //= 10  # integer division

digits(number)

# Q4 - Count number of digits in n

def noofdigits(n):
    count = 0
    while n != 0:
        count += 1
        n //= 10
    return count

number = int(input("Enter the Number : "))
result = noofdigits(number)
print("Number of digits are:", result)

#Q5 write a function to return the  sum of a number

number = int(input("Enter the number : "))
def Sumofnumbers(n):
    s = 0
    while n != 0:
        s += n % 10
        n //= 10
    print("Sum of the digits of the given number is :", s)
Sumofnumbers(number)

#Q6 Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5

print("Numbers that are divisible y both 3 and 5 from 1 to 100 are : ")
for i in range(1,101):
    if i%3==0 and i%5==0 :
        print(i)


#Q7 Continuously input number and check if positive or negative
choice = 1

while choice != 0:
    number = int(input("Enter the number: "))
    
    if number < 0:
        print("Entered number is negative.")
    else:
        print("Entered number is positive.")
    
    choice = int(input("Do you want to continue? Enter 1 for Yes / 0 for No: "))

#Q8  create a Simple that performs arithmetic operations.

''' Create a function that performs addition, subtraction,
multiplication, or division based on the parameter.
calculator(a, b, operation)
[ parameter can have values , , & .operation ‘+’ ‘-’ '*’ ‘/’''' 
 
a=(int)(input("Enter the 1st number :"))
b=(int)(input("Enter the second number : "))
operation=(input(" Choose the operation you want to perform : ‘+’ ‘-’ '*’ ‘/’ : "))
def calculator(p,q,operation) :
    if operation=='+':
        print("Sum is ",p+q)
    elif operation=='-':
        print("Difference is ",p-q)
    elif operation=='*':
        print("Product is ",p*q)
    elif operation=='/':
        print("Division is ",p/q)
    else :
        print("Enter valid choice")

calculator(a,b,operation)

#Q9 Write a function is_prime(n) that returns TRUE if is a prime number and false otherwise

def isPrime(a):
    flag = 0
    for i in range(2, a):
        if a % i == 0:
            flag += 1
            print("Divisor:", i)

    if flag == 0:
        print("Prime Number")
    else:
        print("Not a Prime Number (total divisors:", flag, ")")

n = int(input("Enter the number: "))
isPrime(n)

#Q10 write a program that asks the user to guess it and prints:

flag=1
while flag !=0 :
 guess=89
 user =(int)(input("Guess the number: "))
 if user > guess :
    print ("Guessed number is greater !")
 elif user < guess :
    print ("Guessed number is less !")
 else :
    print ( "Congrats ! You guessed it Right ")
    flag=0



a = "hello"
myinput = input("Enter letters to replace from the end: ")

n = len(myinput)   # n IS defined here
print(n)
a = a[:-n] + myinput
print(a)
