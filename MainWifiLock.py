import ctypes
import time
import subprocess
t = 0
while t == 0:
    print("Starting Everything")
    #Getting the wifi information and parsing
    results = subprocess.check_output(["netsh", "wlan", "show", "network"])
    results = results.decode("ascii") # needed in python 3
    results = results.replace("\r","")
    ls = results.split("\n")
    ls = ls[4:]
    ssids = []
    x = 0
    while x < len(ls):
        if x % 5 == 0:
            ssids.append(ls[x])
        x += 1
    size = len(ssids)

    #Making the ssids easier to compare
    CounterSsid = 0
    while CounterSsid < size:
        ssids[CounterSsid] = ssids[CounterSsid][8:]
        CounterSsid = CounterSsid + 1

    #Checking if the wanted network is available
    current = 0
    Result = 0
    print("Started Checking")
    while current < size:
        check = (" pwned")
        #print("Testing the following:")
        #print(check, ssids[current])
        if str(ssids[current]) == check:
            #print("Network has been found")
            current = 100
            Result = 1
        else:
            #print("not a match, moving on to the next comparison")
            current = current + 1

    if Result == 1: #This means that network has been found
        print("Network has been found, no need to lock computer")
        print("The process will repeat in 20 seconds")
    else:
        print("LOCKING COMPUTER1!!!!")
        ctypes.windll.user32.LockWorkStation()
    time.sleep(20)
