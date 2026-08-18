employees=[]

while True:
	print("\n--Employee Details--")
	choice = input("1-add || 2-update || 3-delete || 4-view || 0-exit: ")
	
	if choice == "0":
		print("Thank you")
		break

	if choice == "1":

		num=int(input("Enter number of employees to add: "))
		
		i=1
		while i<=num:
			employee={}
			print("personal_info")
			employee["personal_info"]={
			"name":input("Enter the name: "),
			"age":int(input("Enter the age: ")),
			"city":input("Enter the city: ")
			}
			print("official_info")	
			employee["official_info"]={
			"designation":input("Enter the designation: "),
			"department":input("Enter the department: "),
			"salary":int(input("Enter the salary: "))
			}
			employees.append(employee)
			i=i+1
			print("Details added")
			
	
	if choice == "2":
		
		name=input("Enter the name of the employee to update: ")
		for employee in employees:
			newemp={}
			if employee["personal_info"]["name"]==name:
				print("Employee found")
				
				new_age = input("Enter the new age: ")
				employee["personal_info"]["age"] == new_age
				print(new_age)
				
				new_city = input("Enter the new city: ")
				employee["personal_info"]["city"] == new_city
				print(new_city)
				
				new_designation = input("Enter the new designation: ")
				employee["official_info"]["designation"] == new_designation
				print(new_designation)
				
				new_department = input("Enter the new department: ")
				employee["official_info"]["department"] == new_department
				print(new_department)
				
				new_salary = input("Enter the new salary: ")
				employee["official_info"]["salary"] == new_salary
				print(new_salary)
				employees.append(newemp)

	if choice == "3":
		name=input("Enter the name of the employee to delete: ")
		for employee in employees:
			if employee["personal_info"]["name"]==name:
				employees.remove(employee)
				print("Employee deleted")
				break	
	if choice == "4":
		for employee in employees:
			for j in employee:
				print(" ")
				print(j)
				for k in employee[j]:
					print(k, ":", employee[j][k])

		
