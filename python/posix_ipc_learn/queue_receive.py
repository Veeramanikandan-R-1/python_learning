import posix_ipc,time,json
import SystemEvent
rec_event=SystemEvent.SystemEvent("rec_evt")
rec_event.wait()
receiving_queue=posix_ipc.MessageQueue(name="/msg3")
# while True:
received_data = json.loads(receiving_queue.receive(timeout=60)[0].decode())
print(received_data)
#time.sleep(5)
rec_event.clear()
