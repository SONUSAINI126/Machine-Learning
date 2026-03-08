#Conditional statements

age=(int)(input("Enter your age : "))

if (age>=18):
    print("you are eligible to vote ")
    print("you are adult ! ")
elif age>13 and age<18 :
    print("You are in Green zone")
    print("You are a teenager")
elif age>0 and age<13:
    print("You are in Red zone")
    print("You are a child")
else:
    print("Enter a valid age !\n ")

print("Hope this helped you !")


#Simple password and username example

username = input("Enter your username : ")
password = input("Enter your Password : ")

if username == "sonu" and password == "sonuspassword":
    print("Welcome", username)
elif username != "sonu" and password != "sonuspassword":
    print("Both username and password are incorrect")
elif username != "sonu":
    print("Wrong username! Enter the correct username")
else:
    print("Wrong password! Enter the correct password")

#checking the given number is multiple of 5 or not

n=(int)(input("Enter a number to check if multiple of 5 or not : "))
if n%5==0:
    print("congrats ! number is divisible by 5")
else:
    print("Number is not divisible by 5")


# Program for checking odd or even 

n=(int)(input("Enter a number to check if even or odd : "))
if n%2==0:
    print("Entered number is even")
else:
    print("Number is odd")

#Concept of nesting

username = input("Enter your username : ")
password = input("Enter your Password : ")

if username == "sonu" and password == "sonuspassword":
    print("Welcome", username)
else:
    if username != "sonu":
      print("Wrong Username ! Enter the correct username")
    else :
        print("Wrong password! Enter the correct password")


# Ternary Statement 


print("condition is true") if 5 else print("not satisfied")

# Match Case

'''The alternative to if-elif-else'''

color = input("Enter the traffic light color : ")
match color:
    case "green":
        print("You can go !")
    case "red":
        print("Stop !")
    case "yellow":
        print("Go Slow !")
    case _:
        print("Enter valid color")




#loops in Python

'''while loop'''

count =1  #iterator
while count<=5 :
    print("You are in while loop")
    count+=1

           #Example 2
i=1
while i<=5:
    print("Number is",i)
    i+=1

print("Out of the loop and i is : ",i)

        #Printing table of a given Number

number=(int)(input("Enter the number to print the table : "))
i=1
while(i<=10):
    print(number," X ",i," = ",number*i)
    i+=1



'''break and continue '''

i=1
while i<=10:
    if i==6:
        break
    print("Number is ",i)
    i+=1        
print("Out of the loop ",i)

i=0
while i<10:
    i+=1
    if i==6:
        continue
    print("Number is ",i)   
print("Out of the loop")


#for loop for sequencial traversal

'''  "in" the membership operator ->? to check presence '''

Name="Sonu"
if 'o' in Name: 
    print("o is present in the name")
    
for char in Name :
    print("characters in name are",char)

for a in range(10):
    print("numbers are",a)

word="Sonu Saini"
count=0
for ch in word:
    if ch=="S":
        count+=1

print("Number of S in Sonu Saini ",count)

# Counting no of vowels

wordcount = "artificial"
count = 0
for vowel in wordcount:
    if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u':
        count += 1
print("No of vowels in the", wordcount, "is :", count)

## range() function -> generate sequence
'''range(start [default(0)],stop(Compulsory),step [default=1])
    It returns an object not the number'''

for a in range(8):
    print(a)
for b in range(2,10):
    print(b)
for c in range(1,10,2):
    print(c)

#example Printing sum of first n natural numbers

n=(int)(input("Enter the value of n : "))
sum=0
for num in range(1,n+1) :
    sum=sum+num
print("Sum of first ",n, "natural numbers is ",sum)

## Functions in Python 

'''block of code that perform specific task
 it has two man components fuction definition[def] and function calling
 def func (non default parameter , default parameters ) '''

def greet():
    print("Hello User !")
    print("Welcome to the world of Python")
greet() 

def add(a,b):
    sum=a+b
    print("Sum is :",sum)       
add(5,10)

#Example printing average value of three numbers

def  average(a,b,c=5):
    avg=(a+b+c)/3
    return avg

print("Average of the given numbers is :",average(5,6))

# Types of function 
''' INbuilt and User defined function

#Lambda function
its usage is in higher order function that is used as a parameter in another function
lambda a,b,c : expression (a+b+c)'''

sum3 = lambda a, b, c: a + b + c
print(sum3(2, 3, 4))

# Finding factorial of a number

number = int(input("Enter the number to find the factorial: "))

def factorial(a):
    fact = 1
    for i in range(1, a + 1):
        fact *= i
    return fact

print("Factorial of the number", number, "is", factorial(number))
