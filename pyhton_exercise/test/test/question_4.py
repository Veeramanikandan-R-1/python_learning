# question
# from the given 2 lists return the list of tuples having coressponding elements in each list
# ex: list1=[1,2,3] and list2 =[4,5,6] output should be [(1,4),(2,5),(3,6)]

# answer
list1=[1,2,3,4,5,11]
list2=[6,7,8,9,10,12]
tuple_list=[]
print("given lists are","\n",list1,"\n",list2)
if(len(list1)==len(list2)):
	for i in range(len(list1)):
		list_temp=[]
		list_temp.append(list1[i])
		list_temp.append(list2[i])
		tuple_list.append(tuple(list_temp))
	print(tuple_list)
else:
	print("list is of different length")