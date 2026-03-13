# 🧩 Day 04 – Object Oriented Programming (OOP) in Python

This folder contains my **Day 04 Python practice programs** focused on **Object Oriented Programming (OOP)** concepts.  
OOP helps organize code using **classes, objects, and reusable components**, which is widely used in real-world software development.

---

# 📚 Topics Covered

## 🔹 Classes and Objects
A **class** is a blueprint for creating objects, and an **object** is an instance of a class.

Example:

```python
class Student:
    Subject = "OOPs Using JAVA"
    Class = "BTECH"
    Year = "Final Year"

stu1 = Student()
print(stu1.Subject)
```

---

# 🏗 Constructors

Constructors are used to **initialize objects automatically**.

### Default Constructor

```python
class Student:
    def __init__(self):
        print("Constructor called")
```

### Parameterized Constructor

```python
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
```

---

# 🧠 Attributes

Two types of attributes:

| Type | Description |
|-----|-------------|
| Class Attribute | Shared by all objects |
| Instance Attribute | Unique for each object |

Example:

```python
class Student:
    college_name = "GJU"
```

---

# ⚙ Methods in Python

### Instance Method
Access both **class and instance attributes**.

### Class Method
Uses `@classmethod` and accesses **class variables only**.

### Static Method
Uses `@staticmethod` and **does not access class or instance variables**.

Example:

```python
@staticmethod
def cal_discount(price,discount):
    return price-(discount*price/100)
```

---

# 🧱 Pillars of OOP

## 1️⃣ Encapsulation
Wrapping **data and methods into a single unit** and controlling access.

Example:

```python
class Person:
    def __init__(self,name,salary):
        self.__salary = salary
```

---

## 2️⃣ Inheritance
Allows one class to **inherit properties from another class**.

Example:

```python
class Employee:
    pass

class Teacher(Employee):
    pass
```

### Types of Inheritance

- Single Level
- Multi Level
- Multiple

---

## 3️⃣ Abstraction
Hiding implementation details using **abstract classes**.

Example:

```python
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
```

---

## 4️⃣ Polymorphism

One interface with **multiple implementations**.

Types:

- Operator Overloading
- Function Overriding
- Duck Typing

Example:

```python
class Employee:
    def get_designation(self):
        print("Employee")

class Teacher:
    def get_designation(self):
        print("Teacher")
```

---

# 🧪 Practice Programs

Solved several OOP based practice problems:

1️⃣ Bank Account class with deposit, withdraw and balance checking  
2️⃣ Book review management system  
3️⃣ Student class with **private attributes and validation**  
4️⃣ Shape hierarchy with **area calculation using polymorphism**  
5️⃣ Vehicle inheritance example (Car and Bike)  
6️⃣ Employee salary calculation using **abstraction**  
7️⃣ Simulating **constructor overloading**  
8️⃣ Player counter using **class variables and class methods**  
9️⃣ Multiple inheritance example (Bear – Herbivore + Carnivore)  

---

# 🧑‍💻 Mini Project

## 💬 OOP Chat System

A mini chat system implemented using OOP concepts.

### Features

- Multiple users
- Multiple chat rooms
- Public messages
- Private messages
- Chat history tracking
- Join/leave chatroom functionality
- Timestamped messages

Classes used:

- `Message`
- `User`
- `ChatRoom`

---

# 💰 Additional Example

## Bank Account with Inheritance

Implemented:

- `Account` class
- `SavingsAccount` subclass
- Interest calculation

Example:

```python
class SavingsAccount(Account):
    def add_interest(self):
        interest=self.getBalance()*(self.rate/100)
        self.deposit(interest)
```

---

# 🎯 Learning Outcome

After completing this module I learned:

- Designing classes and objects
- Using constructors and attributes
- Writing instance, class and static methods
- Implementing OOP pillars
- Building small real-world projects using OOP

These concepts are essential for **scalable software design and advanced Python development**.
