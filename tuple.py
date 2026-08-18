#l1=[1,2,4,1]
#print(len(l1))
#print(l1)
#tp=(1,2,3,4)
#print(tp[2])
#print(tp)

#list1=[1,2,1]

#list1.insert(3,4)
#list1.append(5)
#list1.sort()
#print(list1)

#pilot=("Roja","Raja","Kaja","Pooja")
#trainee=("Rani","Vani","Aani","Nani")

#print(pilot[0:4]) #slice
#print(pilot[1],pilot[2]) #index
#print(pilot,trainee)


#x=("apple","mango","papaya")
#y=list(x)
#y[1]="lemon"
#x=tuple(y)
#print(y)
#print(x)


#l1=[1,2,3] #unpacking
#first, second, third = l1
#print(first, second, third)
#print(second)
#print(third)


l1=(1,6,12)
one, six, twelve = l1
#(one, six, twelve) = 11 #we can also use brackets
a=0
print("forloop")
def forloop():
	for a in l1:
		print(a, end=" ")
	print("")
forloop()

print ("whileloop")

while a<len(l1): #we can use length function
	print(l1[a], end=" ")
	a=a+1
print(" ")
print("**TUPLE**")
tuple=(1,4,5,6)
print(tuple[1:5:2])

