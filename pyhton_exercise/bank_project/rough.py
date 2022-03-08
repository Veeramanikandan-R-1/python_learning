import json

from common_macros import *
with open(user_detail_json_path,'r') as file:
    print(json.loads(file.read()))