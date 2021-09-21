input_string="JOHNISRUNNING"
n=5
loop_count=0
for i in range(0,len(input_string),n-1):
	loop_count+=1
print(loop_count)
print((len(input_string)//(n+(n-2)))+1)
pattern_list=[[" " for column in range((len(input_string)//2)+1)] for row in range(n)]
#print(pattern_list)
col_pos=0
#print(len(input_string)//2)
letter_index=0
for column in range((len(input_string)//2)+1):
#for column in range(loop_count):
	if((column%2==0)):
		for row in range(n):
			#print(row,count-1)
			if(letter_index<(len(input_string))):
				pattern_list[row][col_pos]=input_string[letter_index]
				letter_index+=1
		col_pos+=1
	else:
		for row in range(n-2,0,-1):
			#print(row,count)
			if(letter_index<(len(input_string))):
				pattern_list[row][col_pos]=input_string[letter_index]
				letter_index+=1
			col_pos+=1

#print(count)
for row in pattern_list:
	print("".join(row))
for row in range(n):
	for col in range((len(input_string)//2)+1):
		if(pattern_list[row][col] != " "):
			print(pattern_list[row][col],end="")
#print(pattern_list)
