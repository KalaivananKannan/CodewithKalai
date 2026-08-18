number = input("Enter the number: ")
num = int(number)

def check_number(num):
	if num < 0:
        	print("The number is negative", num)
        	return "negative"
	else:
        	print("The number is positive", num)
        	return "positive"

def even_or_odd(num):
	if num % 2 == 0:
        	print("The number is Even.")
	else:
        	print("The number is Odd.")

result = check_number(num)       
if result == "positive":         
    even_or_odd(num)