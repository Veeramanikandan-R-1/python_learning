letter_m=[[" " for x in range(5)] for y in range(5)]
letter_a=[[" " for x in range(5)] for y in range(5)]
for x in range(5):
	for y in range(5):
		if((y==0) or(y== 4) or (x==2 and y ==2)):
			name_v[x][y]="*"

i,j=2,2
for x in range(3):
	name_v[x][x]="*"
	name_v[i][j]="*"
	i-=1
	j+=1
#print(name_v)
'''	
for x in range(5):
	for y in range(5):
		print(name_v[x][y],end="\n")
'''

for list_a in name_v:
	for digit in list_a:
		print(digit,end=" ")
	print("")
