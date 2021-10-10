from filelock import Timeout,FileLock
lock=FileLock("file_sam.txt.lock")

def cite1():
    with lock:
        open("file_sam.txt", "a").write("I hate it when he does that.")

def cite2():
    with lock:
        open("file_sam.txt", "a").write("You don't want to sell me death sticks.")

# The lock is acquired here.
with lock:
    cite1()
    cite2()

# And released here.