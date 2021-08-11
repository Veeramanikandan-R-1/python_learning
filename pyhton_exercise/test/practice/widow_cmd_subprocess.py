import subprocess,json
command="systeminfo"
output=subprocess.run(command,shell=True,text=True,stdout=subprocess.PIPE)
#print(output.stdout)
output=output.stdout
output=output.split("\n")
output.remove("")
system_info_output={}
for lines in output:
	line_after_split=lines.split(":",1)
	if(len(lines)!=0):
		#print(len(lines),lines)
		#print(line_after_split[0],len(line_after_split[0]))
		#print((line_after_split[0])[0],len((line_after_split[0])[0]))
		if(((line_after_split[0])[0])!=" "):
			#print("yes")
			main_key=(line_after_split[0]).strip()
			main_value=(line_after_split[len(line_after_split)-1]).strip()
			system_info_output[main_key]={}
			system_info_output[main_key]=main_value
		else:
			#print(i,"test")
			sub_key=(line_after_split[0]).strip()
			sub_value=(line_after_split[len(line_after_split)-1]).strip()
			print(main_key)
			print(sub_key,sub_value)
			(system_info_output[main_key])={}
			(system_info_output[main_key])[sub_key]=(sub_value)
			#print(sub_dict)
		
#print(system_info_output)
for key,value in system_info_output.items():
	print(key,":",value)
	#print("\n")
output_dict_json_format=json.dumps(system_info_output,indent=4) #to convert dictionary to json string

file=open("output.json","w") #to write in a file
file.write("output for command : system info/all \n")
file.write(output_dict_json_format)
file.close()