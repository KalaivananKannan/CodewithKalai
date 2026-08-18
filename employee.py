employees=[]
number=int(input("Enter the number of employees to add:"))
for i in range(number):
	employee={}
	name=input("Name: ")
	age=input("Age: ")
	ph_no=input("Ph_no: ")
	
	employee["personal_info"]={
	"name": name,
	"age": age,
	"ph_no": ph_no
	}

	designation=input("Designation: ")	
	department=input("Department: ")
	salary=input("Salary: ")

	employee["official_info"]={
	"designation": designation,
	"department": department,
	"salary": salary
	}

	employees.append(employee)

for employee in employees:
	for j in employee:
		print(" ")
		print(j)
		for k in employee[j]:
			print(k, ":", employee[j][k])
