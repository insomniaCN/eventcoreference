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
import string

PATH = u"/home/lzh/Documents/SinoCoreferencer/突发事件"


def traverseDirByListdir(path):
    childfiles = []
    for dirpath, dirpathnames, filenames in os.walk(PATH):
        for each in dirpathnames:
            childfile = os.path.join(dirpath, each)
            childfiles.append(childfile)
    for childfile in childfiles:
        files = []
        doc = ''
        for dirpath, dirpathnames, filenames in os.walk(childfile):
            doc = dirpath
            files = filenames
        for File in files:
            absoulePath = os.path.join(doc, File).encode('utf-8')
            
              
            title_txt = open(absoulePath, 'rb+') 
            try:  
                full_txt = title_txt.readlines()  
                new_txt = []  
                for line in full_txt:  

                    if line.startswith('URL') or line.startswith('title') or line.startswith('time'):  
            #print "match", line  
                        continue  
                    else:  
                        new_txt.append(line[6:].strip())  
            
                title_txt.seek(0)  
                title_txt.truncate(0)  
    #for line in full_txt:  
    #    title_txt.writelines(line)  
                title_txt.writelines(new_txt)  
      
            finally:  
                title_txt.close()  
  
            print "Over" 
    
traverseDirByListdir(PATH)