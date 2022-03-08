import json,os
import logging
import threading

import lock
from filelock import FileLock

from common_macros import write_event,write_receiving_queue
class basic_functions():
    def read_json(file_path):
        try:
            if (os.path.isfile(file_path)):
                with FileLock(file_path + ".lock"):
                    with open(file_path, "r") as read_file:
                        json_content = json.loads(read_file.read())
                        return json_content
        except Exception as error:
            # print('file is empty')
            return 'Failure'

    def write_json(file_path,content):
        try:
            if (os.path.isfile(file_path)):
                with FileLock(file_path + ".lock"):
                    with open(file_path, "w") as file:
                        file.write(json.dumps(content,indent=4))
                        return 'success'
            else:
                with FileLock(file_path + ".lock"):
                    with open(file_path, "w") as file:
                        file.write(json.dump(content,indent=4))
                        return 'success'
        except Exception as error:
            # print('file is empty')
            return 'Failure'

common_functions=basic_functions()


def write_json(file_path, content):
    try:
        if (os.path.isfile(file_path)):
            with FileLock(file_path + ".lock"):
                with open(file_path, "w") as file:
                    file.write(json.dumps(content, indent=4))
                    return 'success'
        else:
            with FileLock(file_path + ".lock"):
                with open(file_path, "w") as file:
                    file.write(json.dump(content, indent=4))
                    return 'success'
    except Exception as error:
        # print('file is empty')
        return 'Failure'


def file_write_fun():
    while True:
        write_event.wait()
        received_data = json.loads(write_receiving_queue.receive(timeout=60*60)[0].decode())
        print(received_data["file_path"],received_data['Data'])
        write_json(received_data["file_path"],received_data["Data"])
        write_event.clear()

file_write_thread=threading.Thread(target=file_write_fun)
file_write_thread.start()