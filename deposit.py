deposit_amount=0
while True:
	print("1-Deposit", "2-Withdrawal", "3-Display Balance", "0-Exit")
	number=input("Enter your choice:")
	no=int(number)	
	if no==0:
		print("Thank you")
		break
	else:
		if no==1:
			first=input("Enter the Deposit amount:")
			deposit_amount = deposit_amount+int(first)
			print("Thank you for deposit")
		if no==2:
			second=input("Enter the Withdrawal amount:")
			withdraw_amount=int(second)
			deposit_amount = deposit_amount-withdraw_amount
			print("Thank you for withdrawal")
		if no==3:
			print("Remaining balance")
			print(deposit_amount)
		elif no>=4:
			print("Wrong Choice")
	
