from filelock import FileLock,Timeout
file_path="sample.txt"
lock_path="sample.txt.lock"

lock=FileLock(lock_path,timeout=1)

with lock:
    open(file_path,'a').write('\n first message')

try:
    with lock.acquire(timeout=10):
        open(file_path,'a').write('\n new message')
except Timeout:
    print('other instance of the machine holds the lock')