input_string="JOHNISRUNNING"
n=5
pattern_list=[[" " for column in range((len(input_string)//2)+1)] for row in range(n)]
print(pattern_list)
count=0
print(len(input_string)//2)
letter_index=0
temp=0
for row in range((len(input_string)//2)+1):
	if((row%2==0)):
		count+=1
		for column in range(n):
			print(column,count-1)
			if(letter_index<(len(input_string))):
				pattern_list[column][count-1]=input_string[letter_index]
			letter_index+=1
		temp+=1
	else:
		for column in reversed(range(n-2)):
			print(column+1,temp)
			count+=1
			if(letter_index<(len(input_string))):
				pattern_list[column+1][temp]=input_string[letter_index]
				letter_index+=1
			temp+=1

print(count)
for i in pattern_list:
	print(i)
for x in range(n):
	for y in range((len(input_string)//2)+1):
		if(pattern_list[x][y] != " "):
			print(pattern_list[x][y],end="")
#print(pattern_list)
