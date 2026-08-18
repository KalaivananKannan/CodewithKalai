#students=["name","age","city"]
#student=[]
#l1=["Anand","12","Chennai"]
#l2=["Ananthu","14","Vellore"]
#l3=["Aravind", "15", "Villu"]

#student.append(students)
#student.append(l1)
#student.append(l2)
#student.append(l3)
#print(student)

l1=[[[1,2,3]]]
l2=[[[1,2,3]],[[4,5,6]]]
l3=[[[1,2,3]]],[[[4,5,6]]],[[[7,8,9]]],[[[10,11,12]]]

print("for loop")
print("l1: ",l1)
for i in l1:
	for j in i:
		for k in j:
			print(k, end=" ")
print("\nl2: ",l2)
for i in l2:
	for j in i:
		for k in j:
			print(k, end=" ")
print("\nl3: ",l3)
for i in l3:
	for j in i:
		for k in j:
			for l in k:
				print(l, end=" ")


print("\nwhile loop")
print("\nl1: ",l1)
print("l1 length")
print(len(l1))
i=0
while i<len (l1):
	j=0
	while j<len (l1[i]):
		k=0
		while k<len (l1[i][j]):
			print(l1[i][j][k], end=" ")
			k=k+1
		j=j+1
	i=i+1

print("\nl2: ",l2)
print("l2 length")
print(len(l2))
i=0
while i<len (l2):
	j=0
	while j<len (l2[i]):
		k=0
		while k<len (l2[i][j]):
			print(l2[i][j][k], end=" ")
			k=k+1
		j=j+1
	i=i+1

print("\nl3: ",l3)
print("l3 length")
print(len(l3))

i=0
while i<len (l3):
	j=0
	while j<len (l3[i]):
		k=0
		while k<len (l3[i][j]):
			l=0
			while l< len (l3[i][j][k]):
				print(l3[i][j][k][l], end=" ")
				l=l+1
			k=k+1
		j=j+1
	i=i+1
			



