given_set1=list((19,10,12,10,24,25,22))
k=4
def subset_fun(given_set):
	subset_list=[]
	for val in range(len(given_set)):
		rem_list=given_set[val+1:]
		for val1 in rem_list:
			temp=[]
			temp.append(given_set[val])
			temp.append(val1)
			if(temp not in subset_list):
				subset_list.append(temp)
	print(subset_list)
	subset=[]

	for i in subset_list:
		if (sum(i)%k)!=0:
			for val in i:
				if(val not in subset):
					subset.append(val)
	print(subset)
	'''
	ns=[]
	for lis in subset_list:
		ns1=lis
		print(ns1)
		for num in subset:
			#print(lis,num)
			con=True
			for num1 in lis:
				if(num1 not in ns1):
					print(num1,num,num1+num)
				if(((num1+num)%k!=0)):
					#print(num)
					#ns1+lis
					#print(new_lis)
					con=True
				else:
					con=False
					continue
			print(con)
			if(con==True):
				ns1.append(num)
			print(ns1)
		ns.append(ns1)
		print(ns)
	'''
	emp_list=[]
	for val in range(len(subset)):
		emp_list1=[]
		rem_list=subset[val+1:]
		#print(rem_list)
		for val1 in rem_list:
			if emp_list1:
				for val3 in emp_list1:
					print(val3)
			else:
				if((val+val1)%k!=0):
					emp_list1.append(subset[val])
					emp_list1.append(val1)
				print(emp_list1)
	#	emp_list.append(emp_list1)
	#print(emp_list)
	return subset
sub1=subset_fun(given_set1)
#print(sub1)

	
