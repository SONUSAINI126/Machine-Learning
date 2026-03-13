# 📘 Day 03 – Strings & Python Data Structures

This file contains my **Day 03 practice code** while learning Python.  
Today I practiced **Strings, Lists, Tuples, Dictionaries, Sets and Problem Solving**.

---

# 🔤 Strings in Python

A **string** is a sequence of characters enclosed in quotes.

## Topics Covered
- String length using `len()`
- String concatenation
- String indexing
- Iterating through characters
- String slicing
- String immutability

### Example

```python
word = "Python"
print(len(word))
print(word[0])
print(word[2:5])
```

---

# 🧾 String Formatting

String formatting allows inserting variables into strings.

## Methods Learned

### 1️⃣ format() method

```python
a = 5
b = 10
print("Sum of {} and {} is {}".format(a,b,a+b))
```

### 2️⃣ Index Based Formatting

```python
print("Sum is {2} of {0} and {1}".format(a,b,a+b))
```

### 3️⃣ Value Based Formatting

```python
print("values of vars {a} & {b}".format(a=5,b=10))
```

### 4️⃣ F-Strings

```python
print(f"Sum of {a} and {b} is {a+b}")
```

---

# 📋 Lists

Lists are **mutable sequences of elements**.

```python
marks = [34,53,56,33,56,54]
```

## List Operations

- Access elements
- Update elements
- Slicing
- Loop through list

## List Methods

| Method | Description |
|------|------|
| append() | Adds element at end |
| insert() | Insert element at index |
| sort() | Sorts list |
| reverse() | Reverses list |

---

# 🔗 Tuples

Tuples are **immutable sequences**.

```python
tup = (1,2,3,4)
```

## Tuple Methods

- `index()` → returns index of first occurrence  
- `count()` → returns total occurrences  

---

# 📖 Dictionaries

A dictionary stores **data in key-value pairs**.

```python
info = {
    "name": "Sonu",
    "CGPA": 9.8,
    "subjects": ["Maths","Science"]
}
```

## Dictionary Methods

- `keys()`
- `values()`
- `items()`
- `get()`
- `update()`

---

# 🧩 Sets

A set is a **collection of unique elements**.

```python
myset = {1,2,3,4}
```

## Set Methods

- `add()`
- `remove()`
- `clear()`
- `pop()`

## Set Operations

- `union()`
- `intersection()`

---

# 🧪 Practice Problems Solved

### ✔ Problem 1
Check whether a string is a **Palindrome**

### ✔ Problem 2
Calculate **average of numbers in a list**

### ✔ Problem 3
Merge two lists and sort them

### ✔ Problem 4
Create tuple of **even and odd numbers**

### ✔ Problem 5
Menu driven **student marks dictionary program**

### ✔ Problem 6
Create dictionary mapping **word → length**

### ✔ Problem 7
Count **spaces in a string**

### ✔ Problem 8
Check whether **two lists share common elements**

### ✔ Problem 9
Find **duplicate elements in list**

### ✔ Problem 10
Print **unique characters in string**
