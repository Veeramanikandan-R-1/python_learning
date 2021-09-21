import re

inp_string="mani && harish || "
#com=re.compile(' && | || ')
#print(com)
#condition=re.findall('[\s][&&|\|\|][\s]',inp_string)
condition=re.sub(" && | \|\| "," and ",inp_string)
print(condition)

