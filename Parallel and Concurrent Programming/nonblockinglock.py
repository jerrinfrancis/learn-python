import threading
import time

global_resource = 0

tool = threading.Lock()

def increment_global_resource():
    global global_resource
    name = threading.current_thread().getName()
    counter = 0
    while global_resource <= 20:
        if counter and tool.acquire(blocking=False):
            global_resource += counter
            print(name, 'incremented global resource by ', counter,)
            counter = 0
            time.sleep(0.3)
            tool.release()
        else:
            time.sleep(0.1)
            counter += 1
            print(name, 'incrementing counter')

if __name__ == '__main__':
    threadA  = threading.Thread(target=increment_global_resource, name='Thread A')
    threadB = threading.Thread(target=increment_global_resource, name= 'Thread B')
    start_time = time.perf_counter()
    threadA.start()
    threadB.start()
    threadA.join()
    threadB.join()
    elapsed_time = time.perf_counter() - start_time
    print('Elapsed Time: {:.2f} seconds'.format(elapsed_time))