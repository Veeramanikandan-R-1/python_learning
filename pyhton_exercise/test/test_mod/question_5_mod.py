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
output_list=[line for line in output_str if(line !="")]
#print(output_list)
window_ip_config={} 
for i in output_list:
	if(":" in i):
		list1=i.split(":")
		keys=(list1[0])
		#keys.strip()
		new_key=''
		for letter in keys:
			if(letter!="."):
				new_key+=letter
		values=list1[len(list1)-1]
		window_ip_config[new_key.strip()]=values
for keys,values in window_ip_config.items():
	print(keys,":",values)
#print(window_ip_config["IPv4 Address"])

window_ip_config_json_format=json.dumps(window_ip_config) #to covert python dictionary to json format

file=open("output.json","w")
file.write("output for command : ipconfig /all \n")
file.write(window_ip_config_json_format)
file.close()


	

	



