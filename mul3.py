z=[{"name":"anu",},{"name":"manu"},{"name":"sanu"},{"name":"danu"},{"name":"banu"},{"name":"tanu"}]

print(z)
#print(z[0])
#print(len(z))
#print(z[0]["name"])
#print(z[1]["name"])

def zforloop():
	na=input("Enter the name: ")
	flag=0
	for i in z:
		if i["name"] == na:
			flag=1	
	if flag == 1:
		print("The name exists")
	else:
		print("The name not exists")
zforloop()

def zwhileloop():
	i=0
	name=input("Enter the name: ")
	flag=0
	while i<len(z):
		if z[i]["name"] == name:
			flag = 1
		i=i+1
	if flag == 1:
		print("The name exists")
	else:
		print("The number not exists")
#zwhileloop()
