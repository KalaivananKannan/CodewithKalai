import re

txt=input("Enter the text: ")
# x=re.search("^The.*Spain$", txt)
# y=re.findall("[The rain in Spain]", txt)
# y1=re.findall("[a-zA-Z0-9]", txt)
# x1=re.search("[a-zA-Z0-9]", txt)


if re.search(r'^(?=.*[a-z]{2})(?=.*[A-Z]{3})(?=.*[0-9])(?=.*[^a-zA-Z0-9]).{8,15}$', txt):
    print("login success")
else:
    print("login failed")

# y2=re.findall("[A-Z]", txt)
# y3=re.findall("[0-9]", txt)
# y4=re.findall("[^a-zA-Z0-9]", txt)
# x=re.search(".*America$", txt)
# y=re.findall("ea", txt)
# y2=re.findall("s", txt)

# print(x1)

# if x1:
#     print("Match found")
# else:
#     print("No match")

# print(y1)
# print(y2)
# print(y3)
# print(y4)