given_list=[[2,5,4],[1,5,1]]
earning=0
ref_val=0
for sub_list in given_list:
	if(sub_list[0]>ref_val):
		ref_val=sub_list[1]
		earning+=(sub_list[1]-sub_list[0]+sub_list[2])
	else:
		continue
print(earning)
	