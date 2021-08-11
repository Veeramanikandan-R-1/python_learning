import subprocess
formatted_ip_config_data = {}

ip_config_data = (subprocess.getoutput("ipconfig /all")).split("\n\n")

for i in range(len(ip_config_data)):
    if i % 2 != 0:
        formatted_ip_config_data[ip_config_data[i-1].strip().replace(":", "")] = ip_config_data[i].split("\n")


for key in formatted_ip_config_data.keys():

    property_dict = {}

    for i in formatted_ip_config_data[key]:
        split_value = i.split(":")
        property_dict[split_value[0].replace(".", "").strip()] = split_value[1].strip()

    formatted_ip_config_data[key] = property_dict

print(formatted_ip_config_data)