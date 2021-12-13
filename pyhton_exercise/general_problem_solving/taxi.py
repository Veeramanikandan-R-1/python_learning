#given_list=[[2,5,4],[1,5,1]]
given_list=[[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]
earnings_list=[]

for i in range(len(given_list)):
	earning=0
	ref_val=0
	print(given_list[i:])
	for sub_list in given_list[i:]:
		if(sub_list[0]>=ref_val):
			ref_val=sub_list[1]
			earning+=(sub_list[1]-sub_list[0]+sub_list[2])
		else:
			continue
		print(earning)
	earnings_list.append(earning)
	print(earnings_list)

'''
diff_list=[]
for sub_list in given_list:
	diff_list.append(sub_list[1]-sub_list[0]+sub_list[2])
print(diff_list)

new_dictionary={}
for i in range(len(given_list)):
	new_dictionary[diff_list[i]]=given_list[i]
print(new_dictionary)
print(sorted(new_dictionary))
for list_1 in (new_dictionary.keys()):
	print(list_1)
	earnings_list.append(new_dictionary[list_1])
print(earnings_list)
'''

	