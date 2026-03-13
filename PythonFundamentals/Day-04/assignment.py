#Q1 . 
'''Create a class with attributes account_number, owner_name,
and balance.Add methods to deposit, withdraw, and check balance.'''
class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def check_balance(self):
        return self.balance


ba1 = BankAccount(101, "Sonu", 5000)
print(ba1.check_balance())

ba1.deposit(2000)
print(ba1.check_balance())

ba1.withdraw(3000)
print(ba1.check_balance())

#Q2 

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def count_reviews(self):
        return len(self.reviews)

    def display_reviews(self):
        if not self.reviews:
            print("No reviews yet.")
        else:
            print("Reviews:")
            for review in self.reviews:
                print("-", review)

book = Book("The pYTHON", "sonu saini")

book.add_review("Amazing story!")
book.add_review("Loved the characters.")

print("Number of reviews:", book.count_reviews())
book.display_reviews()

#Q3. 
'''Create a class student with private attributes _name, _roll_no, and _marks.
Provide getter and setter methods with validation (e.g., marks cannot be
negative, roll number has to be between 1 & 100 & name cannot be empty)'''

class student:
    def __init__(self):
        self.__name=""
        self.__rollno=0
        self.__marks=0

    def setName(self,name):
        if(name==""):
            print("name cannot be empty")
        else:
         self.__name=name
    def getName(self):
        return self.__name


    def setMarks(self,marks):
        if(marks<0):
            print("marks cannot be negative")
        else:
         self.__marks=marks
    def getMarks(self):
        return self.__marks
    
    def setRollNO(self,rollno):
        if(rollno < 1 or rollno > 100):
            print("ENter valid roll no within 1,100")
        else:
         self.__rollno=rollno
    def getRollNO(self):
        return self.__rollno


s1 = student()
s1.setName("SonuSaini")
s1.setRollNO(10)
s1.setMarks(90)

print(s1.getName())
print(s1.getRollNO())
print(s1.getMarks())

#Q4 
''' Create a class Shape with a method area().
Create subclasses Circle , , and that override the area()
method'''

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14*self.radius*self.radius

class Rectangle(Shape):
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    
    def area(self):
        return self.length*self.breadth

class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def area(self):
        return 0.5*self.base*self.height

T1=Triangle(4,6)
print(T1.area())

R1=Rectangle(4,5)
print(R1.area())

C1=Circle(4.5)
print(C1.area())


#Q5
'''Create a base class Vehicle with attributes like brand and model.
Create two subclasses Car and Bike that add extra attributes - seats (in Car) &
engine_cc (in Bike).'''

class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
class Car(Vehicle):
    def __init__(self,brand,model,seats):
        super().__init__(brand,model)
        self.seats=seats

class Bike(Vehicle):
    def __init__(self,brand,model,engine_cc):
        super().__init__(brand,model)
        self.engine_cc=engine_cc

car1 = Car("Toyota", "Camry", 5)
bike1 = Bike("Yamaha", "R15", 155)

print(car1.brand, car1.model, car1.seats)
print(bike1.brand, bike1.model, bike1.engine_cc)

#Q6

from abc import ABC,abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def __init__(self, stipend):
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend

class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class ContractEmployee(Employee):
    def __init__(self,hour_worked,rate_per_hour):
        self.hour_worked=hour_worked
        self.rate_per_hour=rate_per_hour
    
    def calculate_salary(self):
        return self.hour_worked*self.rate_per_hour

emp1=FullTimeEmployee(30_000)
emp2=ContractEmployee(80,200)
emp3=Intern(8000)

print(emp1.calculate_salary())
print(emp2.calculate_salary())
print(emp3.calculate_salary())

#Q7
'''Create a class Person that allows the constructor to work with:
• name only
• name + age
• name + age + address
As direct cnstructor overloading (multiple constructors) are not allowed but
we have to use default parameters to simulate constructor overloading'''

class Person :
    def __init__(self,name=None,age=None,address=None):
        if(name==None and age==None and address== None ):
            print("No Parameters are Entered")

        elif(age == None and address== None):
            print("One parameter Constructor Name is ",name)
         
        elif(address==None):
            print("Two parameters Coonstructor Name is ",name," Age is ",age)

        else:
            print(f"3 Parameter Constructor Name is {name} Age is {age} and Address is {address} ")

p1=Person()
P2=Person("Sonu")
P3=Person("Sonu",19)
p4=Person("Sonu",19,"Hansi")


#Q8
class Player:
    player_count=0

    def __init__(self,name,level):
        self.name=name
        self.level=level
        Player.player_count+=1

    @classmethod
    def count_players(cls):
        return cls.player_count

p1=Player("Sonu",10)
p2=Player("Nikhil",24)

print(Player.player_count)
print(Player.count_players())

#Q9

class Herbivore:
    def __init__(self):
        self.herb_food = "Plants"

    def eat_plants(self):
        print("Eats plants")


class Carnivore:
    def __init__(self):
        self.meat_food = "Meat"

    def eat_meat(self):
        print("Eats meat")


class Omnivore:
    def eat_both(self):
        print("Eats both plants and animals")


class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self):
        Herbivore.__init__(self)
        Carnivore.__init__(self)

    def show_food(self):
        print("Bear food habits:")
        print(self.herb_food)
        print(self.meat_food)

b1 = Bear()
b1.eat_plants()
b1.eat_meat()
b1.eat_both()
b1.show_food()


#Q10

'''Mini Project - OOPs Chat System'''







