# -*- coding: utf-8 -*-
"""qqqq
Created on Fri Oct 12 16:34:16 2018

@author: 桑叶
"""
#参数1：.blast文件   参数2：物种*_lncrnas_length.txt  参数3：输出.blast.coverage文件

import sys
import os
from collections import defaultdict

path=os.getcwd()
if not os.path.exists(path):
    os.makedirs(path) 
            
fo = open(sys.argv[3],'w')
#lncnum = open(path+'/'+sys.argv[2].split('/')[-1].split('.')[0]+'_num.txt','w')
#读_lncrnas_length.txt
lengthDict = {}
with open(sys.argv[2]) as length:
    for line in length:
        itemm = line.strip().split()
        name = itemm[0]
        lnclength = itemm[1]
        lengthDict[name] = int(lnclength)
        
with open(sys.argv[1]) as blast:
    for line in blast:
        info = line.split()
        if info[0][:4] == 'lcl|':
            genename = info[0][4:]
        else:
            genename = info[0]
        cov = (abs(int(info[9])-int(info[8]))+1)/lengthDict[genename]*100
        fo.write('\t'.join(info+[str('%.2f'%cov)+'%\n']))
               
fo.close()
length.close()
blast.close() 
            