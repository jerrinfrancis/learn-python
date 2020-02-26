import threading
import time

def daemon_work():
    while True:
        print('Daemon Thread executes')
        time.sleep(1)

if __name__ == '__main__':
    print('Main thread starts and begines daemon thread')
    daemon_thread = threading.Thread(target=daemon_work)
    daemon_thread.daemon = True
    daemon_thread.start()

    print('Main thread does work')
    time.sleep(0.6)
    print('Main thread does work')
    time.sleep(0.6)
    print('Main thread does work')
    time.sleep(0.6)
    print('Main thread does work')
