#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import threading
import subprocess
import sys
import os
 
exitFlag = 0

mylove_first = ""

mylove_last = "8"

 
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
        if exitFlag:
            break
			
        cmd ='geth.exe account new --password passwd --keystore ' + threadName
        ret = subprocess.Popen(cmd, shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = ret.communicate()
		
        add = str(result[0],encoding="utf8")

        address = add[add.find("{")+1:-2]
        first = address[0:len(mylove_first)]

        if len(mylove_last) > 0:
            last = address[0-len(mylove_last):]
        else:
            last = ""

        print (address)
        count = count + 1

        if first == mylove_first and last == mylove_last:
            print ("find it in " + threadName)
            exitFlag = 1
            break
			
        if count % 5 == 0:
            cwd = os.getcwd()
            del_file(cwd+'\\'+threadName)


def del_file(path):
    for i in os.listdir(path):
        path_file=os.path.join(path,i)
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            del_file(path_file)		

threads = []
# 创建新线程
for i in range(10):
    thread = myThread(i, "Thread-"+str(i))
    threads.append(thread)

for t in threads:
    t.start()









 