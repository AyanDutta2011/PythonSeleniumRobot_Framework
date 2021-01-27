#by default every code has one thread, called as Main Thread.
#by this method we can use multiple cores of CPU and can execute things simultaniously.

from time import *
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()     #it will ask main thread to wait till t1 and t2 complete their task
t2.join()

print("Bye")
