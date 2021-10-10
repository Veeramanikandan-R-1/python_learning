M1 = [[1,2,3],[4,5,6]]
#M1=[[1,2],[3,4]]
M2 =[[1,2,3],[4,5,6],[7,8,9]]
#M2=[[5,6],[7,8]]
M3  = []
for i in range(len(M1)):
	temp1=[]
	for j in range(len(M1[i])):
		temp=0
		for k in range(len(M2)):
			#print(j,k)
			temp+=(M1[i][k])*(M2[k][j])
		temp1.append(temp)
	M3.append(temp1)
		#print(temp)
for row in M3:
	print(" ".join([str(x) for x in row]))
