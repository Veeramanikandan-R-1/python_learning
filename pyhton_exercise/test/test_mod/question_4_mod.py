# question
# from the given 2 lists return the list of tuples having coressponding elements in each list
# ex: list1=[1,2,3] and list2 =[4,5,6] output should be [(1,4),(2,5),(3,6)]

# answer
list1=[1,2,3,4,5,11]
list2=[6,7,8,9,10,12]
print("given lists are","\n",list1,"\n",list2)
tuple_list=[(list1[x],list2[x]) for x in range(len(list1))]
print(tuple_list)