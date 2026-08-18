import login
from login import reg, login

def stud():
    name=input("Enter the name: ")
    age=input("Enter the age: ")
    ph_no=input("Enter the ph_no: ")

    student=open("stu.txt", "a")
    student.write(name + "\t" + age + "\t" + ph_no + "\n")
    student.close()
    print("student details entered")

def view():
    student=open("stu.txt", "r")
    stl=student.read()
    print(stl)
    student.close()

def reset():
    student=open("stu.txt", "w")
    student.write("")
    student.close()
    print("Reset done")

def update():
    
    naive=input("Enter the name of the student to update: ")
    student=open("stu.txt", "r")
    students=student.readlines()
    student.close
    
    flag=False
    student=open("stu.txt", "w")
    for line in students:
        if naive in line:
            new_name=input("Enter the new name: ")
            new_age=input("Enter the new age: ")
            new_phone=input("Enter the new ph_no: ")
            student.write(new_name + "\t" + new_age + "\t" + new_phone + "\n")
            print("Updation done")
            flag=True
        else:
            student.write(line)
    student.close

    if not flag:
        print("No student")  


while True:
    no=int(input("1. Registration || 2. Login ||  0. Exit"))
    if no==0:
        print("Thank you")
        break
    elif no==1:
        reg()
    elif no==2:             
        data = login()
        print("Logged username: " + data["username"])
        if data["flag"]==1:
       
            while True:    
                choice=int(input("1. Add student || 2. View students || 3. Reset students || 4. Update students || 0. Exit"))
                if choice==0:       
                    print("Thank you")
                    break
                elif choice==1:
                    stud()
                elif choice==2:
                    view()
                elif choice==3:
                    reset()
                elif choice==4:
                    update()

                
        if data["flag"]==0:
            print("Please enter correct username/password to login")