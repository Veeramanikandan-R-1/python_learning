#n=int(input('enter n'))
n=5
for i in range(n*2):
	if(i<=((2*n)/2)):
		print('*'*(i+1))
	else:
		print("*"*((2*n)-i))
