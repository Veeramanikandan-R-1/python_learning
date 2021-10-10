from filelock import FileLock
lock=FileLock("sample.txt.lock")
with lock:
    open("sample.txt",'a').write('sample') # a for appending r for reading r+ for read and write and w for writing