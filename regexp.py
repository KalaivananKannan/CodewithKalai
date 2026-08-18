import re

txt=input("Enter the text: ")

# y=re.findall("[arn]", txt)
# y2=re.findall("[a-b]", txt)

# print(y)
# print(y2)

# if y and y2:
#     print("Match found")
# else:
#     print("No match")

# z=re.findall("[^arn]", txt)
# z2=re.findall("[0123]", txt)

# print(z)
# print(z2)

# if z and z2:
#     print("Match found")
# else:
#     print("No match")

# b=re.findall("[0-9]", txt)
# b2=re.findall("[0-9][0-9][0-9]", txt)

# print(b)
# print(b2)

# if b2:
#     print("Match found")
# else:
#     print("No match")

#l=re.findall("[a-zA-Z]", txt)
l2=re.findall("[+.|(){}]", txt)

#print(l)
print(l2)

# if l and l2:
#     print("Match found")
# else:
#     print("No match")
