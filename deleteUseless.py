#encoding=utf-8
'''
Created on Oct 28, 2016

@author: lzh
'''

import os
import time
time1 = time.time()
PATH = u"/home/lzh/Documents/SinoCoreferencer/突发事件/社会安全/topic62"

os.chdir(PATH)

os.system( "find . -name '*.arg.svm' -type f -print -exec rm -rf {} \;")
os.system( "find . -name '*.arg.svmpred' -type f -print -exec rm -rf {} \;")
os.system( "find . -name '*.arg.tmp' -type f -print -exec rm -rf {} \;")
os.system( "find . -name '*.evc.svm' -type f -print -exec rm -rf {} \;")
os.system( "find . -name '*.genericity.fea' -type f -print -exec rm -rf {} \;")
os.system( "find . -name '*.genericity.pred' -type f -print -exec rm -rf {} \;")
os.system( "find . -name '*.md.tmp' -type f -print -exec rm -rf {} \;")
os.system( "find . -name '*.modality.fea' -type f -print -exec rm -rf {} \;")
os.system( "find . -name '*.polarity.fea' -type f -print -exec rm -rf {} \;")
os.system( "find . -name '*.subtype.svmpred' -type f -print -exec rm -rf {} \;")
os.system( "find . -name '*.tense.fea' -type f -print -exec rm -rf {} \;")
os.system( "find . -name '*.tense.pred' -type f -print -exec rm -rf {} \;")
os.system( "find . -name '*.time.crf' -type f -print -exec rm -rf {} \;")
os.system( "find . -name '*.trigger.svm' -type f -print -exec rm -rf {} \;")
os.system( "find . -name '*.trigger.svmpred' -type f -print -exec rm -rf {} \;")
os.system( "find . -name '*.trigger.tmp' -type f -print -exec rm -rf {} \;")
os.system( "find . -name '*.type.svm' -type f -print -exec rm -rf {} \;")
os.system( "find . -name '*.type.svmpred' -type f -print -exec rm -rf {} \;")
os.system( "find . -name '*.type.tmp' -type f -print -exec rm -rf {} \;")
os.system( "find . -name '*.value.crf' -type f -print -exec rm -rf {} \;")
os.system( "find . -name '*.evc' -type f -print -exec rm -rf {} \;")
os.system( "find . -name '*.md.crf' -type f -print -exec rm -rf {} \;")

os.system( "find . -name '*.arg' -type f -print -exec rm -rf {} \;")
os.system( "find . -name '*.coref.events' -type f -print -exec rm -rf {} \;")
os.system( "find . -name '*.coreference2' -type f -print -exec rm -rf {} \;")
os.system( "find . -name '*.trigger' -type f -print -exec rm -rf {} \;")
os.system( "find . -name '*.time' -type f -print -exec rm -rf {} \;")
time2 = time.time()
t = time2 - time1

print("Time elapsed: %s" % t)
print("Done!")