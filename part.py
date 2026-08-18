class Employee:

	def __init__(self,basic,hra,esi,pf):
		self.basic=basic
		self.hra=hra
		self.esi=esi
		self.pf=pf
		
	def calculate_salary(self):
		print("Employee Salary Calculator not defined")
	
class FullTimeEmployee(Employee):

	def calculate_salary(self):
		print(self.basic+self.hra+self.esi+self.pf)

class PartTimeEmployee(Employee):

	def calculate_salary(self):
		print(self.basic+self.hra)

f=FullTimeEmployee(10000,2500,340,200)
p=PartTimeEmployee(5000,1250,0,0)

print("Employee Salary Calculator")

print("Full Time Employee")
f.calculate_salary()
print("Part Time Employee")
p.calculate_salary()