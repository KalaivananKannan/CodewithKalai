#numbers=[10,20,30]
#it=iter(numbers)
#print(next(it))
#print(next(it))
#print(next(it))


# def count():
#     yield "Apple"
#     yield "Orange"
#     yield "Mango"

# gen=count()

# print(next(gen))
# print(next(gen))
# print(next(gen))

# file=open("file.txt", "r")
# content=file.read()
# print(content)
# file.close()

# file=open("file.txt", "w")
# content=file.write("ffff")
# #print(content)
# file.close()

# file=open("file.txt", "r")
# content=file.read()
# print(content)
# file.close()


movie=open("movies.txt", "w")
list=movie.write("Hitman\tBatman\tSuperman\t")
movie.write("\nRoma")
movie.close()

movie=open("movies.txt", "r")
# list=movie.readline()
# print(list)
# print(movie.readline())



for i in movie:
    print(i.strip())

movie.close()