# f=open("Info.log", "r")
# gen=f.read()
# f.close()
# print(gen)

# def read_file(filename):
#     with open(filename, "r") as file:
#         return file.readlines()

def read_file(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line


lines=read_file("Info.log")

for line in lines:

    if "Error" in line:
        print(line)
        break
