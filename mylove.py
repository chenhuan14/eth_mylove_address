#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import threading
import commands
import sys
 
exitFlag = 0

mylove_first = "666"

mylove_last = ""

 
class myThread (threading.Thread):   
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):  
        find_add(self.name)


def find_add(threadName):
    count = 1
    global exitFlag

    while(1):               
        if exitFlag :
            break
        status, result = commands.getstatusoutput('geth account new --password passwd --keystore ' + threadName)
        address = result[result.find("{")+1:-1]
        first = address[0:len(mylove_first)]

        if len(mylove_last) > 0:
            last = address[0-len(mylove_last):]
        else:
            last = ""

        print address
        count = count + 1

        if first == mylove_first and last == mylove_last:
            print ("find it in " + threadName)
            exitFlag = 1
            break
        if count % 5 == 0:
            commands.getstatusoutput('rm -rf ' + threadName)
    

threads = []
# 创建新线程
for i in range(3):
    thread = myThread(i, "Thread-"+str(i))
    threads.append(thread)

for t in threads:
    t.start()









 