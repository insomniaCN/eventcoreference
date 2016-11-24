#encoding=utf-8

'''
Created on Nov 23, 2016

@author: lzh
'''

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def FileGeneration(Destination, inputFile):
    
    '''
    create file un-contained
    '''
    arg = os.path.join(Destination,".arg")
    entities = os.path.join(Destination, '.coref.entities')
    timeFile = os.path.join(Destination, '.time')
    trigger = os.path.join(Destination, '.trigger')
    typeFile = os.path.join(Destination, '.type')
    valueFile = os.path.join(Destination, '.value')
    xmlFile = os.path.join(Destination, '.xml')
    
    '''
    arg
    '''
    
    
    if not os.path.exists(entities):
        open(entities, 'w')
    
    '''
    timeFile
    '''
    
    '''
    trigger
    '''
    
    
    if not os.path.exists(typeFile):
        open(typeFile, 'w')
        
    if not os.path.exists(valueFile):
        open(valueFile, 'w')
     