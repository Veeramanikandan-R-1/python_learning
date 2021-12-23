import codecs,urllib.request
from subprocess import Popen,PIPE


def internet_connectivity_status_function(): #to check internet connection to the device
    def connect(host="http://google.com"):
        try:
            urllib.request.urlopen(host)
            return True
        except:
            return False
    if connect():
        print("internet is connected")
        return True
    else:
        print("no active internet  ")
        return False

def command_execute_function(cmd):
    try:
        process=Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE)
        global stdout,stderr
        stdout,stderr=process.communicate()
        if stderr:
            print("error occured while executing command : {} ==> {}".format(cmd,stderr))
        elif stdout:
            print("command : {} ==> executed successfully".format(cmd))
    except Exception as error:
        print("error occured while executing command : {} ==> {}".format(cmd,error))

def finding_connection_speed():
    try:
        command_execute_function("sudo pip3 install speedtest-cli")  #to install speed-test-cli module
        command_execute_function("speedtest") #to get connection speed output

        result=str(stdout).replace("b","",1) #to convert from bits to string
        result=(codecs.decode(result,'unicode_escape')).split("\n") #decodes the raw string to normal string
        connection_details={} 
        for word in result: 
            #to take required parameters alone from the result list
            if result.index(word)==1:
                connection_details["network_tested"]=word.rstrip(".") 
            elif result.index(word)==6:
                connection_details["download_speed"]=word.split(":")[1]
            elif result.index(word)==8:
                connection_details["upload_speed"]=word.split(":")[1]
        return connection_details

    except Exception as error:
        print("error occured while checking connection speed ==> {error}")

if internet_connectivity_status_function():
    print(finding_connection_speed())
else:
    print("no active connection")


