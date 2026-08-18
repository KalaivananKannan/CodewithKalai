def update():

    naive=input("Enter the name of the student to update: ")

    if naive == view():

        new_name=input("Enter the new name: ")
        new_age=input("Enter the new age: ")
        new_phone=input("Enter the new ph_no: ")

        student=open("stu.txt", "a")
        student.write(new_name + "\t" + new_age + "\t" + new_phone + "\n")
        student.close()
        print("Updation done")

    if naive !=view():
        print("No student found")