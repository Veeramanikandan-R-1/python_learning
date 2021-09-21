import re
str_given="aaadaa"
sub_str="aa"
m=re.search(sub_str,str_given)
while m:
	i=0
	print("({},{})".format(m.start(),m.end()-1))
	m=re.search(str_given[i:],sub_str)
	i+=1
