given_list=[1,2,3,4,5,6,7,8,9]
count=0
init_pos=0
while(len(given_list)>0):
	count+=2
	given_list.remove(given_list[init_pos+count])
	print(given_list)
	print(count)
print(given_list)
