#encoding=utf-8

'''
Created on Nov 8, 2016

@author: lzh
'''

import os
import shutil

PATH = u'/home/lzh/Documents/SinoCoreferencer/突发事件/事故灾难/topic19/'
AllFiles = []

for dir, dirpathnames, filenames in os.walk(PATH):
    AllFiles = filenames

fileDict = {}

for file in AllFiles:
    original = file.strip().split('.')[0]
    if fileDict.has_key(original):
        fileDict[original] += 1
    else:
        fileDict[original] = 1

print fileDict
for (d,x) in fileDict.items():
    if x == 1:
        filepath = os.path.join(PATH, d)
        shutil.move(filepath, '/home/lzh/Documents/SinoCoreferencer/temp')


