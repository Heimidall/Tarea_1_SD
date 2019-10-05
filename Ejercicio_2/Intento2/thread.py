import threading

timer = None

def wuf ():
    global timer
    print ("Wuf-wuf! ===================================")
    timer = threading.Timer(1, wuf)
    timer.start()

timer = threading.Timer(1, wuf)
flag = True
timer.start()
while flag:
    print("Sot el main \n")

