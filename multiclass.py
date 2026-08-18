#class Mammal:
#    def __init__(self):
#        self.type="Animal"

#class Animal:
#    def __init__(self):
#        self.name="Elephant"
#        self.foodtype="veg"

#class Elephant(Mammal,Animal):
#    def __init__(self):
#        Mammal.__init__(self)
#        Animal.__init__(self)

#e=Elephant()

#print("Mammal Type: " + e.type)
#print("Animal Name: " + e.name)
#print("Animal Foodtype: " + e.foodtype)


class Teacher:
    def __init__(self):
        self.type="Professor"
        self.teach="Teaching"

class Researcher:
    def __init__(self):
        self.research="Research"

class Professor(Teacher,Researcher):
    def __init__(self):
        Teacher.__init__(self)
        Researcher.__init__(self)

p=Professor()

print("Name: " + p.type)
print("Type1: " + p.teach)
print("Type2: " + p.research)