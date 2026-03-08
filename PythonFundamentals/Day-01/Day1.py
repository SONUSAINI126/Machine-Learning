##Printing in Python 

print("Sonu Saini")
print("This is on next line")
print("first","second are on same line")
print (" this is using backspace for \n next line ")

##Variables(IDentifiers) in Python 

# python is case sensitive language 
name="SONU"
My_age=30
PI=3.14
print(" MY Name is : ",name,"\n Age is :",My_age,"\n Value of PI is :",PI)


##Data Types in Python
name="SONU"
My_age=30
PI=3.14
Learning_Python = True
isfilled = None
print("Type of My Age :",type(My_age))
print("Type of Name : ",type(name))
print("Type of PI: " ,type(PI))
print(type(Learning_Python))
print(type(isfilled))

##  Comment in Python 
# -> THis is Single line Comment 

''' -> This is Multi
     Line 
     comment 
'''
#Style Guide 
sonu_saini="snake_case, Preffered for variables and functions"
sonuSaini="camelCase"
SonuSaini="PascalCase"


#Operators in Python

''' Arithmetic Operators : + , - , * , / , % , ** , '''
a=5
b=10
sum=a+b
sub=a-b
mul=a*b
div=b/a
modulo=b%a
power=b**a
print("Sum :",sum,"\nSub :",sub,"\nMul :",mul,"\nDivision: ",div,"\nModulo: ",modulo,"\nPower: ",power)

'''Relational Operators :  > , < , >= , <= , == , != '''
x=15
y=10
print("x > y :",x>y)
print("x < y :",x<y)
print("x >= y :",x>=y)
print("x <= y :",x<=y)
print("x == y :",x==y)
print("x != y :",x!=y)

''' Logical Operators : and , or , not '''

p=True
q=False
print("p and q :",p and q)
print("p or q :",p or q)
print("not p :",not p)
print("not q :",not q)


''' Assignment Operators : = , += , -= , *= , /= , %= , **= '''

m=20
n=5
m+=n  # m=m+n
print("m after m+=n :",m)
m-=n  # m=m-n
print("m after m-=n :",m)          
m*=n  # m=m*n
print("m after m*=n :",m)
m/=n  # m=m/n
print("m after m/=n :",m)
m%=n  # m=m%n
print("m after m%=n :",m)
a**=b  # m=m**n
print("m after a**=b :",a)

''' Membership Operators : in , not in '''

str="Hello Sonu Saini"
print("Sonu in str :", "Sonu" in str)
print("Sonu not in str :", "Sonu" not in str)
print("Hello in str :", "Hello" in str)
print("World not in str :", "World" not in str)

#Operator Precedance in Python

'''
1. Parentheses ()
2. Exponentiation (**)
3. Multiplication, Division, Modulus (*, /, %)
4. Addition, Subtraction (+, -)
5. Relational Operators (>, <, >=, <=, ==, !=)
6. Logical Operators (not
7. and
8. or)
9. Assignment Operators (=, +=, -=, *=, /=, %=, **=)
'''
result=3 + 5 * 2 ** 2 - (4 / 2)
print("Result of the expression is :",result)

#type conversion & Castingin Python

int_var=10
float_var=5.5
str_var="20"
#Implicit Conversion (Type Conversion)
result1=int_var + float_var
print("Result after Implicit Conversion :",result1)
#Explicit Conversion (Type Conversion)
str_to_int=int(str_var)
print("String to Integer after Explicit Conversion :",str_to_int)

#Input in Python

'''by default input function takes input as string'''

name=input("Enter your name : ")
age=input("Enter your age : ")
print("Hello",name,"! You are",age,"years old.")

s=input("Enter a number : ")
t=input("Enter another number : ")
this_is_concatenation=s+t
print("Concatenation of s and t is :",this_is_concatenation)
result=int(s)+int(t)
print("Sum of s and t after Explicit Conversion :",result)

#Printing Average of 2 numbers
num1=float(input("Enter first number : "))
num2=float(input("Enter second number : "))
average=(num1+num2)/2
print("Average of the two numbers is :",average)