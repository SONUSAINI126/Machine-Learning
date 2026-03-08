#question 1: Write a program to take your name and age as input and print it in the format below

name=input("Enter your name : ")
age = (int)(input("Enter your age : "))
print("Hello",name+", you are "+str(age)+" years old!")

#question 2: Take two numbers as input from the user and print their sum, difference,product, and quotient.

num1=(float)(input("Enter first number : "))
num2=(float)(input("Enter second number : "))
sum=num1+num2
difference=num1-num2
product=num1*num2
quotient=num1/num2
print("Sum :",sum)
print("Difference :",difference)
print("Product :",product)
print("Quotient :",quotient)

#question 3: Ask the user to enter two integers and one float. Convert them all to floats and print their average.

a=(float)(input("Enter 1st integer : "))
b=(float)(input("Enter 2nd Integer : "))
c=(float)(input("Enter a float number : "))
average=(a+b+c)/3
print("Average of the given numbers is ",average)

#question 4 : The user enters a string containing a number (e.g.,45 ). Convert it to:
'''• an integer
• a float
• a string again
Print all three values with their types.'''

num_str = input("Enter a number: ")     
num_int = int(num_str)                
num_float = float(num_str)               
num_string_again = str(num_str)
print("Integer value:", num_int, "| Type:", type(num_int))
print("Float value:", num_float, "| Type:", type(num_float))
print("String again:", num_string_again, "| Type:", type(num_string_again))

#  question 5 : Evaluate   10 + 3 * 2 ** 2
x=10 + 3 * 2 ** 2
print("Result is:",x)
'''
Because Python follows operator precedence:
** (exponent) → 2 ** 2 = 4
* (multiplication) → 3 * 4 = 12
+ (addition) → 10 + 12 = 22'''

# Question 6: Swap values of two numbers entered by the user

p = int(input("Enter first number: "))
q = int(input("Enter second number: "))

print("Before swapping: p =", p, "q =", q)
temp = p
p = q
q = temp
print("After swapping: p =", p, "q =", q)

#question 7 : Ask the user for a temperature in Celsius (string input). Convert it to ,then calculate and print temperature in Fahrenheit.Conversion formula: FahrenheitTemp = (CelsiusTemp ∗ (9/5)) +32

CelsiusTemp=(float)(input("Enter the temperature in celsius : "))
FahrenheitTemp = (CelsiusTemp*(9/5)) +32
print("Temperature in Fahrenheit is : ",FahrenheitTemp)

#question 8 :  Take the radius (r) as user input and print the area.Use the formula: Area = π * r2 (value of π = 3.14)

radius=(int)(input("Enter radius of the circle : "))
area=3.14*radius*radius
print("Area of the circle is : ",area)

#question 9 : Ask the user for: Principal (P), Rate (R), Time (T). Convert all to andcompute simple interest:
principle=(float)(input("Enter principle value : "))
rate=(float)(input("Enter rate of interest : "))
time=(float)(input("Enter time in years : "))

SI = (principle*rate*time)/100
print("Simple interest :",SI)


#question 10 : Take a decimal number as input (like 45.78) and output its:
'''• integer part -45
• fractional part -0.78'''
decimalnumber=(float)(input("Enter a floating number : "))
integerpart=(int)(decimalnumber)
fractionalpart=decimalnumber-integerpart
print("so the integer part of the given number is ",integerpart,"fractional part is ",fractionalpart)