# 📂 Day 05 – File Handling, Exceptions, List Comprehension & JSON in Python

This folder contains my **Day 05 Python practice programs**.  
Today I explored **File Handling, Exception Handling, List Comprehension, and the JSON module**, which are essential for real-world Python applications such as data processing, automation, and backend development.

---

# 📚 Topics Covered

## 📁 File Handling in Python

File handling allows Python programs to **read, write, append, and manage files** stored on the system.

### Basic File Operations

```python
f = open("sample.txt","r")
data = f.readline()
print(data)
f.close()
```

### Writing to a File

```python
f = open("sample.txt","a")
f.write("\nThis is the appended text")
f.close()
```

---

# 📌 File Modes

| Mode | Description |
|-----|-------------|
| r | Read file |
| w | Write file (overwrites content) |
| a | Append data to file |
| x | Create a new file |
| rb | Read in binary |
| wb | Write in binary |
| r+ | Read & write from start |
| w+ | Write & read (clears file) |
| a+ | Append & read |

---

# 🔐 Using `with` Keyword

The `with` keyword automatically **closes the file after use**, which is safer.

```python
with open("sample2.txt","r") as f:
    data = f.read()
    print(data)
```

---

# 🗑 Deleting Files

Using the **OS module** to delete files.

```python
import os
os.remove("sample.txt")
```

---

# 🔎 Searching for a Word in File

Program to **search a word and print its line number**.

```python
with open("sample2.txt","r") as f:
    word = input("Enter word to search: ")
```

This program reads the file line by line and identifies where the word exists.

---

# ⚠ Exception Handling in Python

Exceptions occur when **errors interrupt normal program execution**.

Python handles them using:

- `try`
- `except`
- `else`
- `finally`

Example:

```python
try:
    result = num1 / num2
except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

# ⚡ List Comprehension

A **short and powerful way to create lists** in Python.

Example:

```python
squares = [x**2 for x in range(1,11)]
```

Examples practiced:

- Creating squares list
- Finding even numbers
- Squaring odd numbers
- Replacing negative values
- Converting words to uppercase

---

# 🌐 JSON Module in Python

JSON (JavaScript Object Notation) is used to **store and exchange structured data**.

### JSON Data Mapping

| JSON | Python |
|-----|------|
| object | dict |
| array | list |
| string | str |
| number | int / float |
| true | True |
| false | False |
| null | None |

---

### Important JSON Functions

| Function | Purpose |
|--------|---------|
| json.load() | Read JSON from file |
| json.loads() | Read JSON from string |
| json.dump() | Write JSON to file |
| json.dumps() | Convert Python object to JSON string |

Example:

```python
import json

python_obj = {"name":"Jane Doe","age":25}
json_string = json.dumps(python_obj)
```

---

# 🧪 Practice Programs

Solved several practice problems including:

1️⃣ Writing multiple names into a file and reading them  
2️⃣ Creating and updating a log file  
3️⃣ Filtering numbers using list comprehension  
4️⃣ Managing city population data using JSON files  
5️⃣ Handling missing file errors using exception handling  

---

# 🎯 Learning Outcome

After completing Day 05, I learned:

- Reading and writing files in Python  
- Managing files using different modes  
- Using the `with` statement for safe file handling  
- Handling runtime errors using exception handling  
- Writing efficient list operations using list comprehension  
- Working with structured data using JSON  

These concepts are important for **data processing, backend systems, automation, and Machine Learning pipelines**.
