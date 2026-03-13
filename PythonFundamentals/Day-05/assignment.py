#Q1

with open("names.txt", "w") as f:
    for i in range(1,6):
        name=input(f"Enter name {i} :")
        f.write(name+"\n")

    
with open("names.txt","r") as file:
 print("\n names in the file are : ")
 data= file.read()
 print(data)

 #Q2

with open("log.txt", "a") as f:
    f.write("this is the new log\n")

with open("log.txt", "r") as f:
    print(f.read())

#Q3

list=[5,10,15,20,25]
new_list=[x for x in list if x>5]
print(new_list)

#Q4
import json

cities = {
    "Delhi": "60k",
    "Mumbai": "90k",
    "Agra": "80k"
}

with open("cities.json", "w") as f:
    json.dump(cities, f, indent=4, sort_keys=True)

with open("cities.json", "r") as f:
    data = json.load(f)

print("Cities and their populations:")
for city, population in data.items():
    print(city, ":", population)

newcity = input("Enter new city name: ")
newpop = input("Enter its population: ")

data[newcity] = newpop

with open("cities.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=True)

print("Updated data saved to cities.json")
 
#Q5

try:
    with open("data.txt","r") as f:
        print(f.read())
except FileNotFoundError:
    print("File does not exist")









