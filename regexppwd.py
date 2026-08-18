import re

def register():
    username=input("Enter the username to register: ")
    password=input("Enter the password to register: ")
    print("Password Rules: Must be 8 to 15 characters include 1number, 1lowercase, 1uppercase, 1special character.")

    if (8<=len(password)<=15 and
        len(re.findall("[a-z]", password)) > 0 and
        len(re.findall("[A-Z]", password)) > 0 and
        len(re.findall("[0-9]", password)) > 0 and
        len(re.findall("[^a-zA-Z0-9]", password)) > 0):

        print("Password registered")
    else:
        print("Invalid password.")

while True:
    choice=int(input("1. Register || 2. Login || 3. Exit"))
    if choice==3:
        print("Thank you")
        break
    elif choice==1:
        register()
    elif choice==2:
        us=input("Enter the username to login: ")
        pa=input("Enter the password to login: ")

        if username==us and password==pa:
            print("Login success")
        else:
            print("Login failure")


