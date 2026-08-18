print("1to5* ascending")
j=0
while j<5:
	i=0
	while i<j:
		print("*", end="")
		i=i+1
	print("*")
	j=j+1
print("1to5 * descending")
j=5
while j>0:
	i=1
	while i<j:
		print("*", end="")
		i=i+1
	print("*")
	j=j-1
print("\nalternate 1to5 * descending")
j=5
while j>0:
	print("*"*j)
	j=j-1
print("justify")
i=0
while i<5:
	print("*"*5)
	i=i+1
print("\ndescending reverse")
k=4
i=0
while i<5:
	j=0
	while j<5:
		if j<=4:
			print("*")
		j=j+1
	i=i+1
k=k-1