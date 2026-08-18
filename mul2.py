list=[[1,2,3,4,5]]
l=[{'a':[1,2,3,4,5]}]

print(l)
#print(l[0])
#print(l[0]["a"])
#print(l[0]["a"][0])
#print(l[0]["a"][1])
#print(l[0]["a"][2])
#print(l[0]["a"][3])
#print(l[0]["a"][4])


def lforloop():
	number=int(input("Enter the number: "))
	flag=0
	for i in l[0]["a"]:
		if i == number:
			flag=1	
	if flag == 1:
		print("The number exists")
	else:
		print("The number not exists")

def lwhileloop():
	i=0
	number=int(input("Enter the number: "))
	flag=0
	while i<len(l[0]["a"]):
		if l[0]["a"][i] == number:
			flag = 1
		i=i+1
	if flag == 1:
		print("The number exists")
	else:
		print("The number not exists")
lwhileloop()


def forloop():
	number=int(input("Enter the number: "))
	flag=0
	for i in list:
		for j in i:
			if j == number:
				flag=1	
	if flag == 1:
		print("The number exists")
	else:
		print("The number not exists")


def whileloop():
	i=0
	number=int(input("Enter the number: "))
	flag=0
	while i<len(list[0]):
		if list[0][i] == number:
			flag = 1
		i=i+1
	if flag == 1:
		print("The number exists")
	else:
		print("The number not exists")
