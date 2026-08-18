class Hospital_Staff:

		def __init__(self,worktime,patients_handled):
			self.worktime=worktime
			self.patients_handled=patients_handled
		
		def work(self):
			print(" work ")
			
class Doctor(Hospital_Staff):

		def work(self):
			print(self.worktime, self.patients_handled)
			
class Nurse(Hospital_Staff):

		def work(self):
			print(self.worktime, self.patients_handled)
			
class Receptionist(Hospital_Staff):

		def work(self):
			print(self.worktime, self.patients_handled)

print("Hospital_Staff ")
print("worktime, patients_handled")
d=Doctor("10 AM - 1 PM", "3")
n=Nurse("8 AM - 1 PM", "7")
r=Receptionist("10 AM - 5 PM", "10")

staff=[d, n, r]

for s in staff:
	s.work()