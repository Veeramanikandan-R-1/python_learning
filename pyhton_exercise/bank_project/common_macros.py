import os
import posix_ipc
from SystemEvent import SystemEvent

try:
    posix_ipc.unlink_message_queue('/msg3')
except:
    print('queue not created yet')

write_sending_queue=posix_ipc.MessageQueue(name="/msg3",flags=posix_ipc.O_CREX,max_messages=1)
write_receiving_queue=posix_ipc.MessageQueue(name="/msg3")
write_event=SystemEvent("rec_evt")

curr_path=os.getcwd()
user_detail_json_path=curr_path+'/{}'.format('user_details.json')
user_transaction_json_path=curr_path+'/{}'.format('transaction_history.json')
account_no_json_path=curr_path+'/{}'.format('account_no.json')