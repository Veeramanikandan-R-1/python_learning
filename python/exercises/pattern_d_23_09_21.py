for i in range(4):
	for j in range(5):
		if(j==0):
			print("*",end="")
		elif(i==0 and j!=4)or(i==3 and j!=4):
			print("*",end="")
		elif ((j==4 and i!=0) and (j==4 and i!=3)):
			print('*',end="")	
		else:
			print(" ",end="")
	print()
