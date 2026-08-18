def animal(s):
    a="wild or domestic"
    def add():
        
        print("Animal")
        s()
        
    return add

@animal
def wild():
    print("deer")

@animal
def domestic():
    print("dog")

# b=animal(second) 

wild()
domestic()
# def dog():
#     print("domestic")

# def deer():
#     print("wild")

# while True:
#     vari=int(input("2. Domestic - 3. Wild"))
#     if vari==2:
#         animal(dog)
#     if vari==3:
#         animal(deer)
