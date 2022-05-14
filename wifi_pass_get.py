from importlib.util import spec_from_file_location
import subprocess as sp
import re

common_output = sp.getoutput('netsh wlan show profile')
networks = re.findall(': .*',common_output)

networks_list = [network[2:] for network in networks]
password_outputs = []
for network in networks_list :
    password_outputs.append(sp.getoutput(f'netsh wlan show profile name="{network}" key=clear'))

password_list = []
for text in password_outputs :
    if("Key Content" in text):
        password_string = re.search('Key Content .*: .*',text)
        temp_string = password_string.group()
        temp_list = temp_string.split(': ')
        password_list.append(temp_list[1])
print(password_list)    
Final_output ={networks_list[each] : password_list[each] for each in range(len(networks_list))}
for ssid,password in Final_output.items() :
    print(ssid,'-->',password)