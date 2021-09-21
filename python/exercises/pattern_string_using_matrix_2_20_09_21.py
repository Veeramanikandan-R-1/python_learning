input_string="JOHNISRUNNING"
n=5
pattern_list=[[" " for column in range((len(input_string)//2)+1)] for row in range(n)]
print(pattern_list)
count=0
print(len(input_string)//2)
letter_index=0
temp=0
for column in range((len(input_string)//2)+1):
	if((column%2==0)):
		count+=1
		for row in range(n):
			print(row,count-1)
			if(letter_index<(len(input_string))):
				pattern_list[row][count-1]=input_string[letter_index]
			letter_index+=1
		temp+=1
	else:
		for row in range(n-2,0,-1):
			print(row,temp)
			count+=1
			if(letter_index<(len(input_string))):
				pattern_list[row][temp]=input_string[letter_index]
				letter_index+=1
			temp+=1

print(count)
for row in pattern_list:
	print(row)
for row in range(n):
	for col in range((len(input_string)//2)+1):
		if(pattern_list[row][col] != " "):
			print(pattern_list[row][col],end="")
#print(pattern_list)
