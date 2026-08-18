user=[{"name":'anu'},
      {"name":'rahul'}]
print(user)

a=input("Enter the name: ")

flag=0
i=0

while i<len(user):
	
	if user[i]["name"] == a:
		flag=1
	i=i+1

if flag==1:
	print("The name exists")
else:
	print("The name doesn't exist")

if user[1]["name"] == a:
	print("The name exists")
elif user[0]["name"] == a:
	print("The name exists.")
else:
	print("The name doesn't exist")

try:
	print(x)
except:
	print("an exception occur")

try:
	b=int(a)
	total = 0+b
	print("Type changed to integer, sum= ", total)
except:
	print("Its a string")
finally:
	print("It will always run, whether input is string or integer")