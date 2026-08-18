stud=[('Saro', '23', 'Kannur'), ('Maga', '22', 'Ranipet'), ('Viru', '24', 'Ranchi')]
print("Old:", stud)
print(" ")
print(stud[0])
print(stud[1])
print(stud[2])



def fir():
	newly=list(stud[2])
	newly[2]="Kanchi"
	stud[2]=tuple(newly)
	print(" ")
	print("New:", stud)
fir()
def newly():
	newly = list(stud[1])
	newly[0]="Majnu"
	stud[1]=tuple(newly)
	print(" ")
	print("New:", stud)
newly()

def now():
	newly = list(stud[0])
	newly[1]="44"
	stud[0]=tuple(newly)
	print(" ")
	print("New:", stud)
now()