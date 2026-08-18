data={
	"stud_info":[
			{
			"name":"radhesh",
			"age":30
		     	},
		     	{
			"name":"magesh",
			"age":34
			}
		      ],
	"mark":{
		"phy":20,
		"chem":25
		}
}


print(data["stud_info"][1]["name"])

for i in data:
	print(i)
	if i=="stud_info":
		for j in data[i]:
			print(j["name"])
			print(j["age"])
