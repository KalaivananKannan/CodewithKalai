import userauth

from userauth import *


while True:

	n=input("1.Login || 2.Registration || 3. Show || 0.Exit: ")

	if n=="0":
		print("Thank you")
		break

	if n=="2":
		print("Enter the role type below for registration:")
		role=input("a. admin || b. user: ")

		if role=="a":
			admin={
			"username":input("Enter the username: "), 
			"password":input("Enter the password: ")
			}
			if len(user_auth)!=1:
				user_auth.append({"admin":admin})
			else:
				user_auth[0]["admin"]=admin
			print("Admin registered")

		if role=="b":
			i=0
			use=int(input("Enter number of user to be registered: "))
			l=[]
			while i<use:
				user={
					"username":input("Enter the username: "),		 
					"password":input("Enter the password: ")	
					}
				
				l.append(user)
				print("user regiserted")
				i=i+1
			if len(user_auth)!=1:
				user_auth.append({"user":l})
			else:
				user_auth[0]["user"]=l
	if n=="1":
		login=input("1a. admin login || 1b. user login")
		if login=="1a":
			ad=input("Enter the admin username to login: ")
			pwd=input("Enter the password: ")
			if ad==admin["username"] and pwd==admin["password"]:
				print("Login successful")
			else:			
				print("Login failed")
		if login=="1b":
			
			usern=input("Enter the username to login: ")
			pas=input("Enter the username password: ")
			flag=False
			i=0
			print(user_auth)
			while i<len(user_auth):
				
				usern==user["username"] and pas==user["password"]:
				flag=True
				break
				i=i+1
			print("Login Successful" if flag else "Login Failed")
				
	if n=="3":
		print(user_auth)

