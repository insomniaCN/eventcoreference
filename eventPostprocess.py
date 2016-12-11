#encoding=utf-8

'''
Created on Nov 23, 2016

@author: lzh
'''

import os
import collections
from util import read_all_lines
from attributeAnalysis import *
import sys

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

#     get news time    
    destination_file = os.path.join(Destination, file)
    news_time = ''
    child_body = read_all_lines(destination_file)
    for child_line in child_body:
        if child_line.strip().startswith("time:"):
            news_time = child_line[5:].strip()
    
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
                
#                 change time to standard formulate
#                 new_time = TimeRegularzation(news_time, attr[7])
#                 line = attr[8] + ',' + str(int(attr[8])+length_time-1) + ' time ' + new_time + '\n'

#                 without changing time
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
                    
                    new_time = TimeRegularzation(news_time, attr[7])
                    line = attr[8] + ',' + str(int(attr[8])+length-1) + ' time time ' + new_time + '\n'
#                     without changing time
#                     line = attr[8] + ',' + str(int(attr[8])+length-1) + ' time time ' + attr[7] + '\n'

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

def Post_arg(destination, inputFile, file):
    
    '''
    post process
    '''
    arg = os.path.join(destination,"%s.arg" % file)
     
#     all attributes extracted from '.out' file
    attr_set = InputProcess(inputFile)
    
#     get news time    
    destination_file = os.path.join(destination, file)
    news_time = ''
    child_body = read_all_lines(destination_file)
    for child_line in child_body:
        if child_line.strip().startswith("time:"):
            news_time = child_line[5:].strip()
    
#     post generate .arg file
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
                line = attr[10] + ',' + str(int(attr[10])+length_place-1) + '\t'+'place'+'\t' + attr[9] + '\n'
                f_arg.write(line)
                
    #         Add time Feature
            length_time = len(attr[7])        
            if attr[7] != 'NULL':
                
                new_time = TimeRegularzation(news_time, attr[7])
                line = attr[8] + ',' + str(int(attr[8])+length_time-1) +'\t'+'time'+'\t'+new_time+'\n'
#                     without changing time
#                 line = attr[8] + ',' + str(int(attr[8])+length_time-1) + ' time ' +  attr[7]+ '\n'

                f_arg.write(line)
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
                Post_arg(childfile, input_dir, line)

def writeCoreference(coref_lines, arg_lines, coref_attr_dir):
    '''
    write into file
    '''
    f_coref = open(coref_attr_dir, 'w')
    temp = []
    temp_attr = []
    time_attr = []
    
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
            if temp:
                f_coref.write('='*18+'\n')
                for t in temp:
                    f_coref.write(t+'\n')
                f_coref.write('*'*18+'\n')
            if temp_attr:
                for t in temp_attr:
                    f_coref.write(t+'\n')
            
def writeCoreference_v2(coref_lines, arg_lines, coref_attr_dir):
    '''
    write into file
    '''
    f_coref = open(coref_attr_dir, 'w')
    temp = {}
    time_attr = {}
    
    for coref_line in coref_lines:
        if coref_line != '============':

            temp.setdefault(coref_line,{})
            pos = arg_lines.index(coref_line)
            for i in range(pos+1,len(arg_lines)):
                if arg_lines[i] != ('=================='):
                    key, value = arg_lines[i].strip().split('\t')[1:3]
                    temp[coref_line][key] = value
                    if key == 'time':
                        time_attr.setdefault(value,[]).append(coref_line)
                else:
                    break
                     
        

        else:
            if temp:
                attr_temp = []
                f_coref.write('='*18+'\n')
                sorted_attr = sorted(time_attr.iteritems(), key = lambda d:len(d[1]), reverse=True)
                k = ''
                if sorted_attr != []:
                    k = sorted_attr[0][0]
                    del sorted_attr[0]
                for key,value in temp.items():
                    if value.has_key('time') == False or value['time'] == k:     
                        f_coref.write(key+'\n')
                        for k,v in value.items():
                            attr_temp.append((k,v))
                        del temp[key]

                f_coref.write('*'*18+'\n')
                for a in attr_temp:
                    f_coref.write(a[0]+' '+a[1]+'\n')
                
                while temp != {}:
                    attr_temp = []
                    guard = ''
                    for key,value in temp.items():
                        if guard == '':
                            f_coref.write('='*18+'\n')
                            guard = value['time']
                            f_coref.write(key+'\n')
                            for k,v in value.items():
                                attr_temp.append((k,v))
                            del temp[key]
                        else:
                            if value['time'] == guard:
                                f_coref.write(key+'\n')
                                for k,v in value.items():
                                    attr_temp.append((k,v))
                                del temp[key]
                    f_coref.write('*'*18+'\n')
                    for a in attr_temp:
                        f_coref.write(a[0]+' '+a[1]+'\n')
                        
                            
def CombineCoreference(Destination, file,):
    '''
    generate .coreference file ,which contains detail infomation about coreference events
    '''
    
    coref_file = file + '.coref.events'
    coref_dir = os.path.join(Destination, coref_file)
    if os.path.exists(coref_dir):
        
        coref_lines = read_all_lines(coref_dir)
        arg_file = file + '.arg'
        arg_dir = os.path.join(Destination, arg_file)
        arg_lines = read_all_lines(arg_dir)
    
        coref_attr_file = file + '.coreference3'
        coref_attr_dir = os.path.join(Destination, coref_attr_file)
        f_coref = open(coref_attr_dir, 'w')
        f_coref.close()
        
        writeCoreference_v2(coref_lines, arg_lines, coref_attr_dir)   
        
             
                        
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

def EventCoreference_t():
    '''
    test
    '''
    PATH = u"/home/lzh/Documents/SinoCoreferencer/突发事件/社会安全/topic62"
    testLoc = "/home/lzh/Documents/SinoCoreferencer/test"
  
    childfiles = []
    for dirpath, dirpathnames, filenames in os.walk(PATH):
            directory = os.path.join(dirpath, 'directory.all')
            dir_lines = read_all_lines(directory)
            for line in dir_lines:  
                f_test = open(testLoc, 'w')
                absoulePath = os.path.join(dirpath, line).encode('utf-8')
                print absoulePath
                f_test.write(absoulePath+'\n')
                f_test.flush()
                
                input_file = line + '.shtml.out'
                each_input  = 'topic62_'
                input_dir = os.path.join('/home/lzh/Downloads/data/', each_input, input_file)
                FileGeneration(dirpath, input_dir, line)
                

                os.chdir("/home/lzh/Documents/SinoCoreferencer/")
                os.system("./run-coreference.sh test")
                Post_arg(dirpath, input_dir, line)

def CombineAllCoreference_t():
    '''
    process all files contained
    '''
    PATH = u"/home/lzh/Documents/SinoCoreferencer/突发事件/社会安全/topic62"

    childfiles = []
    for dirpath, dirpathnames, filenames in os.walk(PATH):
            directory = os.path.join(dirpath, 'directory.all')
            dir_lines = read_all_lines(directory)
            for line in dir_lines:
                print dirpath
                print line         
                CombineCoreference(dirpath, line)


     
    
               
if __name__ == '__main__':
#     EventCoreference()
#     CombineAllCoreference()
    
#     run event coreference
#     EventCoreference_t()
#     run coreference combine
 
#     CombineAllCoreference_t()
    '''
    coreference1 within-time
    coreference2 without-time
    coreference3 abondon mistakes with time
    '''
    Post_arg(u"/home/lzh/Documents/SinoCoreferencer/突发事件/社会安全/topic62", "/home/lzh/Downloads/data/topic62_/n454059513.shtml.out", "n454059513")
    CombineCoreference(u"/home/lzh/Documents/SinoCoreferencer/突发事件/社会安全/topic62","n454059513")    
#     CombineCoreference("/home/lzh/Documents/SinoCoreferencer/突发事件/社会安全/topic62/", "n454056663", "2016-06-12 23:37:27")
#     EventCoreference_test()
    print("Done!")