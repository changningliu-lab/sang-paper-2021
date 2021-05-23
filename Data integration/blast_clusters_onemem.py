#参数：.blast.coverage文件   输出1：*_genome目录下lncRNAname.txt  
import sys
import os
from collections import defaultdict

gap = 4000
path = sys.argv[1].split('.b')[0]
if not os.path.exists(path): os.mkdir(path) 

lncRNA = ""
lncDict = defaultdict(list)

def write_cluster(key,value):
    fo = open(path+"/"+key+".txt", "w")
    num = 0
    for chrom,loci in value.items():        
        index = -gap
        identity_cov_100_list = []
        for locusnum in sorted(loci):  
            if (float(locusnum[2]) == 100) and (float(locusnum[3]) == 100):
               identity_cov_100_list.append(locusnum[4])  
            else:                    
                if locusnum[0] > index+gap:
                    num = num + 1
                    fo.write(str(num)+' '+"-"*150+'\n')
                fo.write(locusnum[4])
                index = locusnum[1]
        for identity_cov_100 in identity_cov_100_list:
            num = num + 1
            fo.write(str(num)+' '+"-"*150+'\n')
            fo.write(identity_cov_100)           
    fo.close()

with open(sys.argv[1]) as f:
	for line in f:
		lineinfo = line.split("\t")
		if lineinfo[0] != lncRNA:
			if lncDict:
				write_cluster(lncRNA,lncDict)
				lncDict = defaultdict(list)
			lncRNA = lineinfo[0]
		lineinfo[8] = int(lineinfo[8])
		lineinfo[9] = int(lineinfo[9])
		if lineinfo[8] < lineinfo[9]:
			lncDict[lineinfo[1]+' +'].append((lineinfo[8],lineinfo[9],lineinfo[2],lineinfo[-1][:-2],line.strip()+'\t'+'+'+'\n'))
		else:
			lncDict[lineinfo[1]+' -'].append((lineinfo[9],lineinfo[8],lineinfo[2],lineinfo[-1][:-2],line.strip()+'\t'+'-'+'\n'))
#lncnum = open(path+"/"+sys.argv[1].split('.b')[0]+'_lncrnanum.txt1','w')

write_cluster(lncRNA,lncDict)

f.close()

