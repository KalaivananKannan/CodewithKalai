#l1=["name","age","city","hh","name","age","city","hh"]

#i=0
#while i<len(l1):
#	print(l1[i])	
#	i=i+1


l1=[["name","age","city"],["Anu","12","caddalore"]]
#print(l1[0][0])
#print(l1[0][1])
#print(l1[0][2])

#print(l1[1][0])
#print(l1[1][1])
#print(l1[1][2])


i=0
	
while i<len(l1):
	j=0
	while j<len(l1[i]):
		print(l1[i][j])
		j=j+1
	print("")
	i=i+1
print("---------------------")
for w in l1:
	for q in w:
		print(q)