import re
value='32223232323mdfasdf@gmail.com65654654654654654'
condition=re.findall('^[a-z0-9]{3,25}@gmail.com$',value)
print(condition)