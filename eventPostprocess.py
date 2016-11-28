#encoding=utf-8

'''
Created on Nov 23, 2016

@author: lzh
'''

import os
from util import read_all_lines
import sys
from bokeh.charts.builders.line_builder import Line
reload(sys)
sys.setdefaultencoding('utf-8')

def InputProcess(inputFile):
    
    input_lines = read_all_lines(inputFile)
    
    attr_set = []
    attr = []
    for line in input_lines:
        pos_set = []
        for i in range(len(attr_set)):
            pos_set.append(attr_set[i][2])
        attr = line.strip().split('|')
        word = attr[0].split('，')   
        attr[0] = word[0]

        if attr[2] in pos_set:
            for i in range(len(attr_set)):
                if attr[2] == attr_set[i][2]:
                    attr_set[i].append(word[1])
#                     attr_set[i].append(word[2])
        else:
            attr.append(word[1])
#             attr.append(word[2])            
            attr_set.append(attr)
#     for a in attr_set:
#         print a 
    return attr_set

def FileGeneration(Destination, inputFile, file):
    
    '''
    create file un-contained
    '''
    arg = os.path.join(Destination,"%s.arg" % file)
    entities = os.path.join(Destination, '%s.coref.entities' % file)
    timeFile = os.path.join(Destination, '%s.time' % file)
    trigger = os.path.join(Destination, '%s.trigger' % file)
    typeFile = os.path.join(Destination, '%s.type' % file)
    valueFile = os.path.join(Destination, '%s.value' % file)
    xmlFile = os.path.join(Destination, '%s.xml' % file)
    
#     all attributes extracted from '.out' file
    
    attr_set = InputProcess(inputFile)
    
    '''
    add event attributes
    '''
    f_arg = open(arg, 'w')

    for attr in attr_set:
        try:
            f_arg.write("==================\n")
            length = len(attr[0])
            line = attr[2] + ',' + str(int(attr[2])+length-1) + ' ' + attr[1] + ' ' + attr[0] + '\n'
            f_arg.write(line)
            
    #         add place feature
            length_place = len(attr[9])
            if attr[9] != 'NULL':
                line = attr[10] + ',' + str(int(attr[10])+length_place-1) + ' place ' + attr[9] + '\n'
                f_arg.write(line)
                
    #         Add time Feature
            length_time = len(attr[7])        
            if attr[7] != 'NULL':
                line = attr[8] + ',' + str(int(attr[8])+length_time-1) + ' time ' + attr[7] + '\n'
                f_arg.write(line)
            
#             add relation feature   
#             for i in range(11,len(attr)):
#                 relation = attr[i].split('：')
#                 pos1 = attr[4].index(relation[1])
#                 pos2 = attr[4].index(attr[0])
#                 length_relation = len(relation[1])
#                 start_pos = int(attr[2])+pos1-pos2
#                 line = str(start_pos) + ',' + str(start_pos+length_relation-1) + ' ' + relation[0] + ' ' + relation[1] + '\n'
#                 f_arg.write(line)
                    
            if not os.path.exists(entities):
                open(entities, 'w')
            
        
            f_time = open(timeFile, 'w')
            for attr in attr_set:
                length = len(attr[7])
                if attr[7] != 'NULL':
                    line = attr[8] + ',' + str(int(attr[8])+length-1) + ' time time ' + attr[7] + '\n'
                    f_time.write(line)
                
         
            f_trigger = open(trigger, 'w')
            for attr in attr_set:
                length = len(attr[0])
                line = attr[2] + ',' + str(int(attr[2])+length-1) + ' ' + attr[1] + ' ' + attr[0] + '\n'
                f_trigger.write(line)
            
            
            if not os.path.exists(typeFile):
                open(typeFile, 'w')
                
            if not os.path.exists(valueFile):
                open(valueFile, 'w')
        except Exception,e:  
            print Exception,":",e            
            continue
        
def EventCoreference():
    '''
    event coreference within a second-file
    '''
    PATH = u"/home/lzh/Documents/SinoCoreferencer/突发事件/社会安全"
    testLoc = "/home/lzh/Documents/SinoCoreferencer/test"
  
    childfiles = []
    for dirpath, dirpathnames, filenames in os.walk(PATH):
        for each in dirpathnames:
            childfile = os.path.join(dirpath, each)
            directory = os.path.join(childfile, 'directory.all')
            dir_lines = read_all_lines(directory)
            for line in dir_lines:
                
                f_test = open(testLoc, 'w')
                absoulePath = os.path.join(childfile, line).encode('utf-8')
                print absoulePath
                f_test.write(absoulePath+'\n')
                f_test.flush()
                
                input_file = line + '.shtml.out'
                each_input  = each + '_'
                input_dir = os.path.join('/home/lzh/Downloads/data/', each_input, input_file)
                FileGeneration(childfile, input_dir, line)
                

                os.chdir("/home/lzh/Documents/SinoCoreferencer/")
                os.system("./run-coreference.sh test")
                
def CombineCoreference(Destination, file):

    arg_file = file + '.arg'
    arg_dir = os.path.join(Destination, arg_file)
    arg_lines = read_all_lines(arg_dir)
    coref_file = file + '.coref.events'
    coref_dir = os.path.join(Destination, coref_file)
    coref_lines = read_all_lines(coref_dir)
    coref_attr_file = file + '.coreference'
    coref_attr_dir = os.path.join(Destination, coref_attr_file)
    f_coref = open(coref_attr_dir, 'w')
    
    temp = []
    temp_attr = []
    for coref_line in coref_lines:
        if coref_line != '============':
            try:
                temp.append(coref_line)
                pos = arg_lines.index(coref_line)
                for i in range(pos+1,len(arg_lines)):
                    if arg_lines[i] != ('=================='):
                        temp_attr.append(arg_lines[i])
                    else:
                        break
            except Exception,e:
                print Exception, ':', e

        else:
            f_coref.write('='*18+'\n')
            for t in temp:
                f_coref.write(t+'\n')
            f_coref.write('*'*18+'\n')
            for t in temp_attr:
                f_coref.write(t+'\n')
                         
            temp = []
            temp_attr = []
                        
def CombineAllCoreference():
    '''
    process all files contained
    '''
    PATH = u"/home/lzh/Documents/SinoCoreferencer/突发事件/社会安全"

    childfiles = []
    for dirpath, dirpathnames, filenames in os.walk(PATH):
        for each in dirpathnames:
            childpath = os.path.join(dirpath, each)
            directory = os.path.join(childpath, 'directory.all')
            dir_lines = read_all_lines(directory)
            for line in dir_lines:
                print childpath
                print line
                CombineCoreference(childpath, line)
                                        
if __name__ == '__main__':
    EventCoreference()
#     CombineAllCoreference()
#     CombineCoreference('/home/lzh/Documents/SinoCoreferencer/突发事件/社会安全/topic62/','n454056663')
#     FileGeneration('/home/lzh/Documents/SinoCoreferencer/突发事件/社会安全/topic62/', '/home/lzh/Downloads/data/topic62_/n454062273.shtml.out', 'n454062273')
    print("Done!")