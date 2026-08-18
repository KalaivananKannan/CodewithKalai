l=[1,2,3,4,5]
print(l)
#i=0
num=int(input("Enter a number: "))
flag=0  #we have assigned a variable outside the loop as print statement executes multiple times

#while i<len(l):
#	if l[i]==num:
#		flag=1
#	i=i+1


#if flag==1:
#	print("The number exists")
#else:
#	print("The number not exists")

for i in l:
	if num == i:	
		flag=1		
if flag==1:
	print("The number exists")
else:
	print("The number not exists")
	


	