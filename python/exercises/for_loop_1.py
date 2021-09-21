a=["a","a","z","e","b","c","l"]
b=["d","c","e","l","z"]
final_list=[]
for i in range(len(a)):
	if ((a[i] not in b) and (a[i] not in a[:i])):
		final_list.append(a[i])
		print(final_list)
	for j in range(len(b)):
		if ((b[j] not in a) and (b[j] not in b[:i])):
			final_list.append(b[j])
print(a)
print(b)
print(final_list)
'''

		if ((a[i]!=b[j]) and (a[i] not in b) and (b[j] not in a)):
			final_list.append(a[i])
			final_list.append(b[j])
		else:
			continue
print(a)
print(b)
print(final_list)
added_list=a+b
final_list=[]
for letter in added_list:
	if letter not in common_list:
		final_list.append(letter)
print(a)
print(b)
#print(common_list)
print(final_list)
'''
