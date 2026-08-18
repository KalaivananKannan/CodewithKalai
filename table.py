students=[]
while True:
	print("\n1. Insert")
	print("2. Select")
	choice = input("Enter your choice: ")
	if choice == "1":
		number=int(input("Enter the number of students to add:"))
		i = 1
		while i <= number:
			print(f"Student {i}")
			student=[]
			a = input("Enter the name: ")
			b = input("Enter the age: ")
			c = input("Enter the phone_no: ")
			student.append(a)
			student.append(b)
			student.append(c)
			students.append(tuple(student))
			i=i+1
		print("Student details inserted successfully")
        
	elif choice == "2":
        	print("\nStudent details:")
        	print(students)
	else:
        	print("Invalid choice!")
        	break