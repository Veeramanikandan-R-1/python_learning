from filelock import FileLock,Timeout
file_path="sample.txt"
lock_path="sample.txt.lock"

lock=FileLock(lock_path,timeout=1)
# recursive locks
def cite1():
    with lock:
        open(file_path,'a').write('\nneww message')

def cite2():
    with lock:
        open(file_path,'a').write('\nnews message')
# lock acquired here
with lock.acquire(10):
    cite1()
    cite2()
# lock released here