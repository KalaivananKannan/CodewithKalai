#class A:
#	name=""
#	age=0
#	def __init__(self):
#		print("hello")
#a=A()


#a.__init__()

#class A:
	
#	def __init__(self,name,age): #behaviour
#		self.name=name  #feature
#		self.age=age      #feature

#	def display(self):    #behaviour
#		print(self.name) #feature
#		print(self.age) #feature

#a=A("Arun","20")
#b=A("Varu","30")
#c=A("Raja","32")
#a.display()
#b.display()
#c.display()


#class Person:
	
#	def __init__(self,name,age):   
#		self.name=name
#		self.age=age

#		print(self.name)
#		print(self.age)

#a=Person("Arun","20")
#b=Person("Varu","30")
#c=Person("Raja","32")


class Calculator:

	def __init__(self,a,b):
		self.a=a
		self.b=b

	def add(self):
		print(self.a+self.b)		
	
	def sub(self):
		print(self.a-self.b)

	def mul(self):
		print(self.a*self.b)

	def div(self):
		print(self.a/self.b)

#print("a=10 || b=20")
#a=Calculator(10,20)

#a.add()
#a.sub()
#a.mul()
#a.div()

#print("a=21 || b=30")
#b=Calculator(21,30)

#b.add()
#b.sub()
#b.mul()
#b.div()


class ScientificCalculator(Calculator):
	pass                  #if no body we can use "pass"
	
b=ScientificCalculator(21,30)

b.add()





