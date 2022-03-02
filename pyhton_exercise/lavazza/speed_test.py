from subprocess import Popen,PIPE
import datetime,re,traceback,codecs,json,threading,time,getpass
from filelock import FileLock

def command_execute_function(cmd):
    try:
        process=Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE,universal_newlines=True)
        global stdout,stderr
        if cmd=="/root/mani/lavazza/lavazza_self/speed_test/final/speed_final/speedtest":
            try:
                #pwd = getpass.getpass()
                #process.stdin.write("{}\n".format(pwd))
                stdout,stderr=process.communicate()
                #stdout,stderr=process.communicate(input="{}\n".format("yes")) #to give yes as response
            except:
                #stdout,stderr=process.communicate()
                print("no response required")
        else:    
            stdout,stderr=process.communicate()
        p_status=process.wait() #to get output only after command executed successfully
        if stderr:
            print("error occured while executing command : {} ==> {}".format(cmd,stderr))
        elif stdout:
            print("command : {} ==> executed successfully".format(cmd))
    except:
        print("error occured while executing cmd ==> {}".format(traceback.format_exc()))


def finding_connection_speed():
    try:
        #command_execute_function("sudo pip3 install speedtest-cli")  #to install speed-test-cli module will be called in threading py
        command_execute_function("/root/mani/lavazza/lavazza_self/speed_test/final/speed_final/speedtest") #to get connection speed output
        result=stdout
        result=str(stdout).replace("b","",1) #to convert from bits to string
        result=(codecs.decode(result,'unicode_escape')) #decodes the raw string to normal string
        result=re.findall("[Download|Upload].*.Mbps",result) 
        connection_details={} 
        connection_details["time_tested"]=(datetime.datetime.now()).strftime("%H:%M:%S")
        list_len=len(result)
        if list_len>1:
            for word_index in range(list_len): 
                #to take required parameters alone from the result list
                word_after_split=result[word_index].split(":")
                connection_details[word_after_split[0]]=word_after_split[1].strip()
        else:
            connection_details["Download"]="0.00 Mbps"
            connection_details["Upload"]="0.00 Mbps"

        return connection_details

    except Exception as error:
        print("error occured while executing cmd ==> {}".format(error))

filepath="speed_details.json"
lockpath=filepath+".lock"
lock=FileLock(lockpath)
#from lavazza_cfds_server_communication_macros import BASE_DIRECTORY
#SPEED_DETAILS_FILE_PATH=BASE_DIRECTORY + "src/configs/feature_configs/speed_details.json"
def updating_json():
    try:
        command_execute_function("chmod 777 speedtest")
        while True:
            speed_data=finding_connection_speed()
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
            time.sleep(30)
    except Exception as error:
        print("error occured while reading json ==> {}".format(error))

thread1=threading.Thread(target=updating_json)
thread2=threading.Thread(target=reading_json)
thread1.start()
thread2.start()


