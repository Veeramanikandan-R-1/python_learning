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
#for i in output_str:
#	i.strip()
#output_str=output_str.strip()
output_str.remove("")
#print(output_str)
json_format=json.dumps(output_str,indent=4)
#print(json_format)
file=open("output.json","w")
file.write("output for command : ipconfig /all \n")
file.write(json_format)
file.close()