employees=[]
while True:
	print("--Employee Details--")
	print("Select 0-Exit|1-Add|2-View personal_info|3-View official_info|4-Update|5-Delete")
	
	choice=input("Enter your choice: ")
	
	if choice=="1":
		employee={}
		print("\n Enter Personal Info")
		name=input("Name: ")
		age=input("Age: ")
		ph_no=int(input("Ph_no: "))
			
		employee["personal_info"]={
		"name": name,
		"age": age,
		"ph_no": ph_no
		}

		print("\n Enter Official Info")	
		designation=input("Designation: ")	
		department=input("Department: ")
		salary=int(input("Salary: "))

		employee["official_info"]={
		"designation": designation,
		"department": department,
		"salary": salary
		}

		employees.append(employee)
		print("Employee details added")

	elif choice=="2":
		if not employees:
			print("No employees found")
		else:
			for i in range (len(employees)):
				print(f"\nEmployee {i+1}")
				for k in employees[i]["personal_info"]:
					v=employees[i]["personal_info"][k]
					print(f" {k}:{v}")
	elif choice=="3":
		if not employees:
			print("No employees found")
		else:
			for i in range (len(employees)):
				print(f"\nEmployee {i+1}")
				for k in employees[i]["official_info"]:
					v=employees[i]["official_info"][k]
					print(f" {k}:{v}")
	elif choice=="4":
		if not employees:
			print("No employees found")
		else:
			name=input("Enter name of the employee to update: ")
			found=False
			for employee in employees:
				if employee["personal_info"]["name"] == name:
					found=True
					print("Employee found")
					new_age=input(f"Age{employee['personal_info']['age']}: ")	
					if new_age:
						employee["personal_info"]["age"]=int(new_age)
				
					new_ph=input(f"ph{employee['personal_info']['ph_no']}: ")	
					if new_ph:
						employee["personal_info"]["ph_no"]=int(new_ph)
					new_designation=input(f"designation{employee['official_info']['designation']}: ")	
					if new_designation:
						employee["official_info"]["designation"]=(new_designation)
					new_department=input(f"department{employee['official_info']['department']}: ")	
					if new_department:
						employee["official_info"]["department"]=(new_department)
					new_salary=input(f"salary{employee['official_info']['salary']}: ")	
					if new_salary:
						employee["official_info"]["salary"]=int(new_salary)
					print("Employee details updated")
					break
			if not found:
				print("Employee not found")
	elif choice=="5":
		if not employees:
			print("No employees found")
		else:
			name=input("Enter name of the employee to delete: ")
			deleted=False
			for employee in employees:
				if employee["personal_info"]["name"] == name:
					employees.remove(employee)
					print("Employee deleted")
					deleted=True
					break
			if not deleted:
				print("Employee not found")
	elif choice=="0":
		print("Thank you")
		break
	else:
		print("Invalid choice")











