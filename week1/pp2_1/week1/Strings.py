#Strings
print("Hello")
print('Hello')

#Assign string to var
x = "hello"
print(x)

#Multiline strings
a = """lorem30vrsvr rvervevrevev
vrevrev
ververververv
vreverv"""
print(a)

#Strings are Arrays
a = "Hello World"
print(a[1])

#Looping through a String
for x in "BOMBACLADDD":
    print(x)

#String Length
a = "Hello, World!"
print(len(a))

#Check String
txt = "The best things in life are free!"
print('free' in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
    
#Check if NOT
txt =  "The best things in life are free!"
print("expensive" not in txt)

txt =  "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present. ")
    



#Slicing
b = "Hello World"
print(b[2:5])

#slice from the start 
b = 'Hello World'
print(b[:5])

#slice to the end
b = 'Hello World'
print(b[2:])

#negative indexing
b = 'Hello World'
print(b[-5 : -2])



# Upper Case
a = 'Hello World'
print(a.upper())

# Lower Case
a = 'Hello World'
print(a.lower())

# Remove Whitespace
a = ' Hello World '
print(a.strip()) # returns "Hello World"

# Replace String
a = 'Hello World'
print(a.replace("H" , "J"))

# Split String
a = "Hello World"
print(a.split(",")) # returns ['Hello', 'World']


# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# String Format
age = 18
txt = "My name is Arsen, and i am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


