from filelock import FileLock,Timeout
file_path="sample.txt"
lock_path="sample.txt.lock"

lock=FileLock(lock_path,timeout=1)

with lock:
    open(file_path,'a').write('\n first message')
lock.acquire()
try:
    open(file_path,'a').write('\n second message')
finally:
    lock.release()