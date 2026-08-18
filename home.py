current_user=None

def login(page):
        
    def log():
        global current_user

        if current_user==None:
            print("Kindly login first")

            username=input("Enter username: ")
            password=input("Enter password: ")
            
            if username=="admin" and password=="ipcs@123":
                print("login success")
                current_user=username
                page()
            else:
                print("Invalid")
        
        else:
            page()
                            
    return log

@login
def admin():
    print("Welcome to admin page !!!")

@login
def home():
    print("Welcome to home page !!!")

while True:
    no=int(input("1. Admin || 2. Home || 0. Exit"))
    if no==1:
        admin()
    elif no==2:
        home()
    elif no==0:
        print("Thank you")
        break