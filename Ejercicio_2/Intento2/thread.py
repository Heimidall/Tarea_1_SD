import threading
import time

timer = None

def wuf ():
    global timer
    print ("Wuf-wuf! ===================================")
    timer = threading.Timer(2, wuf)
    timer.start()

timer = threading.Timer(2, wuf)
flag = True
timer.start()
while True:
    print("Sot el main \n")
    time.sleep(3)


