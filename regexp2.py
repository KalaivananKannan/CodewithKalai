import re
txt=input("Enter the text: ")
#x=re.findall("[a-m]", txt) #set of characters
#x2=re.findall("\d", txt) #Find all digits in characters
#x3=re.findall("h...o", txt) #search for sequence in between
# x4=re.findall("^hello", txt) #starts with
# if x4:
#     print("Match found")
# else:
#     print("Match not found")
# x5=re.findall("Planet$", txt) #ends with

# x6=re.findall("he.+o", txt)
# x7=re.findall("he.?o", txt)
# x8=re.findall("he.{4}o", txt)
# x9=re.findall("falls|stays|new", txt)

match=re.search(r"My name is (John) My name is (Raga)", txt)
print(match.groups())

#print(x)
#print(x2)
#print(x3)
#print(x4)
#print(x5)
#print(x6)
#print(x7)
#print(x8)
#print(x9)
