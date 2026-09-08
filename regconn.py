import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="KalaiSql123#",
    database="Student"
)

print("Connected !!")

name= input("Enter the name: ")
age=str(input("Enter the age: "))
ph_no=str(input("Enter the ph_no: "))

username=input("Enter the username: ")
password=input("Enter the password: ")

cursor=conn.cursor()

# sql = "insert into studdata(id, name, age) values(6, 'Ragavi', 23)"
sql = "insert into register(age, name, ph_no, username, password) values("+age+", '"+name+"', "+ph_no+", '"+username+"', '"+password+"')"

cursor.execute(sql)
conn.commit()