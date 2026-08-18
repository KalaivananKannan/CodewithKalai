print ("The largest of three numbers")
a=12
b=14
c=11
def large(a,b,c):
	if a>b:
		if a>c:
			print("a is greater")
		else:
			print("c is greater")
	else:
		if b>c:
			print("b is greater")
		else:
			print("c is greater")
large(a,b,c)
print("The second largest of three numbers")
def sec_lar(a,b,c):
	if a>b:
		if a>c:
			if b>c:
				print("b is second greater")
			else:
				print("c is second greater")
		else:
			print("a is second greater")
	else:
		if b>c:
			if a>c:
				print("a is second greater")
			else:
				print("c is second greater")

		else:
			print("b is second greater")
sec_lar(a,b,c)