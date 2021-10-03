#print(letter_string)
#order=7
row=5
col=4
letter_string=[str(x+1).zfill(3) for x in reversed(range(row*col))]
print(letter_string) 
matrix_result=[[" " for column in range(col)] for row in range(row)]
#print(matrix_result)
letter_index=0
row_pos=0
col_pos=0
#for m in range(3):
while(row>0 and col>0):
	#print(row,col)
	#print(row_pos,col_pos)
	for loop in range(4):
		if(loop==0):
			#print(row)
			for box in range(col):
				#print(row_pos,col_pos)
				if(letter_index<len(letter_string)):
					matrix_result[row_pos][col_pos]=letter_string[letter_index]
					letter_index+=1
				col_pos+=1
			col_pos-=1
			row_pos+=1
			row-=1
			col-=1
			#order-=1
		elif(loop == 1):
			#col-=1
			print(col)
			for box in range(row):
				#print(row_pos,col_pos)
				if(letter_index<len(letter_string)):
					matrix_result[row_pos][col_pos]=letter_string[letter_index]
					letter_index+=1
				row_pos+=1
		elif(loop == 2):
			#print(order)
			col_pos-=1
			row_pos-=1
			#row-=1
			#print(row,col)
			for box in range(col):
				#print(row_pos,col_pos)
				if(letter_index<len(letter_string)):
					matrix_result[row_pos][col_pos]=letter_string[letter_index]
					letter_index+=1
				col_pos-=1
			#order-=1
			row-=1
		elif(loop == 3):
			#print(order)
			#print(row_pos)
			row_pos-=1
			col_pos+=1
			col-=1
			#print(col)
			for box in range(row):
				#print(row_pos,col_pos)
				if(letter_index<len(letter_string)):
					matrix_result[row_pos][col_pos]=letter_string[letter_index]
					letter_index+=1
				row_pos-=1
	row_pos+=1
	col_pos+=1
	#col+=1
	#print(order,"order")

for row in matrix_result:
	print(row)
	#for col in row:
	#	print(col,end="")
	#print()
