num=int(input("Enter a number:"))
original=num
reverse=0
while num>0:
	a=num%10
	reverse=reverse*10+a
	num=num//10
if original==reverse:
	print("Palindrome")
else:
	print("Not palindrome")
	