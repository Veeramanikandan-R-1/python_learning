n=5
for i in range((2*n)):
	#for j in range(n-i-1):
	if(i<(2*n)//2):
		print(" "*(n-i-1),end="")
		print('*'*((2*i)+1),end="")
	else:
		print(" "*((i-n)+1),end="")
		print('*'*((2*n)-((i%5)+1)),end="")
	print()
