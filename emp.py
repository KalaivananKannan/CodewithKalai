
a={
	"personal_info":{
		"name":"Karan",
		"age":29,
		"ph_no":778
			},
	"official_info":{
		"designation":"Specialist",
		"department":"Operations",
		"salary":27000
			}
	}
b={
	"personal_info":{
		"name":"Maran",
		"age":28,
		"ph_no":798
			},
	"official_info":{
		"designation":"Analyst",
		"department":"Operations",
		"salary":27500
			}
	}
c={
	"personal_info":{
		"name":"Saran",
		"age":27,
		"ph_no":878
			},
	"official_info":{
		"designation":"Trainee QA",
		"department":"Quality",
		"salary":26000
			}
	}
d={
	"personal_info":{
		"name":"Paran",
		"age":32,
		"ph_no":708
			},
	"official_info":{
		"designation":"Specialist",
		"department":"Operations",
		"salary":29000
			}
	}

	


employees=[a,b,c,d]

#print(employees[0])
#print(len(employees))

for employee in employees:
	#print(employee)
	for j in employee:
		print(" ")
		print(j)
		for k in employee[j]:
			print(k, ":", employee[j][k])
