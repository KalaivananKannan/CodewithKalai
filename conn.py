import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="KalaiSql123#",
    database="Student"
)

print("Connected !!")

name= input("Enter the name: ")
id=str(7)
age=str(42)

cursor=conn.cursor()

# sql = "insert into studdata(id, name, age) values(6, 'Ragavi', 23)"
sql = "select * from studdata"

cursor.execute(sql)
rows=cursor.fetchall()

print("id   name    age     city")
for row in rows:
    for k in row:
        print(k, end='      ')
    print('')

conn.commit()

