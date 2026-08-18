data={
	"stud_info":{
			"name":"magesh",
			"age":34
			},
	"mark":{
		"phy":20,
		"chem":25
		}
}

#data["mark"]["mat"]=29
#data["stud_info"]["age"]=29
#print(data["stud_info"])

#data["stud_info"].pop("age")


#print(data)
for i in data:
	print(i)
	for j in data[i]:
		print(j, ":", data[i][j])
