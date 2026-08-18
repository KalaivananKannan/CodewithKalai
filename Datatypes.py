
name=input("Enter the name: ")
Total_score=300
grade='A'
city=input("Enter the city: ")
state=input("Enter the state: ")

maths=int(input("Enter the maths score: "))
physics=int(input("Enter the physics score: "))
chemistry=int(input("Enter the chemistry score: "))


# numbers=[2,6,7,9]
# x,y,z,d=numbers

print(name,city,state)
print(maths+physics+chemistry)

if maths+physics+chemistry<Total_score:
	print("Fail")
else:
	print("Pass: ",grade)
