#encoding=utf-8

'''
Created on Nov 28, 2016

@author: lzh
'''

from eventPostprocess import InputProcess
import os
import re
from util import read_all_lines

class Time():
    '''
    time format: xxxx-xx-xx xx
    '''
    
    def __init__(self):
        self.year = 0
        self.month = 0
        self.day = 0
        self.hour = 0
        
    def timeall(self):
        time_all = str(self.year)+'-'+str(self.month)+'-'+str(self.day)+' '+str(self.hour)
        return time_all
    
def ExtractTiming(input):
    attr_set = InputProcess(input)
    time_set = []
    for attr in attr_set:
        if attr[7] != 'NULL':
            time_set.append(attr[7])
    print time_set
    return time_set


def Multi():
    '''
    time attribute statictics
    '''
    f_time = open("/home/lzh/Downloads/data/collection.time", 'w')
    PATH = u"/home/lzh/Documents/SinoCoreferencer/突发事件/社会安全"
    
    for dirpath, dirpathnames, filenames in os.walk(PATH):
        for each in dirpathnames:
            childfile = os.path.join(dirpath, each)
            directory = os.path.join(childfile, 'directory.all')
            dir_lines = read_all_lines(directory)
            for line in dir_lines:
                                
                input_file = line + '.shtml.out'
                each_input  = each + '_'
                input_dir = os.path.join('/home/lzh/Downloads/data/', each_input, input_file)
                time_set = ExtractTiming(input_dir)
                for t in time_set:
                    f_time.write(t+'\n')

def HourRegularzation(attr_time):
    '''
    seach hour expression by regulation
    '''
    
    pattern_h1 = re.compile(r'(\d+)时')
    pattern_h2 = re.compile(r'(\d+)点')
    if pattern_h1.findall(attr_time):
        return pattern_h1.findall(attr_time)[0]
    elif pattern_h2.findall(attr_time):
        return pattern_h2.findall(attr_time)[0]
    else:
        if "凌晨" in attr_time:
            return 6
        elif "早" in attr_time:
            return 9
        elif "中午" in attr_time:
            return 12
        elif "下午" in attr_time:
            return 14
        elif "晚" in attr_time:
            return 19
        elif "夜" in attr_time:
            return 21
        else:
            return 0
        
def TimeRegularzation(news_time, attr_time):
    
    news_time = news_time.strip().split(':')[0]
    news_year = news_time.split('-')[0]
    news_month = news_time.split('-')[1]
    news_day = (news_time.split('-')[2]).split(' ')[0]
    news_hour = (news_time.split('-')[2]).split(' ')[1]
#     print  news_time
#     process time
    new_time = Time()
    pattern_y = re.compile(r'(\d+)年')
    pattern_m = re.compile(r'(\d+)月')
    pattern_d = re.compile(r'(\d+)日')

    
    if not pattern_y.findall(attr_time):
        new_time.year = news_year
    elif pattern_y.findall(attr_time) and (not pattern_m.findall(attr_time)):
        new_time.year = pattern_y.findall(attr_time)[0]
        new_time.month = 0
        new_time.day = 0
    elif pattern_y.findall(attr_time) and pattern_m.findall(attr_time) and (not pattern_d.findall(attr_time)):
        new_time.year = pattern_y.findall(attr_time)[0]
        new_time.month = pattern_m.findall(attr_time)[0]
        new_time.day = 0
    elif pattern_y.findall(attr_time) and pattern_m.findall(attr_time) and pattern_d.findall(attr_time):
        new_time.year = pattern_y.findall(attr_time)[0]
        new_time.month = pattern_m.findall(attr_time)[0]
        new_time.day = pattern_d.findall(attr_time)[0]
        
    if not pattern_m.findall(attr_time):
        new_time.month = news_month
    elif pattern_m.findall(attr_time) and (not pattern_d.findall(attr_time)):
        new_time.month = pattern_m.findall(attr_time)[0]
        new_time.day = 0
    else:
        new_time.month = pattern_m.findall(attr_time)[0]
        new_time.day = pattern_m.findall(attr_time)[0]
        
        
    if not pattern_d.findall(attr_time):
        new_time.day = news_day
    else:
        new_time.day = pattern_d.findall(attr_time)[0]
    
    new_time.hour = HourRegularzation(attr_time)
    
    if new_time.year == news_year and new_time.month == news_month and new_time.day == news_day and new_time.hour == 0 and '昨日' in attr_time:
        new_time.day = int(news_day) - 1
    if new_time.year == news_year and new_time.month == news_month and new_time.day == news_day and new_time.hour == 0 and '前天' in attr_time:
        new_time.day = int(news_day) - 2        
    time_re = new_time.timeall()
    if time_re == '2016-11-28 0':
        print attr_time
    return time_re

def data_analysis():
    lines = read_all_lines("/home/lzh/Downloads/data/collection.time")
    new_lines = []
    process = 0
    unprocess = 0
    for line in lines:
        time_re = TimeRegularzation("2016-11-28 19:37:00", line)
        new_lines.append(time_re)
        if time_re == '2016-11-28 0':
            unprocess += 1
        else:
            process += 1
    f_time = open("/home/lzh/Downloads/data/collection1.time",'w')
    for l in new_lines:
        f_time.write(l+'\n')
    f_time.write("processed: %d" % process+'\n')
    f_time.write("unprocessed: %d" % unprocess+'\n')
    
if __name__ == '__main__':
#     Multi()
#     TimeRegularzation("2016-11-28 19:37:00", "中新社布鲁塞尔3月21日电(记者沈晨)巴黎系列恐怖袭击案关键疑犯萨拉赫?阿卜杜勒?萨拉姆3月21日首度与辩护律师斯文?马利交流")
#     ExtractTiming('/home/lzh/Downloads/data/topic62_/n454054862.shtml.out')
    data_analysis()
    print("Done!")
