import threading
import time

class secondThread(threading.Thread):
    def __init__(self):
        super().__init__()
    
    def run(self):
        print('Second thread started and doing its job')
        time.sleep(3)
        print('second thread completed the jon')

# main thread
if __name__ == '__main__':
    print('Main thread started and requesting second thread for work')
    second_thread = secondThread()
    print('Second thread Alive?:', second_thread.is_alive())

    print('Main thread asks the second thread to start')
    second_thread.start()
    print('Second thread Alive?:', second_thread.is_alive())

    print('Main thread continues with its work')
    time.sleep(0.5)
    print('Second thread Alive?:', second_thread.is_alive())

    print('Main thread finishes its job and waits for second thread to finish')
    second_thread.join()
    print('Second thread Alive?:', second_thread.is_alive())

    print('Both the threads finish their jobs')