'''
This is a really interesting program as it generates some really funny outputs. It is also a healthy practice problem for beginners who want to understand the “string” type more clearly. Let’s look into the problem.

Given a string, find a substring based on the following conditions:

The substring must be the longest one of all the possible substring in the given string.
There must not be any repeating characters in the substring.
If there is more than one substring satisfying the above two conditions, then print the substring which occurs first.
If there is no substring satisfying all the aforementioned conditions then print -1.
Although there can be many methods of approach to this problem, we will look at the most basic one.
'''
inp_string="cass"
def substring_match(string):
	substr_list=[]
	for value in range(len(string)):
		starting_index=value
		substr=""
		new_str=string[value:]
		#print(new_str)
		for i in range(len(new_str)):
			#print(new_str[:i])
			if new_str[i] in new_str[:i]:
				break
			else:
				substr+=new_str[i]
					
		substr_list.append(substr)
	#print(substr_list)
	return substr_list
substr_list=substring_match(inp_string)
max_str=""
for i in range(len(substr_list)-1):
	if len(substr_list[i])>len(max_str):
		max_str=substr_list[i]
print(max_str)
			
