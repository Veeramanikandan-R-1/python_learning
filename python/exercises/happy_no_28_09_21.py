inp=2
inp=str(inp)
#n=4
while True:
	sqr=0
	#print(inp)
	for i in range(len(str(inp))):
		#print(inp[i])
		sqr+=(int(inp[i])*int(inp[i]))
	inp=str(sqr)
	if(inp=="1"):
		print("happy number")
		break
	elif(inp=="4"):
		print('sad')
		break
