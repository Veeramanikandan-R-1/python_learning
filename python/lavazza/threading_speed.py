import speed_test2,json,threading,time
from filelock import FileLock
filepath="speed_details.json"
lockpath=filepath+".lock"
lock=FileLock(lockpath)
count=0
def updating_json():
    try:
        while True:
            speed_data=speed_test2.conn_speed()
            if speed_data:
                with lock:
                    with open("speed_details.json","w") as file:
                        file.write(json.dumps(speed_data))
            else:
                continue
            time.sleep(1)
    except Exception as error:
        print("error occured while updating json ==> {}".format(error))

def reading_json():
    try:
        while True:
            with lock:
                with open("speed_details.json","r") as file:
                    print(file.read())
            time.sleep(60)
    except Exception as error:
        print("error occured while reading json ==> {}".format(error))

thread1=threading.Thread(target=updating_json)
thread2=threading.Thread(target=reading_json)
thread1.start()
thread2.start()

