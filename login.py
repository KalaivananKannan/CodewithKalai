def reg():
    f=open("regis.txt", "w")
    username=input("Enter the username to register: ")
    password=input("Enter the password to register: ")

    f.write(username + "\n")
    f.write(password + "\n")
    print("User registered")
    f.close()

def login():
    f=open("regis.txt", "r")
    username=input("Enter the username to login: ")
    password=input("Enter the password to login: ")

    u=f.readline().strip() #print(len(u.strip())) **we will use strip function to remove spaces
    p=f.readline().strip()
    f.close()
    
    flag=0
    if username==u and password==p:
        print("login successful")
        flag=1
    else:
        print("login unsuccesful")
        flag=0
    
    l={"username":username, "flag": flag}
    return l