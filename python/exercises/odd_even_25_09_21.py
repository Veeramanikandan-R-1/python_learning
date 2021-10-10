def method1():
	input_times = int(input("no of inputs\n"))
	type_list = []
	times_list = []
	result_list = []
	for i in range(input_times):
		input_given1=input("enter type and number of times\n")
		input_given=input_given1.split(' ')
		type_list.append(input_given[0])
		times_list.append(input_given[-1])
	print(type_list)
	print(times_list)
	for entry in range(input_times):
		if(type_list[entry]=="odd"):
			count=1
			i=1
			while (count<=int(times_list[entry])):
				if((i%2)!=0):
					print(i)
					count+=1
				i+=1
		elif(type_list[entry]=="even"):
			count=1
			i=1
			while (count<=int(times_list[entry])):
				if((i%2)==0):
					print(i)
					count+=1
				i+=1

# method1()
def method2():
	input_times = int(input("no of inputs\n"))
	time_type_dict={}
	for entry in range(input_times):
		input_string=input('enter a type and times\n').split(" ")
		time_type_dict[input_string[0]]=input_string[-1]
	print(time_type_dict)

method2()
