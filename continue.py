try:
	i=0
	j=int(input("Enter the number from 0 to 20 to skip: "))
	while i<=20:
		
		if i==j:
			i=i+1
			continue
		else:
			print(i, end=" ")
		i=i+1

except ValueError:
	print("Only numbers should be entered")