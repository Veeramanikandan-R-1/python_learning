input_string="JOHNISRUNNINGFAST"
n=12
loop_count=0
for i in range(0,len(input_string),n-1):
	loop_count+=1
temp=0
col_count=0
for i in range(0,len(input_string),n-1):
	if(temp<len(input_string)):
		#print(input_string[i])
		#col_count+=1
		#print(col_count)
		for j in range(n):
			temp+=1
		print(temp)
		#print(temp)
		col_count+=1
		for j in range(n-2):
			col_count+=1
			temp+=1
			#print(temp)
		#print(col_count)
print(col_count)
	
print(loop_count)
#print((len(input_string)//(n+(n-2)))+1)
pattern_list=[[" " for column in range(4)] for row in range(n)]
print(pattern_list)
col_pos=0
#print(len(input_string)//2)
letter_index=0
#for column in range((len(input_string)//2)+1):
for column in range(loop_count):
	if((column%2==0)):
		for row in range(n):
			print(row,col_pos)
			print(letter_index)
			if((letter_index<(len(input_string)) and (col_pos<loop_count+2))):
				pattern_list[row][col_pos]=input_string[letter_index]
				letter_index+=1
		col_pos+=1
	else:
		for row in range(n-2,0,-1):
			print(row,col_pos)
			if((letter_index<(len(input_string))) and (col_pos<loop_count+2)):
				pattern_list[row][col_pos]=input_string[letter_index]
				letter_index+=1
			col_pos+=1

#print(count)
for row in pattern_list:
	print(row)
for row in pattern_list:
	print("".join(row))
for row in range(n):
	for col in range(4):
		if(pattern_list[row][col] != " "):
			print(pattern_list[row][col],end="")
#print(pattern_list)
