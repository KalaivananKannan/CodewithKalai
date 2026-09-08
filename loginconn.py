# import regconn
# from regconn import *
import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="KalaiSql123#",
    database="Student"
)

print("Connected !!")

cursor=conn.cursor()

user=input("Enter the username to login: ")
pwd=input("Enter the password to login: ")


#sql = "insert into studdata(id, name, age) values(6, 'Ragavi', 23)"
#sql = "update register set username='Tarika@123' where name='Tarika'"
#sql2= "update register set password='Ipcs@global2' where name='Tarun'"
sql2= "select * from register"
cursor.execute(sql2)
rows=cursor.fetchall()
#print(rows)

flag=0
for row in rows:
    
    if row[3]==user and row[4]==pwd:    
        flag=1
        
if flag==1:
    print("login success")
    print("Name     Age     Phone_no")
    for k in row[0:3]:
        print(k, end= "     ")
    print(" ")
else:
    print("Invalid credentials!")
conn.commit()