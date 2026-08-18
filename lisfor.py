students = []
i = 1

while i <= 3:
    print(f"Stud {i}")
    a = input("Enter the name: ")
    b = input("Enter the age: ")
    c = input("Enter the phone_no: ")
    students.append([a, b, c])
    i=i+1

print("The student details:")
for student in students:
    print(student)
