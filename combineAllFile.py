#encoding=utf-8

'''
Created on Nov 8, 2016

@author: lzh
'''

import os
import shutil

PATH = u'/home/lzh/Documents/SinoCoreferencer/突发事件/事故灾难/topic19/'
DESTINATION = u'/home/lzh/Documents/SinoCoreferencer/topic19/'
AllFiles = []

for dir, dirpathnames, filenames in os.walk(PATH):
    AllFiles = filenames



for file in AllFiles:
    filepath = os.path.join(PATH, file)
#     print filepath
    desfile = os.path.join(DESTINATION, file)
    if os.path.exists(desfile):
        continue
    else:
        shutil.move(filepath, DESTINATION)



