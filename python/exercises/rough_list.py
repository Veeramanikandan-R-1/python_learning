letter_string=[chr(asci) for asci in range(65,91)]*3
print(letter_string)
order=7
matrix_result=[[" " for column in range(order)] for row in range(order)]
print(matrix_result)
letter_index=0
row_pos=0
col_pos=0
#for m in range(3):
while(order>0):
	for loop in range(4):
		if(loop==0):
			print(order)
			for box in range(order):
				print(row_pos,col_pos)
				if(letter_index<len(letter_string)):
					matrix_result[row_pos][col_pos]=letter_string[letter_index]
					letter_index+=1
				col_pos+=1
			col_pos-=1
			row_pos+=1
			order-=1
		elif(loop == 1):
			print(order)
			for box in range(order):
				print(row_pos,col_pos)
				if(letter_index<len(letter_string)):
					matrix_result[row_pos][col_pos]=letter_string[letter_index]
					letter_index+=1
				row_pos+=1
		elif(loop == 2):
			print(order)
			col_pos-=1
			row_pos-=1
			for box in range(order):
				print(row_pos,col_pos)
				if(letter_index<len(letter_string)):
					matrix_result[row_pos][col_pos]=letter_string[letter_index]
					letter_index+=1
				col_pos-=1
			order-=1
		elif(loop == 3):
			print(order)
			#print(row_pos)
			row_pos-=1
			col_pos+=1
			for box in range(order):
				print(row_pos,col_pos)
				if(letter_index<len(letter_string)):
					matrix_result[row_pos][col_pos]=letter_string[letter_index]
					letter_index+=1
				row_pos-=1
	row_pos+=1
	col_pos+=1
	print(order,"order")

for row in matrix_result:
	print(row)
