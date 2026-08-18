class Animal:
    def __init__(self):
        self.name='hai'
        self.sound='hello'

class Animal1(Animal):
    def __init__(self):
        self.name='hs'
        self.sound='ff'
        
class Dog(Animal1):
    def __init__(self):
        super().__init__()
        self.type='test'

class Puppy(Dog):
    def __init__(self):
        super().__init__()
        self.size=20




puppy = Puppy()
print(puppy.name)
print(puppy.sound)
print(puppy.type)
print(puppy.size)