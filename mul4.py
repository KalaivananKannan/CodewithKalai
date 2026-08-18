student=[{"name":"anu","age":"20","gender":"male","city":"karur"},
	{"name":"manu","age":"21","gender":"male","city":"trichy"},
	{"name":"sanu","age":"19","gender":"female","city":"chennai"},
	{"name":"danu","age":"20","gender":"male","city":"salem"},
	{"name":"banu","age":"20","gender":"female","city":"mysore"},
	{"name":"tanu","age":"19","gender":"female","city":"kannur"}]

print(student)


#print(len(student))

def stuwhileloop():
	f=input("Enter the student name to display the details")

	i=0
	flag=0
	while i<len(student):
		if student[i]["name"]==f:
			flag=1
			print(student[i])
		i=i+1
	if flag == 1:
		print("Student found")
	else:
		print("No student")	
#stuwhileloop()


def stuforloop():
	f=input("Enter the student name to display the details")
	flag=0
	for i in student:
		if i["name"]==f:
			flag=1
			print(i)
	if flag == 1:
		print("Student found")
	else:
		print("No student")
stuforloop()