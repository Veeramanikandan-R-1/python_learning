a=["a","z","e","b","c","l","a"]
b=["d","c","e","l","z"]
common_list=[]
for i in range(len(a)):
	for j in range(len(b)):
		if a[i]==b[j]:
			common_list.append(a[i])
		else:
			continue
added_list=a+b
final_list=[]
for letter in added_list:
	if letter not in common_list:
		final_list.append(letter)
print(a)
print(b)
#print(common_list)
print(final_list)
