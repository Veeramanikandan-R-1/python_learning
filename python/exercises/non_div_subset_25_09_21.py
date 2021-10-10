'''
list_given=[1,7,2,4]
permutation_list=[]
def permutation_fun(list):
	for number in range(len(list_given)-1):
		temp=[]
		val=list_given[number]
		temp.append(val)
		rem_list=list_given[(number+1):]
		temp.append(rem_list)
	if(len(rem_list)>3):
		return
	else:
		permutation_fun(rem_list)
permutation_fun(list_given)
'''
input=[1,2,3,4,5]
output=[]
'''
for ind in range(len(input)):
	temp=[]
	temp.append(input[ind])
	output.append(temp)
	rem_list=input[(ind+1):]
	for ind_rem in range(len(rem_list)):
		temp1=[]
		temp1.append(input[ind])
		temp1.append(rem_list[ind_rem])
		print(temp1)
		output.append(temp1)
print(output)
'''
for ind in range(len(input)):
	temp=[]
	temp.append(input[ind])
	output.append(temp)
	rem_list=input[:ind]+input[ind+1:]
	for val in range(len(rem_list)):
		for ind_rem in range(len(rem_list)):
			temp1=[]
			temp1.append(input[ind])
			if val<len(rem_list):
				temp1.append(rem_list[val])
			if(temp1 not in output):
				output.append(temp1)
	for val in range(len(rem_list)):
		for ind_rem in range(len(rem_list)):
			temp1=[]
			temp1.append(input[ind])
			for i in range(len(input)):
				print(rem_list[i:i+2])
				if(rem_list[i:i+2]):
					temp1.append(rem_list[i:i])
print(output)
		