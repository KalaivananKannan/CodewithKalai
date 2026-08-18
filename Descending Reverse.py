print("\ndescending reverse")
k=4
i=0
while i<5:
	j=0
	while j<5:
		if j>=k:
			print("*", end="")
		else:
			print(" ", end="")
		j=j+1
	print("")
	i=i+1
	k=k-1
print("\ndescending reverse mirror")
k=0
i=0
while i<5:
	j=0
	while j<5:
		if j>=k:
			print("*", end="")
		else:
			print(" ", end="")
		j=j+1
	print("")
	i=i+1
	k=k+1
