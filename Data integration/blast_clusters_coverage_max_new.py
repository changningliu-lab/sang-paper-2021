# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 15:11:00 2018

@author: 桑叶
"""
#参数1：*_coverage/lncRNAname_cluster_coverage_max.txt文件  参数2：lncRNAname_cluster_coverage.txt
#输出lncRNAname_cluster_coverage_max_new.txt文件

import sys
import os

path=os.getcwd()
if not os.path.exists(path):
    os.makedirs(path)

cov_max_list = []
with open(sys.argv[1], 'r') as f1:
    for line in f1:
        info = line.split()
        numorder = info[0]
        cov_max_list.append(numorder)
cluster_Dict = {}
with open(sys.argv[2], 'r') as f2:
    for line in f2:
        if line[:2] != '\n': 
            info = line.split()
            if info[0].isdigit():
                key = info[0]
                cluster_Dict[key] = []
            else:
                if line[0] != 'c':
                    cluster_Dict[key].append(line)
                else:
                    cluster_Dict[key+' '+ line.strip()] = cluster_Dict[key]
                    del cluster_Dict[key]
f_out = open(path + '/' + sys.argv[1].split('.t')[0] + '_new.txt', 'w')

for key,value in cluster_Dict.items():
    if key.split()[0] in cov_max_list: 
        f_out.write(key + ' ' + '-'*140 + '\n' + ''.join(value[0:]))
f1.close()
f2.close() 
f_out.close() 
