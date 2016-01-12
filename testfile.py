#!/usr/bin/python
#coding=utf-8
import time
import os
import sys
import hashlib
import platform
import threading
import random
from datetime import datetime
import re
#m=hashlib.md5()
#随机生成测试目标和文件大小
path=sys.argv[1]
startsize=int(sys.argv[2])
endsize=int(sys.argv[3])
targets = []
sizes=[]
FileList = []
pw = re.compile(r'(\w)(:)\\(.*)\\')
pl = re.compile(r'/(\w+)/(.*)')
if platform.system() == "Linux":
        matchs = pl.findall(path)
        if matchs:
            pass
        else:
            print "The system is Linux,please input liunx format.example:/var/log/test-log/"
            sys.exit(1)
if platform.system() == "Windows":
    matchs=pw.findall(path)
    if matchs:
        pass
    else:
        print "The system is Windows,please input windows format.example:d:\\test\\log"
        sys.exit(1)
if os.path.exists(path):
        pass
else:
        os.makedirs(path)

for i in xrange(startsize,endsize):
        filename=hashlib.md5(str(i)).hexdigest()
        target = path+filename
        targets.append(target)
        size=random.randint(startsize,endsize)
        sizes.append(size)
#随机测试的类
class Random_Write(threading.Thread):
        """随机生成文件的大小,并且写入磁盘"""
        def __init__(self, target,size):
                threading.Thread.__init__(self)
                self.target=target
                self.size=size

        def Random_test_writefile(self):
                print "Writing test file" + self.target +" " + str(self.size)
                t1 = datetime.utcnow()
                f=file(self.target,'wb')
                filesize=self.size*1024
                f.write('\x00'*filesize)
                timeused = datetime.utcnow() - t1
                print "File size is %.2f Kbytes Write to file for :%.4f Millisecond" %(filesize/1024,timeused.microseconds/1000)
                f.flush()
                f.close()
                FileList.append(self.target)

        def run(self):
            self.Random_test_writefile()
if __name__ == "__main__":
    getThreads = []
#对每个文件开启一个线程进行文件写入
for i in range(len(targets)):
    t = Random_Write(targets[i],sizes[i])
    getThreads.append(t)

for i in range(len(getThreads)):
    getThreads[i].start()
    print "Current active thread number is %d" %threading.activeCount()

for i in range(len(getThreads)):
    getThreads[i].join()

print '.'*10+"总共写入了%s个文件" %len(FileList) +'.'*10