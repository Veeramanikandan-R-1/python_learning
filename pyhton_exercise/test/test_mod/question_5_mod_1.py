# question
# to pass command="ipconfig /all" and store result in a dictionary and covert to json and store in a json file

# answer
import subprocess
import json
command="ipconfig /all"
output=subprocess.run(command,shell=True,text=True,stdout=subprocess.PIPE)
output_str=output.stdout
#print(type(output_str))
output_str=output_str.split("\n")
#print(output_str)
output_list=[line for line in output_str if(line !="")] #to remove blank lines
#for i in output_list:
#	print(i)
#keys=[]
output_dict={} 
for i in output_list:
	#print(i[0])
	#print(len(i[0]))
	if(i[0]!=" "): #to get first key(outer key)	
		if(":" in i):
			a_1=i.replace(":","") #to remove ':" attached to some keys alone
			output_dict[a_1]={}
			j=a_1 #to pass outer key to map inner key values
		#keys.append(i)
		else:
			output_dict[i]={}
			j=i
	if((":" in i) and (i[0]==" ")): #to process the inner keys and values
		#print(i)
		list1=i.split(":") # separating inner key and values
		keys=(list1[0])
		#keys.strip()
		new_key=''
		for letter in keys: #to remove all "." in keys
			if(letter!="."):
				new_key+=letter
		if(":" in new_key): #removing ":" in keys if present
			a_2=i.replace(":","")
			new_key_1=a_2
		else:
			new_key_1=new_key
		#print(new_key_1)
		values=list1[len(list1)-1]
		(output_dict[j])[new_key_1.strip()]=values #assigning key value pairs to key taken above
			
#print(output_dict)
#for x,y in output_dict.items():
#	print(x,y)
#	print("\n")

output_dict_json_format=json.dumps(output_dict,indent=4)
#print(output_dict_json_format)
#print(output_dict["Wireless LAN adapter Wi-Fi"])

file=open("output.json","w")
file.write("output for command : ipconfig /all \n")
file.write(output_dict_json_format)
file.close()