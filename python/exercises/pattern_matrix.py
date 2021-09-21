matrix_given_1=[[0 for x in range(4)] for y in range(4)]
matrix_given_2=[[0 for x in range(4)] for y in range(4)]
matrix_given_3=[[0 for x in range(4)] for y in range(4)]
matrix_given_4=[[0 for x in range(4)] for y in range(4)]
#print(matrix)
def first(matrix):
	for i in range(4):
		matrix[i][i]=i+1
	#print(matrix)
	for row in matrix:
		print(row)
	print("\n")

def second(matrix):
	j=1
	for i in range(3,-1,-1):
		matrix[len(matrix)-1-i][i]=j
		j+=1
	#print(matrix)
	for row in matrix:
		print("".join(str(row)))
	print("\n")

def third(matrix):
	j=1
	for i in range(3,-1,-1):
		matrix[i][len(matrix)-1-i]=j
		j+=1
	#print(matrix)
	for row in matrix:
		print("".join(str(row)))
	print("\n")

def fourth(matrix):
	for i in range(3,-1,-1):
		matrix[i][i]=(len(matrix)-1)-i+1
	#print(matrix)
	for row in matrix:
		print("".join(str(row)))
	print("\n")

first(matrix_given_1)
second(matrix_given_2)
third(matrix_given_3)
fourth(matrix_given_4)

matrix_given_1=[[0 for x in range(4)] for y in range(4)]
matrix_given_2=[[0 for x in range(4)] for y in range(4)]
matrix_given_3=[[0 for x in range(4)] for y in range(4)]
matrix_given_4=[[0 for x in range(4)] for y in range(4)]

def common(start,end,third,initial,matrix):
	if initial==1:
		operation="add"
	else:
		operation="subtract"
	for i in range(start,end,third):
		if(operation=="add"):
			matrix[i][initial-1]=abs(initial)
			initial+=1
		else:
			matrix[i][initial-1]=abs(initial)+1
			initial-=1
	for row in matrix:
		print(row)
	print("\n")
common(0,4,1,1,matrix_given_1)
common(3,-1,-1,1,matrix_given_2)
common(0,4,1,0,matrix_given_3)
common(3,-1,-1,0,matrix_given_4)
