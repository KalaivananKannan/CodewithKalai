def insert(name, age, phone):
	name=name
	age=age
	ph_no=phone
	print("Thank you for entering the details")

def update(a):
	name=str(input("Enter the name to be updated "))
	age=int(input("Enter the age to be updated "))
	ph_no=int(input("Enter the Phone No to updated "))
	print("Thank you for entering the details")

while True:
	print("Student details")
	print("1-insert, 2-update, 3-display, 0-Exit")
	num=input("Enter the choice:")
	no=int(num)
	if no==0:
		print("Thank you")
		break
	if no==1:
		name = input("Enter the name ")
		age=int(input("Enter the age "))
		phone = int(input("Enter the Phone No "))
		insert("x")
	if no==2:
		
		update("a")
	if no==3:
		def display(c):
			print("Student details are ")
		update("a")