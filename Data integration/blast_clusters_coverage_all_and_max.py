# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 09:22:28 2018

@author: 桑叶
"""
#参数1：*_genome/lncRNAname.txt文件   参数2：物种*_lncrnas_length.txt   输出:lncRNA_cluster_coverage.txt和lncRNA_cluster_coverage_max.txt文件

import sys
import os 
from collections import defaultdict

#读*_genome/lncRNAname.txt，存在locusDict里
num = 0 
with open(sys.argv[1]) as file_in:
    locusDict = defaultdict(list)
    for line in file_in:
        info = line.split()                     
        if info[1] != '-'*150:
            if int(info[8]) < int(info[9]):
                end = int(info[9])
                start = int(info[8])
            identity = float(info[2])
            if int(info[8]) > int(info[9]):
                start = int(info[9])
                end = int(info[8])
            locusDict[str(info[0])+'*'+str(info[1])+'_'+str(num)].append((start,end,identity,line))
        else:
            num = num + 1
    file_in.close()

#读_lncrnas_length.txt
lengthDict = {}
with open(sys.argv[2]) as length:
    for line in length:
        itemm = line.strip().split()
        name = itemm[0]
        lnclength = itemm[1]
        lengthDict[name] = int(lnclength)

#读locusDict，计算有效长度，输出到path下的_cluster_coverage.txt文件中   
work_dir = os.getcwd()                    
path = work_dir+'/'+sys.argv[1].split('/')[0]+'_cluster_coverage'
if not os.path.exists(path):
    os.makedirs(path)

count = 0  
identity_weighing_max = 0  
file_out1 = open(path+'/'+sys.argv[1].split('.t')[0].split('/')[1]+'_cluster_coverage.txt','w') 
for lnc_chr_info,loci in locusDict.items():
    index = -1
    sumlength = 0
    count = count +1
    identity_weighing_numerator = 0
    identity_weighing_denominator = 0
    file_out1.write(str(count)+' '+'-'*160+'\n')
    for locusnum in sorted(loci):
        identity_weighing_numerator = identity_weighing_numerator + locusnum[2]*(locusnum[1] - locusnum[0] + 1)
        identity_weighing_denominator = identity_weighing_denominator + (locusnum[1] - locusnum[0] + 1)
        if locusnum[0] > index:
            efflength = locusnum[1] - locusnum[0] + 1
            index = locusnum[1]
            sumlength = sumlength + efflength
        else:
            if locusnum[1] > index:
                efflength = locusnum[1] - index
                index = locusnum[1]
                sumlength = sumlength + efflength
        file_out1.write(locusnum[3]+'\n')
    identity_weighing = identity_weighing_numerator/identity_weighing_denominator
    cov = sumlength/lengthDict[lnc_chr_info.split('*')[0]]*100
    file_out1.write('cluster_coverage:'+str('%.2f'%cov)+'%'+'\t'+'identity_weighing:'+str('%.3f'%identity_weighing)+'\n')
    if (identity_weighing > 80) and (cov > 70):
        if identity_weighing > identity_weighing_max:
            identity_weighing_max = identity_weighing
            cov_max = cov
            file_out = open(path+'/'+sys.argv[1].split('.t')[0].split('/')[1]+'_cluster_coverage_max.txt','w') 
            file_out.write('\t'.join([str(count),lnc_chr_info.split('*')[0],lnc_chr_info.split('*')[1],str('%.2f'%cov)+'%',str('%.3f'%identity_weighing)+'\n']))
            file_out.close()
        elif identity_weighing == identity_weighing_max:
            if cov == cov_max:
                file_out = open(path+'/'+sys.argv[1].split('.t')[0].split('/')[1]+'_cluster_coverage_max.txt','a+') 
                file_out.write('\t'.join([str(count),lnc_chr_info.split('*')[0],lnc_chr_info.split('*')[1],str('%.2f'%cov)+'%',str('%.3f'%identity_weighing)+'\n']))
                file_out.close()
            elif cov > cov_max:
                cov_max = cov
                file_out = open(path+'/'+sys.argv[1].split('.t')[0].split('/')[1]+'_cluster_coverage_max.txt','w')
                file_out.write('\t'.join([str(count),lnc_chr_info.split('*')[0],lnc_chr_info.split('*')[1],str('%.2f'%cov)+'%',str('%.3f'%identity_weighing)+'\n']))
                file_out.close()
    
length.close()
file_out1.close()       
        
             
             
             
             
             
             
             
             
             
             
             
