# lambda arguments: expression
# map(function, iterable)
# filter(function, iterable)
# reduce(function, iterable)

# lambda → quick mini function
# map → transform all items
# filter → select only items that pass a test
# reduce → combine everything into one

# #EX:

# numbers=10,87,2,3,4,58,63,7,99,48
# even=filter(lambda x:x%2==0, numbers)
# l=list(even)
# print(l)
# odd=filter(lambda x:x%2!=0, numbers)
# m=list(odd)
# print(m)

# def add(num):
# 	return num*2


# mm= map(add, numbers)
# print(list(mm))


# for even1 in l:
# 	print(even1, end = " " )
# print(" ")
# for odd1 in m:
# 	print(odd1, end = " ")	


from functools import reduce
numbers=[1,2,3,4,5]

even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

double = list(map(lambda x: x**2, even))
print(double)

total = reduce(lambda a, b: a + b, numbers)
print(total)


