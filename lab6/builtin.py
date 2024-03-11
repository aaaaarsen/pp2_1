#ex 1
def multilpy_all_el(n):
    prod = 1
    for i in n:
        prod *= i
    return prod

my_list = [1, 2, 3, 4, 5, 10]
product = multilpy_all_el(my_list)
print(product)


#ex 2
def calc(s):
    uppers = 0
    lowers = 0
    for ch in s:
        if ch.isupper():
            uppers+=1
        if ch.islower():
            lowers+=1
    return uppers, lowers

my_string = "Arsen"
result_uppers, result_lowers = calc(my_string)
print(f"Uppercase letters: {result_uppers}")
print(f"Lowercase letters: {result_lowers}")

#ex 3
def is_pali(s):
    i = s[::-1]
    if i == s:
        return True
    return False

my_str = str(input())
if is_pali(my_str):
    print(my_str, "is palindrome")
else:
    print(my_str, "is not palindrome")\
        
        
#ex 4
import math
import time

def calc_square_root(number, delay_ms):
  time.sleep(delay_ms / 1000)
  print(f"Square root of {number} after {delay_ms} milliseconds is {math.sqrt(number)}")


number = float(input())
delay_ms = int(input())
calc_square_root(number, delay_ms)

#ex 5

def are_True(n):
    h = 0
    for i in n:
        if bool(i):
           h += 1
    if h == len(n):
        return True
    return False

my_list = [1, 4, "", 'kbtu', 0]
res = are_True(my_list)
print(res)


