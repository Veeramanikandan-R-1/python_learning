input_list=[1,2,3,4]
output=[]
'''
for number in range(len(input_list)):
	empty_list=[]
	empty_list.append(input_list[number])
	print(number)
	for number1 in input_list[:input_list.index(input_list[number])]:
		empty_list.append(number1)
		for number2 in input_list[input_list.index(input_list[number]):]:
			#print(number1,number2)
			empty_list.append(number2)
	output.append(empty_list)
print(output)
'''

len_list=len(input_list)
loop_count=1
for i in range(len(input_list)):
	loop_count*=(i+1)
print(loop_count)
def permutation_fun(input_list):
	for i in range(len(input_list)):
		rem_list=input_list[:i]+input_list[i+1:]
		rem_list.insert(0,input_list[i])
		output.append(rem_list)
		permutation_fun(rem_list)
		for j in range(len(rem_list)):
			pass
for row in output:
	print(row)
		
