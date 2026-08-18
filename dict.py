di={
	"name":"Rani",
	"age":29,
	"salary":20000,
	"location":"Spkoil"
}

d222={
	"name":"Vani",
	"age":32,
	"salary":25000,
	"location":"Madurai"
}


#print (di["name"])
#print (di.get("age"))
#di.keys()


#a = di.keys()
#print (a)

di["native"]="karur"
di["name"]="Manga"
d222["age"]=45
d222["native"]="Ranchi"
di.pop("age")  #to delete
d222.pop("age") #to delete
print(di)
print(d222)
print(di.values())
print(d222.values())