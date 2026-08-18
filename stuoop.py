print("Student details")
class Student:
	name=[]
	age=[]
	phoneNo=[]

	def stu_update(self,name,age,phoneNo):
		self.name.append(name)
		self.age.append(age)
		self.phoneNo.append(phoneNo)

	def display(self):
		for i in range(len(self.name)):
	
			print("Index: ", i)
			print("Name: "+ str(self.name[i]))
			print("Age: "+ str(self.age[i]))
			print("Phone_no: "+ str(self.phoneNo[i]))
			print("----------------------------")

	def remove_details(self):
		self.display()
		index=int(input("Enter the student index to remove: "))
		del self.name[index]
		del self.age[index]
		del self.phoneNo[index]			

s=Student()

while True:
	type=int(input("1-register || 2-display || 3-Remove || 0-exit: "))

	if type==0:
		print("Thank you")
		break

	if type==1:
		no=int(input("Enter no of students to register: "))
		for i in range(no):
			name=input("Enter the name: ")
			age=input("Enter the age: ")
			phone=int(input("Enter the phone_no: "))
			s.stu_update(name,age,phone)
			print("student details registered")

	if type==2:
		s.display()

	if type==3:
		s.remove_details()
		print("Student details removed")

	if type>3:
		print("Invalid Choice")	


	

