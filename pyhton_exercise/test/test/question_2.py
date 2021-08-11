#question
#from given lists i)find common elements in both lists 
#ii)find element in list1 but not in list2
#iii)combined list of list1 and list2 with unique elements

#answer
list1=[1,2,3,10,11]
list2=[5,6,7,8,9,1,3]
print("given lists are \n",list1,"\n",list2)
#first question
common_elements=[]
for entry in list1:
	if(entry in list2):
		common_elements.append(entry)
print("common elements in both lists are:",common_elements)

#second question
elements_not_in_list2=[]
for entry in list1:
	if(entry not in list2):
		elements_not_in_list2.append(entry)
print("elements in list1 but not in list2 are:",elements_not_in_list2)

#third question
combined_list=list1+list2
#print(combined_list)
combined_list_with_unique_entries=[]
for i in range(len(combined_list)):
	if(combined_list[i] not in combined_list[:i]):
		combined_list_with_unique_entries.append(combined_list[i])
print("unique elements after combining both lists are",combined_list_with_unique_entries)
		

