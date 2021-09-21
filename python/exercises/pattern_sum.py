a=3
total=0
for i in range(a):
	str_temp=""
	for j in range(i+1):
		str_temp+=str(a)
	print(str_temp)
	total+=int(str_temp)
print(total)
