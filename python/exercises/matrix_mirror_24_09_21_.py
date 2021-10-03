max_row=4
max_col=4
initial_matrix=[[0 for box in range(max_col)] for box in range(max_row)]
result_matrix=[[0 for box in range(max_col)] for box in range(max_row)]
count=1

for row in range(max_row):
	for col in range(max_col):
		initial_matrix[row][col]=count	
		count+=1
#print(initial_matrix)
row_pos=0
for row in initial_matrix:
	print(row)

for row in range(max_col-1,-1,-1):
	for col in range(max_row):
		#print(row_pos,col)
		result_matrix[col][row]=initial_matrix[row_pos][col]	
	row_pos+=1
for row in result_matrix:
	print(row)
