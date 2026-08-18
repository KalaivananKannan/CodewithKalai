students=[]
def insert(choice):		
	number=int(input("Enter the number of students to add:"))
	i = 1
	while i <= number:
		print(f"Student {i}")
		student=[]
		a = input("Enter the name: ")
		b = input("Enter the age: ")
		c = input("Enter the city: ")
		student.append(a)
		student.append(b)
		student.append(c)
		students.append(tuple(student))
		i=i+1
	print("Student details inserted successfully")
def show(students):
	print("\nStudent details:")
	print(students)
def update(students,index):
	newly = list(students[index])	
	print(newly)
	#students[index]=tuple(newly)
	
	a = input("Enter new name: ")
	b = input("Enter new age: ")
	c = input("Enter new city: ")
	newly[0]=a
	newly[1]=b
	newly[2]=c
	t=tuple(newly)
	#students.remove(students[index])
	students.insert(index, t)

	print("Student updated")
	print(students)
def remove_data(value,no):
	value=students[no]
	students.remove(value)
	print("Student removed")
	print(students)
def start():
	while True:
		choice = input("1-Insert, 2-Show, 3-Update, 4-Remove, 0-Exit: ")
		if choice == "0":
			print("Thank you")
			break
		elif choice == "1":
			insert(choice)
		elif choice == "2":
			show(students)
		elif choice == "3":
			value=int(input("Enter the student index to update: "))
			update(students,value)
		elif choice == "4":
			value=int(input("Enter the student index to remove: "))
			remove_data(students,value)
start()





def updated():
	name = input("Enter the name of the student to update: ")
	i = 0
	while i < len(students):
		if students[i][0] == name:
			print(f"Student found: {students[i]}")
			a = input("Enter new name: ")
			b = input("Enter new age: ")
			c = input("Enter new city: ")
			students[i] = (a, b, c)
			print("Student details updated successfully")
			return
		i=i+1
	print("Student not found")
def remove():
	name = input("Enter the name of the student to remove: ")
#	print(students)
	i = 0
	while i < len(students):
		if students[i][0] == name:
			print(f"Student found: {students[i]}")
			students.pop(i)
			print("Student removed successfully")
			return
		i=i+1
	print("Student not found")

