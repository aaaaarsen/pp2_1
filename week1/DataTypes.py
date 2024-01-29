x = 5
print(type(x))

x = 1j
print(type(x))

x = ['apple' , 'banana' , 'melon']
print(type(x))

x = ('apple' , 'banana' , 'orange')
print(type(x))

x = range(6)
print(type(x))

x = {"name" : "Arsen" , "age" : 18}
print(type(x))

x = {"apple" , "banana" , "orange"}
print(type(x))

x = True
print(type(x))

x = b"hello"
print(type(x))

x = bytearray(5)
print(type(x))

x = memoryview(bytes(5))
print(type(x))

x = None
print(type(x))

# Setting the specific data type
x = str("hello world")

x = int(19)

x = float(3.9)

x = complex(1j)

x = list(("apple", "banana", "cherry"))	

x = tuple(("apple", "banana", "cherry"))

x = range(6)

x = dict(name="John", age=36)	

x = set(("apple", "banana", "cherry"))

x = frozenset(("apple", "banana", "cherry"))

x = bool(5)		

x = bytes(5)		

x = bytearray(5)		

x = memoryview(bytes(5))

# Exercises:

#ex1
x = 12
print(type(x)) # int

#ex2
x = "Hello World"
print(type(x)) # string

#ex3
x = 32.90
print(type(x)) # float

#ex4
x = ['apple', 'banana']
print(type(x)) # list

#ex5
x = ('apple', 'banana')
print(type(x))  # typle

#ex6
x = {"name" : 'John', "age" : 24}
print(type(x)) # dict

#ex7
x = True
print(type(x)) # bool