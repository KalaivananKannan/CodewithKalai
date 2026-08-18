#print(list(zip(["apple","orange","mango"],["alligator","ox","mangoose"],["albatross","owl","myna"])))
#def f(*args):
#	print(*args)
#f(1,2,3,"r","t")


#import sys
#print(sys.argv)
#from collections import Counter, deque

#from collections import defaultdict
#d=defaultdict(int)
#print(d["missing"])

#class Demo:
#	@property #With @property, we can access the method like a normal variable.
#	def value(self):
#		return 42
#obj=Demo()
#print(obj.value)


def greet(func):
	def wrapper():
		print("Hello!")
		func()
	return wrapper

@greet
def say_name():
	print("Kalaivanan")
say_name()


class Demo:
#	@staticmethod
	def add(a, b):
		return a+b
print(Demo.add(20, 44))


class Demo:
	name="Python"
	@classmethod
	def show():
		print(.name)
Demo.show()



