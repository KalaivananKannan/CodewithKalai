import re

txt=input("Enter the text: ")
# x=re.search(".*America$", txt)
y=re.findall("e", txt)
y2=re.findall("s", txt)

# if x:
#     print("Match found")
# else:
#     print("No match")

print(y)
print(y2)