test_dict = {"Gfg": { "a" : [1, 3, 7, 8], "b" : [4, 9], "c" : [0, 7]}}
outer_key=[]
inner_val=[]
for i,j in test_dict.items():
	#outer_key.append(i)
	#inner_val.append(j)
	print(i)
	m={}
	for k,l in sorted(j.items(),reverse=True):
		m[k]={}
		(m[k])[i]=l
print(m)	
	#print(k,l)
		#(test_dict[k])[i]=l
#print(test_dict)
#print(outer_key)
#print(inner_val)
	
