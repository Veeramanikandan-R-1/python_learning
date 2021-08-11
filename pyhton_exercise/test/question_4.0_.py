list1=[1,2,3,4,5,11]
list2=[6,7,8,9,10,12]
print("given lists are","\n",list1,"\n",list2)
tuple_list=[(list1[x],list2[x]) for x in range(len(list1))]
print(tuple_list)