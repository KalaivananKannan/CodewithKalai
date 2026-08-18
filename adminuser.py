user_auth= [
	     {
		'admin': {'username': 'ipcs', 'password': 'global'},
		
		'user': [{
				'username': 'Tina', 
				'password': 'global111'
			 },
			 {
				'username': 'Nina', 
				'password': 'global112'
			 }
			]
	     }
]
print(type((1,)))
#print(user_auth)
#print(user_auth[0])
#print(user_auth[0]["admin"])
#print(user_auth[0]["user"])
#print(user_auth[0]["admin"]["username"])
#print(user_auth[0]["admin"]["password"])

#print(user_auth[0]["user"][0])
#print(user_auth[0]["user"][0]["username"])
#print(user_auth[0]["user"][0]["password"])

#print(user_auth[0]["user"][1])
#print(user_auth[0]["user"][1]["username"])
#print(user_auth[0]["user"][1]["password"])


#type=input("Enter the type (admin/user) : ")

def admin():
	user=input("Enter the username: ")
	pwd=input("Enter the password: ")

	if user==user_auth[0]["admin"]["username"] and pwd==user_auth[0]["admin"]["password"]:
		print("login successful")
	else:
		print("login unsuccessful")

#c="hi"
#v="kk"
#print(c+""+v)
#print(c,v)

#user=input("Enter the type: ")

def user():
	user=input("Enter the username: ")
	pwd=input("Enter the password: ")

	i=0
	flag=0
	while i<len(user_auth[0]["user"]):
		if user == user_auth[0]["user"][i]["username"] and pwd == user_auth[0]["user"][i]["password"]:
			flag=1
		i=i+1
	if flag == 1:
		print("login successful")
	else:
		print("login unsuccessful")

def userloop():
	user=input("Enter the username: ")
	pwd=input("Enter the password: ")

	
	flag=0
	for i in user_auth[0]["user"]:
		if user == i["username"] and pwd == i["password"]:
			flag=1
	if flag == 1:
		print("login successful")
	else:
		print("login unsuccessful")


#if type=="admin":
#	admin()
#if type=="user":
#	userloop()







