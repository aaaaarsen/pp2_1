#ex 1
def multilpy_all_el(n):
    prod = 1
    for i in n:
        prod *= i
    return prod

my_list = [1, 2, 3, 4, 5, 10]
product = multilpy_all_el(my_list)
print(product)