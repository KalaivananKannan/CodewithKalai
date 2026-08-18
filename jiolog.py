while True:
    type=int(input("1.Login || 2. Register || 0.Exit"))

    if type==2:
        user=input("Enter the username to register: ")
        pwd=input("Enter the password to register: ")
        username=user
        password=pwd
        print("user registered")
    if type==1:
        username=input("Enter the username to login: ")
        password=input("Enter the password to login: ")
        if username==user and password==pwd:
                print("Login successful")
        else:
                print("Login unsuccessful")
    if type==0:
        print("Thank you")
        break
    if type>3:
        print("Invalid Choice!!")

