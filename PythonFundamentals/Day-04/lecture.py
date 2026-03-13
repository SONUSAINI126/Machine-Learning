#Classes and Objects 

class Student:
    Subject ="OOPs Using JAVA"
    Class = "BTECH"
    Year = "Final Year" #attribute 
    # and can have behaviour (methods=function inside class)

 
stu1=Student()
stu2=Student()
stu3=Student()

stu1.Subject="mysubject"
print(stu1.Subject,stu1.Class,stu1.Year)
print(stu2.Subject,stu2.Class,stu2.Year)
print(stu3.Subject,stu3.Class,stu3.Year)

## Methods in a class 

# __init__Method (Constructor)
'''initialize an object 
in python we cant create multiple constructors 
for each class we should have only one constructor'''

#default constructor

class Student1:
    def __init__(self):
        print("Constructor was called automatically")
student1=Student1()
student2=Student1()

# Parameterized Constructor

class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def get_name(self):
        return self.name
   
student3=Student("Sonu",101)
student4=Student("Lalit",102)

print("Student Name :",student3.name)
print("Student Roll No :",student3.rollno)  
print("Student Name :",student4.name)
print("Student Roll No :",student4.rollno)

print(student3.get_name())


#attributes
'''class attributes -> belong to class same for object 
    instance attributes -> belong to object
    when both have the same name to class and object that is self then the instance valle ki high priority'''

class Student:
    college_name="GJU"

    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa

stu1 = Student("Sonu Saini ",99)
print(Student.college_name,stu1.name,stu1.gpa)

stu2 = Student("Lalit ",98)
print(stu2.college_name,stu2.name,stu2.gpa)

# methods in python 

# Instance method 
''' have the self parameter as the first parameter
and they can access instance as well as class variables '''

class Laptop:

    storage_type = "ssd"   # class variable

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage
    
    # instance method
    def get_info(self):
        print(f"Laptop has {self.RAM}GB RAM and {self.storage}GB {self.storage_type}")
    
    # class method 
    '''It has the first parameter as cls -> refering to class
    it can only access class attributes and NOT the instance attributes
    decorator @classmethod -> used to make a method as class method'''
    
    @classmethod
    def get_storage_type(cls):
        print(f"Storage type : {cls.storage_type}")

    @staticmethod
    def cal_discount(price,discount):
        final_price=price-(discount*price/100)
        print(f"Discounted Price= {final_price}")


L1 = Laptop(8, 512)
L2 = Laptop(16, 512)

L1.get_info()
L2.get_info()
L1.get_storage_type()   # works, but better to call using class name
# Laptop.get_storage_type()
L1.cal_discount(40_000,10) #underscores are ignored in numbers

#Static method 

'''no compulsory parameter and also 
no need for self and cls attribute
cant access class as well as instance attribute
@staticmethod is the decorator used here '''

#Question 
'''Design and create an online store for Products(name,Price).
Track total products being created.
Create a static method to calculate discount on each product based on a % parameter'''

class Products:
    count=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        Products.count+=1 

    def get_Info(self):
        print(f"price of {self.name} is {self.price}")
    
    @classmethod
    def total_pr(cls):
        print(f"Total products created are {cls.count}")
    
    @staticmethod
    def getdiscount(price,discount):
        print(f"final price is {price-(discount*price/100)}")

p1=Products("Laptop",40_000)
p2=Products("Iphone",1_00_000)
p3=Products("Maruti",20_00_000)

p1.get_Info()
Products.total_pr()
p1.getdiscount(p1.price,10)


# Pillars of OOPs 

#Encapsulation in Java
'''wrapping data and functions into a single unit
we can also do data hiding using it 

public-> inside and outside the class (default)

protected-> class and in subclass

class Person:
    def __init__(self,name,salary):
        self.name=name
        self._salary = salary #setted as protected
print(f"{p1.name} {p1._salary}") --> accessible outside
this is not inforced in python but a convension 

private-> only inside the class
data mangling

class Person:
    def __init__(self,name,salary):
        self.name=name
        self._salary = salary #setted as protected
print(f"{p1.name} {p1._Person.__salary}") --> accessible outside

 '''
  
class Person:
    def __init__(self,name,salary):
        self.name=name
        self.__salary = salary #setted as private

    def getSalary(self):
        return self.__salary

p1=Person("Sonu",1_00_00_000)

print(f"{p1.name} {p1.getSalary()}")


#Inheritance 

class Employee:
    start_time="7am"
    end_time="5pm"
    def __init__(self,Name,Subject):
       self.Name=Name
       self.Subject=Subject

class Student(Employee): 
    pass

class Teacher(Employee):
    pass 

S1=Student("Sonu Saini","Mathematics")
print(S1.start_time)
print(S1.Name)

#Types of Inheritance 
'''Single Level Inheritance 
    MUlti Level Inheritance 
    Multiple Inheritance
    '''

#Multilevel Inheritance 

class Employee:
    start_time="10am"
    end_time="6pm"

class AdminStaff(Employee):
    def __init__(self , role):
        self.role=role

class Accountant(AdminStaff):
    def __init__(self,role,salary):
        super().__init__(role)
        self.salary=salary

acc1=Accountant("Major",25_000)
print(acc1.role,acc1.salary,acc1.start_time,acc1.end_time)

#Multiple Inheritance 

class Teacher :
    def __init__(self,salary):
        self.salary=salary

class Student:
    def __init__(self,gpa):
        self.gpa=gpa

class TA(Teacher,Student):
    def __init__(self,gpa,salary,name):
    
        Student.__init__(self,gpa)
        super().__init__(salary)
        self.name=name

Phd1 = TA(9.4,50_000,"SONU")
print(Phd1.gpa,Phd1.name,Phd1.salary)

#<--abstraction-->
# Hiding some and showing  other details -> in abc module it is present 

from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("ROAR !!")

class Cat(Animal):
    def make_sound(self):
        print("moew")


lion=Lion()
lion.make_sound()



 ##   <--  Polymorphism  -->

'''many forms multiple functions with same name
Operator Overloading 
+ -> String Concatenation and for maths addition '''

    #Function Overriding 
'''redefining parent class function in child class '''

class Employee:
    def get_designation(self):
        print("designation  = employee ")

class Teacher :
    def get_designation(self):
        print("Designation = Teacher")

E1=Employee()
E1.get_designation()
T1= Teacher()
T1.get_designation()

    #Duck Typing 
'''Duck typing = behavior-based typing, not class-based typing
Python checks what an object can do, not what it is.'''



