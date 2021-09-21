import re
string=input('string\n')
string_input=input('enter a string\n')
#match=re.match('[{}]'.format(string_input),string)
#match=re.findall('[{}]'.format(string_input),string)
#print(match.start(),match.end())
#match=re.findall("{}".format(string_input),string)
match=re.search(string_input,string)
pattern=re.compile(string_input)
#print(pattern) 
#print(match)
for x,y in enumerate(string):
	if re.match(string_input,string[x:]):
		print(x,(x+len(string_input)-1))
	if re.search(string_input,string[x:])==None:
		print('(-1,-1)')
