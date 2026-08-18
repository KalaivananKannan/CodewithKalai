print("1-Add", "2-Sub", "3-Mul", "4-Div")

try:
	number=int(input("Enter your choice:"))

	first=float(input("Enter the first no:"))
	second=float(input("Enter the second no:"))
	
	if number==1:
		print("Result=",first+second)
	elif number==2:
		print("Result=",first-second)
	elif number==3:
		print("Result=",first*second)
	elif number==4:
		if second==0:
			print("Division by 0 is not allowed")
		else:
			print("Result=",first/second)
	else:
		print("Invalid choice. Please enter 1 or 2 or 3 or 4")
		
except ValueError:
	print("Please enter only numbers")