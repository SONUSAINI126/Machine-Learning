#Strings in Python 
''' It is the sequence of characters '''
Word1 = "Python"
Word2 =" With Sonu Saini"
print(len(Word1))

#concatenate 

print(Word1 + Word2)

#indexes in String starts from 0

print(Word1[0])
for ch in Word2:
    print(ch)

'''Strings are immutable
Word[1]='P' will give an error '''

#Operation on String 
'''Slicing-> for getting substrings
str[starting index : ending index(excluded)]
default value of starting index is 0 
and of ending index is string(len) i.e. ending index+1
if we take index from starting -> 0 to str(length)-1
if we take index from end -> then first word index= -str(length) to -1 '''

print(Word1[2:5])
print(Word2[2: ])
print(Word2[ :6])
print(Word2[-5:-2])

#String formatting 
'''dynamic string ->different varaibles and values'''
'''Two ways to format are -> format() & -> f-strings
{} is the placeholder '''

a=5
b=10
sum=a+b

#normal formatting 
print("sum of {} and {} is {} ".format(a,b,sum))
print("language is {}".format("Python"))

#Index based formatting
print("Sum is {2} of {0} and {1}".format(a,b,sum))

#Value based formatting
'''reusability is possible'''
print("values of vars {a} & {b} where a is {a}".format(a=5, b=10))

#F-String
'''Literal string interpolation '''

print(f" Literal string interpolation Sum of {a} and {b} is {a+b}")

# # # Built in data TYPES in Python

##List 
'''mutable sequence of values '''

marks=[34,53,56,33,56,54]
'''these all have particular index starting from 0'''

print(marks)
print(len(marks))
print(marks[1])
marks[2]=90  
'''since list are mutable'''

detail = ["Sonu",99,"Lalit",98]

print(detail)
print(type(list))

#slicing of list 
''' on slicing we get the sub list '''

print(marks[0:5])
print(marks[5:len(marks)])
print(marks[-5:-1])

# Methods for list 

# l.append(val)-> add one element at the end
# l.insert (idx,val) -> insert element at index
# l.sort() -> arranges in increasing order 
# l.reverse() -> reverse order 

numbers=[1,2,3,4]

numbers.append(6)
print(numbers)

numbers.insert(2,9)
print(numbers)

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers.reverse()
print(numbers)

#Using Loops with list

for val in numbers :
    print(val)

'''Searching the value with index no. -> Linear Search'''

num=(int)(input("Enter the number to search : "))
idx=0
for val in numbers:
    if val==num:
        print(f"Value {num} found at index -> {idx}")
        break
    idx+=1

## Tuples in Python

'''Immutable sequence of values created using ()'''

tupple = (1,2,3,54,5,6,"Sonu","Lalit",1.10)
print(tupple)
print(type(tupple))
print(len(tupple))
print(tupple[6])

'''tupple[4]=9 this will give an error hence not possible'''

'''single value tupple should not be created 
as they will be interpreted as that datatype not tupple
if want to create a single value tupple then add , in last'''

singletupple=(2)
print(type(singletupple))

singletupple=("Sonu")
print(type(singletupple))

singletup=(1,)
print(type(singletup))

#slicing of tupple 

print(tupple[ :5])
print(tupple[ : ])

for var in tupple:
    print (var) 

# -> Methods in tupple

#t.index(val) -> return index or first occurence 
#t.count(val) -> count total occurrence 

mytup=(2,4,2,5,6,"sonu","Sonu")

print(f"index of 2 is {mytup.index(2)}")
print(f"no. of times value 2 in tupple is {mytup.count(2)}")




## Dictionary in Python

'''key value pair mai write krte hai hum 
    dictionary = { key:value }
    and the key is unique here 
    dictionary are muttable
    dictionary are unordered'''

info={
   "name":"Sonu",
   "Cgpa":9.8,
   "Subjects":["maths","Science","English"],
   3.14 : "PI"
}

print(info)
print(info["name"])
info["Cgpa"]=9.9
print(info)

##Methods in Dictionary 

#d.keys() ->> return all keys
#d.values() ->> return all values
#d.items() ->> return (key.val) pairs
#d.get(val) ->> return val acc. to key
#d.update(new_item) ->> add new item to dict

dict_key = list(info.keys())
print(dict_key)
print(type(dict_key))

dict_val = (info.values())
print(dict_val)
print(type(dict_val))

print(info.items())

# print(info.get(key))
'''also to get the key value pair like with [] 
but that will give an error if that key not exist 
but this will give none'''

print(info.get("Subjects"))
print(info.get("no_key"))

info.update({
    "city" : "Delhi"
})
print(info)



## Sets in Python

'''collection of unique elements 
and its elements must be immutable while the set can be muttable
sets are unordered'''

# Sets in Python

myset = {22, 2, 3, 34, 4, 2, 2}
print(myset)
print(type(myset))
print(len(myset))

myset.add(44)
print(myset)


'''creating empty set 
set={} will not create an empty set instead 
it will assume it a dictionary so we use () for empty set'''

empty_di = {}
print(type(empty_di))  # dict

emptyset = set()
print(type(emptyset))  # set

#Sets Methods in Python 

'''s.add()'''

myset.add(67)
print(myset)

'''s.remove(val)'''

myset.remove(67)
print(myset)

'''s.clear() -> empties the set '''

myset.clear()
print(myset)

'''s.pop() -> removes a random value'''

s={34,45,76,4,34,3,23,4}
print(s)
s.pop()
print(s)

'''s.union(set2)'''
a={2,2,3,3445,56,6,7}
b={3,2,4,45,6,7,889,8}

print(a.union(b))

'''s.intersection(s2)'''

print(a.intersection(b))


#practice Problems

''' Given a list of tuples with info(name,subject):
   1) List all unique courses
   2) List students enrolled in english 
   3) create dictioinary (student, set of courses)'''

mylist=[("Sonu","Maths"),
        ("Lalit","Science"),
        ("Sonu","Science"),
        ("Nikhil","Maths"),
        ("Lalit","Maths"),
        ("Sonu","English"),
        ("Nikhil","English")]

unique_courses=set()
for tup in mylist:
   unique_courses.add(tup[1])
print(unique_courses)

'''When we have iterables -> on which we can run loops 
we can use variables for them '''

for name,course in mylist :
    if course=="English":
      print(name,course)

dict={}
for name,course in mylist :
    if(dict.get(name)==None):
        dict.update({name :set()})
        dict[name].add(course)
    else:
        dict[name]

print (dict)
