print("Range 0 to 10")
for i in range(10):
	print(i, end="")

print("\nRange 5 to 10")
for j in range(5,10):
	print(j, end="")

print("\nRange -3 to 10 with steps")
for i in range(-3,10,3):
	print(i, end="")

print("\n6 times *")
for i in range(0,6):
	print("*", end="")

print("\nver and hor *")
for i in range(0,5):
	print("*", end="")

for i in range(0,6):
	print("*")

print("\njustify *")
for i in range(0,5):
	for i in range(1,5):
		print("*", end="")
	print("*")

print("\nAscending *")
for i in range(1,6):
	print("")
	for j in range(0,i):
		print("*", end="")
		
print("\nDescending *")
for i in range(5,0,-1):
	for j in range(i):
		print("*", end="")
	print()