Fname=""
Fage=""
Fphone=""
def insert(name,age,phone):
	global Fname
	global Fage
	global Fphone
	Fname=name
	Fage=age
	Fphone=phone
def update(name,age,phone):
	global Fname
	global Fage
	global Fphone
	Fname=name
	Fage=age
	Fphone=phone
def display():
	print("Name:",Fname)
	print("Age:",Fage)
	print("Phone:", Fphone)
while True:
	print("Student details. Press 1-insert, 2-update, 3-display, 0-Exit")
	num=input("Enter the choice:")
	no=int(num)
	if no==0:
		print("Thank you")
		break
	elif no == 1:
		name = input("Enter the name ")
		age = input("Enter the age ")
		phone = input("Enter the phone no ")
		print("Thank you for inserting the details")
		insert(name,age,phone)
	elif no == 2:
		name = input("Enter the name to be updated")
		age = input("Enter the age to be updated")
		phone = input("Enter the phone no to be updated")	
		print("Thank you for updating the details")
		update(name,age,phone)
	elif no == 3:
		display()