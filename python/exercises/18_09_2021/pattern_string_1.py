input_string="JOHNISRUNNINGFAST"
pattern_list=[[" " for x in range(len(input_string))] for j in range(3)]
print(pattern_list)

count=0
print(len(input_string)//2)
count_1=0
temp=1
for i in range((len(input_string)//2)+1):
	count+=1
	if((i%2==0)):
		for j in range(3):
			print(j,i)
			if(count_1<(len(input_string))):
				pattern_list[j][count-1]=input_string[count_1]
			count_1+=1
	else:
		for j in reversed(range(1)):
			print(1,temp)
			pattern_list[1][temp]=input_string[count_1]
			count_1+=1
		temp+=2
'''
for i in range(3):
	if(i!=2):
		gap=4
	else:
		gap=2
	for j in range(len(input_string)):
		for 	
		#pattern_list[i][j]=input_string[j]	
		pattern_list[i][j]="a"
		if(j!=2):
			count+=1
'''
print(count)
for i in pattern_list:
	print(i)
for x in range(3):
	for y in range((len(input_string)//2)+1):
		if(pattern_list[x][y] != " "):
			print(pattern_list[x][y],end="")
#print(pattern_list)
