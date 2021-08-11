#question
#to find the repeated elements and print list of tuples having elements and number of times it repeated

#answer
list1=[1,2,2,4,4,5,6,6,61,1,1]
print("given list:",list1)
repeated_entry_list=[(list1[x],list1.count(list1[x])) for x in range(len(list1)) if(((list1.count(list1[x]))>1)and(list1[x] not in list1[:x]))]
print(repeated_entry_list)
#use simple by using set print([(val, dup.count(val)) for val in set(dup) if dup.count(val) > 1])