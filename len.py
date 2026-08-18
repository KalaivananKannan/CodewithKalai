#l1=[1,2,4,1]
#print(l1)
#print("Length of the above list:", len(l1))

#tp=(33,55,10,4)
#print(tp)
#print("Index tp[0] of the above tuple:", tp[0])
#print("Index tp[1] of the above tuple:", tp[1])
#print("Index tp[2] of the above tuple:", tp[2])
#print("Index tp[3] of the above tuple:", tp[3])

#students=[("Ram"),(5),(777)]

#def removedata(num,no):
#	value = students[no]
#	students.remove(value) # remove option takes only value not index hence created a variable "value" and assigned to students list as "no" - index
#	print(students)
#removedata(students,2)


stud=[('Saro', '23', 'Kannur'), ('Maga', '22', 'Ranipet'), ('Viru', '24', 'Ranchi')]
print(stud)

#def update(num,no):
	value=int(input("Enter the student index to update: "))
	print(stud[0])
	print(stud[1])
	print(stud[2])
	
	newly = list(stud[0])
	newly[0]="Maro"
	stud[0]=tuple(newly)
	print(stud)	

	a = input("Enter new name: ")
	b = input("Enter new age: ")
	c = input("Enter new city: ")
	stud.insert(2,a)
	stud.insert(2,b)
	stud.insert(2,c)
	print(stud)
update(stud,2)