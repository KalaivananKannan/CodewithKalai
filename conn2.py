import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="KalaiSql123#",
    database="Student"
)

print("Connected !!")

# id=str(7)
# age=str(42)

cursor=conn.cursor()
# sql = "insert into studdata(id, name, age) values(6, 'Ragavi', 23)"
# sql = "update studdata set name='Roma' where id=3"
sql = "delete from studdata where id=5"
cursor.execute(sql)

conn.commit()

