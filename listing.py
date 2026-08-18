list1=["apple","orange","mango","lemon"]
list2=[100,250,150,400]
list1.sort()
print(list1)
#for x in list:
#	print(x)
list2.sort()
print(list2)

#l3=[20,10]
#l4=[]
#a=0
#for x in l3:
#	if a==0:
#		print(l3)


x=("apple","banana","lemon","rose","jasmine","lily")
b=("road")
print(x, "--Before update")
print(b)
y=list(x)
c=list(b)
c[0]=("street")
b=tuple(c)
y[2]="kiwi"
y[5]="lotus"
x=tuple(y)
print(x, "--After update")
print(b)