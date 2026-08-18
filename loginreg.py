class User:
    def __init__(self, username, password):
        self.username=username
        self.password=password
    def getusername(self):
        return self.username
    def getpassword(self):
        return self.password


a=User("Rahul", "IPCSglobal123")
print(a.username())
print(a.password())

# while True:
#     choice=int(input("1-Login , 2-Register, 0-Exit"))
#     if choice==2:

#         username=input("Enter the username to register: ")
#         password=input("Enter the password to register: ")
#         user=User(username, password)

#     if choice==1:

#         username1=input("Enter the username to login: ")
#         password2=input("Enter the password to login: ")
#         if user.getusername()==username1 and user.getpassword() == password2:
#             print("login successful")
#         else:
#             print("login unsuccessful")
#     if choice ==0:
#         break