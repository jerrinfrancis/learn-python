#!/usr/bin/env python3
import threading
import time

global_resource = 0
tool = threading.Lock()

def edit_resource():
    global global_resource
    for i in range(5):
        print(threading.current_thread().getName(), 'is editing')
        time.sleep(0.5)
        tool.acquire()
        global_resource += 1
        tool.release()

if __name__ == '__main__':
    threadA = threading.Thread(target=edit_resource)
    threadB = threading.Thread(target=edit_resource)
    threadA.start()
    threadB.start()
    threadA.join()
    threadB.join()
    print('Global Resource value is', global_resource)
