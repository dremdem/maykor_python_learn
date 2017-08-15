import threading
import time




def hello():
    print("hello, Timer")

if __name__ == '__main__':
    t = threading.Timer(3.0, hello)
    t.start()
    print 'hey!'
    time.sleep(1)
    print 'hey2!'
