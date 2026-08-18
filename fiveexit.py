i=0
while i<=5:
	print("1-Add", "2-Sub", "3-Mul", "4-Div", "5-Exit")
	number=input("Enter your choice:")
	if number.isdigit():
		no=int(number)	
	
		if no==5:
			break
		elif no>5:
			print("wrong choice")
		else:
			first=input("Enter the first no:")
			a=int(first)
			second=input("Enter the second no:")
			b=int(second)
			if no==1:
				print(a+b)
			elif no==2:
				print(a-b)
			elif no==3:	
				print(a*b)
			elif no==4:
				print(a/b)
	i=i+1
