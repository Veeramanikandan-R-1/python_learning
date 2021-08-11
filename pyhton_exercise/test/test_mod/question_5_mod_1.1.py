# question
# to pass command="ipconfig /all" and store result in a dictionary and covert to json and store in a json file

# answer
import subprocess,json
command="ipconfig /all"
output=subprocess.run(command,shell=True,text=True,stdout=subprocess.PIPE)
output_str=output.stdout
output_str=output_str.split("\n") #spliting at newlines
output_list=[line for line in output_str if(line !="")] #to remove blank lines
output_dict={} 
for line in output_list:
	if(line[0]!=" "): #to get first key(outer key)	
		#print(line)
		if(":" in line):
			a_1=line.replace(":","") #to remove ':" attached to some keys alone
			output_dict[a_1]={}
			main_key=a_1 #to pass outer key to map inner key values
		else:	
			output_dict[line]={}
			main_key=line
	if((":" in line) and (line[0]==" ")): #to process the inner keys and values
		list1=line.split(":") # separating inner key and values
		keys=(list1[0])
		sub_key=''
		for letter in keys: #to remove all "." in keys
			if(letter!="."):
				sub_key+=letter
		if(":" in sub_key): #removing ":" in keys if present
			a_2=line.replace(":","")
			sub_key_final=a_2
		else:
			sub_key_final=sub_key
		values=(list1[len(list1)-1]).strip()
		(output_dict[main_key])[sub_key_final.strip()]=values #assigning key value pairs to key taken above
			

output_dict_json_format=json.dumps(output_dict,indent=4) #to convert dictionary to json string

file=open("output.json","w") #to write in a file
file.write("output for command : ipconfig /all \n")
file.write(output_dict_json_format)
file.close()