from filelock import FileLock,Timeout
file_path='sample.txt'
lock_path='sample.txt.lock'
lock=FileLock(lock_path,timeout=1)
# with lock:
#     open(file_path,'a').write('updated')
# lock.acquire()
# try:
#     open(file_path, 'a').write('mani')
# finally:
#     lock.release()

def cite1():
    with lock:
        open(file_path, "w").write("I hate it when he does that.")

def cite2():
    with lock:
        open(file_path, "w").write("You don't want to sell me death sticks.")

# The lock is acquired here.
with lock:
    cite1()
    cite2()

# And released here.