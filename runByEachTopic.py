#encoding=utf-8

'''
Created on Oct 26, 2016

@author: lzh
'''

import os
import fnmatch
import  sys 
reload(sys)
sys.setdefaultencoding("utf-8")

PATH = u"/home/lzh/Documents/SinoCoreferencer/突发事件/"
testLoc = "/home/lzh/Documents/SinoCoreferencer/test"

def traverseDirByListdir(path, testloc):
    childfiles = []
    for dirpath, dirpathnames, filenames in os.walk(PATH):
        for each in dirpathnames:
            childfile = os.path.join(dirpath, each)
            childfiles.append(childfile)
    for childfile in childfiles:
        out = open(testloc, 'w')
        files = []
        doc = ''
        for dirpath, dirpathnames, filenames in os.walk(childfile):
            doc = dirpath
            files = filenames
        for File in files:
            out = open(testloc, 'w')
            absoulePath = os.path.join(doc, File).encode('utf-8')
            print absoulePath
            out.write(absoulePath+'\n')
            out.flush()
        
            os.chdir("/home/lzh/Documents/SinoCoreferencer/")
            os.system("./run.sh test")
#         os.chdir("/home/lzh/workspace/eventcoreference")
        
    
traverseDirByListdir(PATH,testLoc)