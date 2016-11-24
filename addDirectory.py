#encoding=utf-8

'''
Created on Nov 24, 2016

@author: lzh
'''
import os

PATH = u"/home/lzh/Desktop/突发事件/社会安全"
def AddDirectory():    
    childfiles = []
    for dirpath, dirpathnames, filenames in os.walk(PATH):
        for each in dirpathnames:
            childfile = os.path.join(dirpath, each)
#             print childfile
            for childpath, childpathnames, childfilenames in os.walk(childfile):
#                 print childfilenames
                diretory_pos = os.path.join(childpath, 'directory.all')
                f_dir = open(diretory_pos, 'w')
                for child in childfilenames:
                    f_dir.write(child + '\n')
AddDirectory()