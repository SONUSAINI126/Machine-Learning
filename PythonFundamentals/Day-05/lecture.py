# open , read ,close

'''f=open("file path","mode read(r) , write ") it return file object '''

f=open("sample.txt","r")

#data=f.read()
# Uses pointer concept for reading the file
data=f.readline()
print(data)

data=f.readline()
print(data)

print(type(data))
f.close()

#writing into a file 

f=open("sample.txt","a")
#While using the write function the complete file is overwritten 
f.write("\nThis is the Overriden text\n of previous file")

#File Operatios 
'''reading(default)
write & write + append mode "a"

# x --> x for creating a new file and write into it 
# rb--> write in binary form
# rt -->read in text form 
# wt -->write in text form 
# wb --> Write in binary form 
# r+  -->  read and write the file from starting and the pointer will point in the starting
# w+  --> write and read completely delete the content and start from the starting 
# a+ -->  append plus read ++ pointer wil starts from end  '''

file= open("sample2.txt","x")
file.write("This is the text written into the file new ones ")
file.close()

file=open("sample2.txt","r+")
file.write("new written in starting \n")
print(file.read())

file=open("sample2.txt","a+")
file.write("\n written in the end of the file")
print(file.read())  #it will read nothing since file pointer is at the end 



# with keyword --> isme auto closed ho jaati hai file 

with open("sample2.txt","r") as f:
    data=f.read()
    print(data)
    print(len(data))

#Deleting a fie --> OS operating system module 

import os 

os.remove("sample.txt")

#searching for a word in the file

with open("sample2.txt", "r") as f:
    word = input("Enter the word to be searched: ")
    
    line_number = 0
    found = False

    while True:
        line = f.readline()
        # If line is empty, we've reached the end of the file
        if not line:
            break
            
        line_number += 1
        
        if word in line:
            print(f"Word found at line no. {line_number}")
            found = True
            break
            
    if not found:
        print("Word not found in the file.")


#exceptions in python
''' Exception -> an event that occurs during the execution of a program that disrupts the normal flow of instructions'''
'''the try except and else(if no exception occurs) and finally(always) block is used to handle the exceptions '''

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter valid numbers!")
else:
    print("Division performed successfully.")
finally:
    print("Execution completed.")


#List Comprehension
''' concise way to create lists '''

squares = [x**2 for x in range(1, 11)]
print(squares)

even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)

squares_of_odd= [x**2 for x in range(1, 11) if x % 2 != 0]
print(squares_of_odd)

nums=[-2, -1, 0, 1, 2]
replaced_nums = [0 if x < 0 else x for x in nums]
print(replaced_nums)

words=['hello', 'world', 'python', 'is', 'awesome']
words_upper = [word.upper() for word in words]
print(words_upper)

#JSON(Javascript Object Notation) Module --
''' to work with json data 
null -> None
array -> list
object -> dict  
string -> str
true -> True
false -> False

Json Functions:
  json.load() -> to read json data from a file
    json.loads() -> to read json data from a string
    json.dump() -> to write json data to a file
    json.dumps() -> to write json data to a string
'''
import json

json_data = '{"name": "John Doe","age": 30}'
data = json.loads(json_data)
print(data)
print(type(data))

python_obj = {"name": "Jane Doe", "age": 25, "city": "New York"}
json_string = json.dumps(python_obj)
print(json_string)
 
with open("data.json", "w") as f:
    json.dump(python_obj, f,indent=4,sort_keys=True)

with open("data.json", "r") as f:
    data = json.load(f)
    print(data)

    