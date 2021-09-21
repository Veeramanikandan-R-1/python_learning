#from operator import itemgetter
lis = [{ "name" : "Nandini", "age" : 26}, 
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Niikhil" , "age" : 19 },
{ "name" : "Nikkhil" , "age" : 25 },
{ "name" : "Nikhiil" , "age" : 30 },
{ "name" : "Nikhilh" , "age" : 19 }]
age_list=[]
for i in lis:
	age_list.append(i["age"])
age_list.sort()
print(age_list)

new_dic=[]
for dic in lis:
	if ((dic["age"]==age_list[0])):
			find=dic
			lis.remove(find)
			lis.insert(0,find)

#minimum=max(age_list)
for dic in range(len(lis)-1):
	minimum=max(age_list)
	if lis[dic+1]["age"]<minimum:
		minimum=lis[dic+1]["age"]
		lis[dic],lis[dic+1]=lis[dic+1],lis[dic] 
print(lis)
#print(sorted(lis,key=itemgetter('age')))
