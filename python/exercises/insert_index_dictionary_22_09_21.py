#dictionary
original_dict = {'a':1, 'b':2}
key_l=[]
val_l=[]
for i,j in original_dict.items():
	key_l.append(i)
	val_l.append(j)
to_be_inserted={'c':3}
pos=1
updated_dict={}
for i in range(len(original_dict)+len(to_be_inserted)):
	if i==pos:
		updated_dict.update(to_be_inserted)
	else:
		k=0
		updated_dict.update({key_l[k]:val_l[k]})
		k+=1
original_dict.update(to_be_inserted)
print(original_dict)
