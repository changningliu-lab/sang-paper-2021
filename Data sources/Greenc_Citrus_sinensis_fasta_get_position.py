# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 21:44:07 2018

@author: chenw
"""
#参数1：.txt 参数2：.fasta 输出：带有位置信息的fasta
import sys

transcripts = dict()
with open(sys.argv[1], 'r') as txt:
        for line in txt:
            item = line.strip().split()            
            transcript_id = item[0]
            chrome = item[1]
            start = item[2]
            end = item[3]
            strand = '.'
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
            
file_out = open(sys.argv[3], 'w')
with open(sys.argv[2], 'r') as fasta:
    for line in fasta:
        if line[0] == '>':
            item = line.strip().split()
            genename = item[0][5:]  
            if genename in transcripts:
                info = transcripts[genename]
                flag = 1
                line = item[0] + ' ' + ' '.join(info) + '\n'
            else:
                flag = 0
        if flag == 1:
            file_out.write(line)

txt.close()
fasta.close()
file_out.close()

            
            
