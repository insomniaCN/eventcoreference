#coding=utf-8
'''
Created on Oct 26, 2016

@author: lzh
'''
import os
import fnmatch
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


PATH = u"/home/lzh/Documents/SinoCoreferencer/事件类型/突发事件"

def multiProcess(path):
    path = os.path.expanduser(path)
    for (dirname, subdir, subfile) in os.walk(path):
        for f in subfile:
            childpath = os.path.join(dirname, f)
            if  fnmatch.fnmatch(childpath,  '*.shtml'):
                newDoc = f.strip().split('.')[0]
                fwrite = open(os.path.join(dirname ,newDoc), 'wb')
                fopen = open(childpath, 'rb')
                Done = 1
                while Done:
                    temp = fopen.readline()
                    if temp:
                        if not str(temp).startswith('URL'):
                            fwrite.write(temp)
                    else:
                        Done = 0
                os.remove(childpath)

multiProcess(PATH)