#question
#to find the repeated elements and print list of tuples having elements and number of times it repeated

#answer
list1=[1,2,2,4,4,5,6,6,61,1,1]
print("given list:",list1)
repeated_entry_list=[]
for i in range(len(list1)):
	if(((list1.count(list1[i]))>1)and(list1[i] not in list1[:i])):
		list2=[]
		#print(tuple1[0])
		list2.append(list1[i])
		list2.append(list1.count(list1[i]))
		repeated_entry_list.append(tuple(list2))
print(repeated_entry_list)