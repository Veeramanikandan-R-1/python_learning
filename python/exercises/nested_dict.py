test_dict = {"Gfg" : 4, "best" : 9}
test_list = [8, 2]
output_list={}
new_list=[]
#for i in range(len(test_list)):
for x,y in test_dict.items():
	new_list.append({x:y})
print(new_list)	
for val in range(len(test_list)):
	output_list[test_list[val]]=new_list[val]
print(output_list)
