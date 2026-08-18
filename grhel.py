names=["Aravind", "Bala", "Chandran"]

def greet(names):
    return "Hello "+names

# l=[]
# for i in names:
#     l.append(greet(i))
# print(l)

a= map(greet,names)

print(list(a))
print(tuple(a))