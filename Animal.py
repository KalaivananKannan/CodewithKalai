class Animal:

	def eat(self,type=''):
		if len(type)==0:
			print("Eating")
		else:
			print("Eating "+type)

	def noise(self):
		print("Making Noise")	

class Dog(Animal):
	def noise(self):
		print("Barking")

b=Dog()
b.eat()
b.eat("veg")
#b.sleep()
#b.noise()


print(len("hi")) #len is an example of overloading
print(len([1,2,5]))

polymorphism - 2 Types
#phone is an object which uses calling by phone and whatsapp which is an example of overloading 
#software update is an example of overriding where new feature is added and previous feature also should remain.

