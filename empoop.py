print("Employee Details")
class Employee:
	name=[]
	department=[]
	salary=[]
	
	def insert(self,name,department,salary):
		self.name.append(name)
		self.department.append(department)
		self.salary.append(salary)
	def delete(self):
		self.view()
		index=int(input("Enter index of the employee to delete"))
		del self.name[index]
		del self.department[index]
		del self.salary[index]
		print("Employee deleted")
	def view(self):
		for i in range(len(self.name)):
			#print(len(self.name))
			print("Index: ", i)
			print("Name: "+ str(self.name[i]))
			print("Department: "+ str(self.department[i]))
			print("Salary: "+ str(self.salary[i]))
			print(" ")
e=Employee()

while True:
	choice=int(input("1.Insert || 2.Delete || 3.View || 0.Exit: "))

	if choice==0:
		print("Thank you")
		break
	elif choice==1:
		no=int(input("Enter the no of employees to insert: "))
		for i in range(no):
			#print(range(no))		
			name=input("Enter the name: ")
			department=input("Enter the department: ")
			salary=int(input("Enter the salary: "))
			e.insert(name,department,salary)
			print("Details added")
	elif choice==2:
		e.delete()	
	elif choice==3:
		e.view()
	else:
		print("Invalid Choice")