# Q1 Ask the user for a string and check whether it is a palindrome or not

word = input("Enter the word: ")
print(word[::-1])
if word == word[::-1]:
    print("Given word is a palindrome")
else:
    print("Given word is NOT a palindrome")

#Q2 : Given a list of integers compute the average of all numbers in the list

numbers =[ 2,3,5,6,9,7,8]
sum=0
for num in numbers :
    sum+=num
average=sum/len(numbers)
print(average)

#Q3  Input two lists of integers from the user. Merge them into one list and sort the result.

list1=[]
print("Enter members of list 1 ->")
for i in range(1,6):
   num=(int)(input(" : "))
   list1.append(num)
print(f"List 1 items are : {list1}")

list2=[]
print("\nEnter members of List2 ->")
for i in range(1,5):
   num=(int)(input(" : "))
   list2.append(num)
print(f"List 2 items are : {list2}")


concatenatedlist=(list1 + list2)
print(f"\nConcatenated list is : {concatenatedlist}")

sorted_list = sorted(concatenatedlist)
print(f"\n Sorted list by using sorted () is : {sorted_list}")

concatenatedlist.sort()
print(f"\nsorted list using sort () is : {concatenatedlist}\n")

#Q4 . Given a tuple of integers , create :
'''• A tuple of all even numbers
• A tuple of all odd numbers '''

giventupple = (3,4,3,2,454,56,4,5,9,7,5,4,3,7)
eventupple = ()
oddtupple = ()

for num in giventupple:
    if num % 2 == 0:
        eventupple = eventupple + (num,)   # add element to tuple
    else:
        oddtupple = oddtupple + (num,)     # add element to tuple

print("Even tuple:", eventupple)
print("Odd tuple:", oddtupple)

# Q5 . Create a dictionary where :
'''• Keys = student names
• Values = marks (integer)
Write a menu-based program where user presses a key (ʼAʼ, ‘Bʼ, ‘Cʼ, ‘Dʼ)
depending on the operation they want to perform on the dictionary'''

student_info = {
    "Sonu": 99,
    "Lalit": 98,
    "Nikhil": 97,
    "Ankit": 90
}

print("Choose an operation you want to perform:")
print("A) Add a Student")
print("B) Update Marks")
print("C) Search for a Student")
print("D) Display all Students and Marks")

key = input("Enter your choice: ").upper()

# A) Add a student
if key == 'A':
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    student_info[name] = marks
    print("Student added successfully!")

# B) Update marks
elif key == 'B':
    name = input("Enter student name to update marks: ")
    if name in student_info:
        new_marks = int(input("Enter new marks: "))
        student_info[name] = new_marks
        print("Marks updated successfully!")
    else:
        print("Student not found!")

# C) Search for a student
elif key == 'C':
    name = input("Enter student name to search: ")
    if name in student_info:
        print(f"{name} found! Marks = {student_info[name]}")
    else:
        print("Student not found!")

# D) Display all students
elif key == 'D':
    print("All students and their marks:")
    for name, marks in student_info.items():
        print(name, ":", marks)

else:
    print("Invalid choice!")

#Q6  Given a list of words:
'''
words = ["apple", "banana", "kiwi", "cherry", "mango"]
Create a dictionary that maps each word to its length.
Example:
{"apple": 5, "banana": 6, "kiwi": 4, ...}'''

mylist=["SONU","Lalit","Nikhil","Ankit","Pankaj"]
diction={}
for name in mylist :
   diction[name]=len(name)
print(diction )

#Q7 Write a program that takes a string from the user and prints the number of spaces in the string.

mystring=(input("Enter any string : "))
flag=0
for ch in mystring :
    if ch==" ":
        flag+=1
        print(f" Number of spaces in the given string is : {flag}")
    else:
        print(ch)

#Q8 Write a program to check whether two lists share no common elements.
# share no common elements list1 = [1, 2, 3, 4] list2 = [5, 6, 7, 8]
# share common elements list1 = [1, 2, 3] list2 = [3, 4]

list1=[1,2,3,4,5,'b']
list2=[45,6,5,4,6,67,7,'b']

set1=set()
set2=set()

for i in list1:
    set1.add(i)

for j in list2:
    set2.add(j)

print(set1)
print(set2)
print("common elements in both the list ",set1.intersection(set2))

#Q9 Given a list, print all elements that appear more than once in the list.

List=[4,3,3,34,4,5,5,4,4,4,3,3,4,54,9]
seen=set()
duplicate=set()

for i in List:
    if i in seen :
        duplicate.add(i)
    else:
        seen.add(i)
print("Elements appearing more than once : {} and no of elements {}".format(seen,len(seen)))


#Q10 Ask the user for a string and print:
'''• All unique characters
• The count of unique characters'''

newstring=(input("Enter the string "))

newset=set()
for ch in newstring :
    newset.add(ch)

print("Unique characters in the String are",newset)
print("No. of unique characters :" ,len(newset))
