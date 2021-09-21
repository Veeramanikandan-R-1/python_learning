list_given=[[1,4,5],[1,3,4],[2,6]]
added_str=""
for list_a in list_given:
	for digit in list_a:
		added_str+=str(digit)
print(added_str)
added_list=[]
maximum=100
added_list=[x for x in added_str]

for i in range(len(added_list)):
	for j in range(i):
		if added_list[i]<added_list[j]:
			added_list[i],added_list[j]=added_list[j],added_list[i]
print(added_list)

'''
for i in range(1,len(added_list)):
	for x in added_list[:i]:
		if (added_list[i]<x):
			condition=True
		else:
			condition=False
	if (condition==True):
		added_list[i-1]=added_list[i]
print(added_list)
'''		
