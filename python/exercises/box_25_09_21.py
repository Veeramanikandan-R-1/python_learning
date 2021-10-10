no_of_boxes=10
no_of_person=10
box_list=[0 for x in range(no_of_boxes)]
multiplier=1
for person in range(1,no_of_person+1):
	#print(person*multiplier)
	for box in range(1,len(box_list)+1):
		#print(box*multiplier)
		if(box*multiplier-1<no_of_person):
			if(box_list[box*multiplier-1])==0:
				box_list[box*multiplier-1]=1
			else:
				box_list[box*multiplier-1]=0
	multiplier+=1
	print(box_list)