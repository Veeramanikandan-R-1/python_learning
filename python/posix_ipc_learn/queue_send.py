import posix_ipc,time,json
from SystemEvent import SystemEvent
# sending_evt=SystemEvent("send_evt")
# sending_evt.wait()
try:
    posix_ipc.unlink_message_queue('/msg3')
except:
    print('queue not created yet')
sending_queue=posix_ipc.MessageQueue(name="/msg3",flags=posix_ipc.O_CREX,max_messages=1)
while True:
    try:
        sending_queue.send(json.dumps("mani").encode(), timeout=60)
        rec_evt = SystemEvent("rec_evt")
        rec_evt.set()
        # time.sleep(5)
    except Exception as error:
        print(error)
