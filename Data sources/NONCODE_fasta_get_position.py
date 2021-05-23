# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 21:44:07 2018

@author: chenw
"""
#参数1：.bed 参数2：.fasta 输出：带有位置信息的fasta
#import re
import sys

transcripts = dict()
with open(sys.argv[1], 'r') as bed:
        for line in bed:
            #if line[0] == '#':
                #continue
            item = line.strip().split('\t')
            #if item[2] == "lnc_RNA":
                #try:
            transcript_id = item[3]#re.findall('transcript_id=(\S+?)\;', item[8])[0]
            chrome = item[0]
            start = item[6]
            end = item[7]
            strand = item[5]
            if (len(chrome) <= 5):
                if transcript_id in transcripts:
                    transcripts[transcript_id].append(chrome)
                    transcripts[transcript_id].append(strand)
                    transcripts[transcript_id].append(start)
                    transcripts[transcript_id].append(end)
                else:
                    transcripts[transcript_id] = list()
                    transcripts[transcript_id].append(chrome)
                    transcripts[transcript_id].append(strand)
                    transcripts[transcript_id].append(start)
                    transcripts[transcript_id].append(end)
                #except:
                    #pass
file_out = open(sys.argv[3], 'w')
with open(sys.argv[2], 'r') as fasta:
    for line in fasta:
        if line[0] == '>':
            genename = line[1:].strip('\n')  
            if genename in transcripts:
                flag = 1
                info = transcripts[genename] 
                line = line.strip('\n') + ' ' + ' '.join(info) + ' lncRNA' +  '\n'
            else:
                flag = 0
        if flag == 1:
            file_out.write(line)
bed.close()
fasta.close()
file_out.close()
