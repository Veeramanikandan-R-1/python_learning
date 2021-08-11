#question
#from given lists i)find common elements in both lists 
#ii)find element in list1 but not in list2
#iii)combined list of list1 and list2 with unique elements

#answer
list1=[1,2,3,10,11]
list2=[5,6,7,8,9,1,3]
list1_set=set(list1)
list2_set=set(list2)
print("common elements in both lists are:",list(list1_set.intersection(list2_set)))
print("elements in list1 but not in list2 are:",list(list1_set.difference(list2_set)))
print("unique elements after combining both lists are",list(list1_set.union(list2_set)))