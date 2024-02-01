# Lists are used to store multiple items in a single variable.
fruits = ["apple", "banana", 'cherry']
print(fruits)

#List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#ex1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#ex2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#ex3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#ex4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

#ex5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#ex6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#ex7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#ex8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))