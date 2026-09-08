import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="KalaiSql123#",
    database="Student"
)

print("Connected !!")

name= input("Enter the name: ")
id=str(input("Enter the id: "))
age=str(input("Enter the age: "))
city= input("Enter the city: ")

cursor=conn.cursor()

# sql = "insert into studdata(id, name, age) values(6, 'Ragavi', 23)"
sql = "insert into studdata(id, name, age, city) values("+id+", '"+name+"', "+age+", '"+city+"')"

cursor.execute(sql)
conn.commit()

