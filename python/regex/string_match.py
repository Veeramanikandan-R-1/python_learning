import re
txt="this is a beautiful"
condition=re.findall("^this.*beautiful$",txt)
print(condition)
