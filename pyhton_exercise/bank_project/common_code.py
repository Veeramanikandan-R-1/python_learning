import json,os
import logging


class basic_functions():
    def read_json(file_path):
        try:
            if (os.path.isfile(file_path)):
                with open(file_path, "r") as read_file:
                    json_content = json.load(read_file)
                    return json_content
        except Exception as error:
            print('file is empty')
            return 'Failure'

    def write_json(file_path,content):
        try:
            if (os.path.isfile(file_path)):
                with open(file_path, "w") as file:
                    file.write(json.dumps(content,indent=4))
                    return 'success'
        except Exception as error:
            print('file is empty')
            return 'Failure'