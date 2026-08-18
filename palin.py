while True:
	no=input("Enter a number/text or (q to quit):")
	if no=='q':
		print("Thank you")
		break
	if no==no[::-1]:
		print("The entered one is a palindrome")
	else:
		print("The entered one is not palindrome")