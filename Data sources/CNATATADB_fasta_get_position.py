# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 21:44:07 2018

@author: chenw
"""
#参数1：.gtf 参数2：.fasta 输出：带有位置信息的fasta
import re
import sys

transcripts = dict()
with open(sys.argv[1], 'r') as gtf:
        for line in gtf:
            if line[0] == '#':
                continue
            item = line.strip().split('\t')
            if item[2] == "transcript":
                try:
                    transcript_id = re.findall('transcript_id \"(\S+)\"', item[8])[0]
                    chrome = item[0]
                    start = item[3]
                    end = item[4]
                    strand = item[6]
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
                except:
                    pass
file_out = open(sys.argv[3], 'w')
with open(sys.argv[2], 'r') as fasta:
    for line in fasta:
        if line[0] == '>':
            genename = line[1:].strip('\n')  
            info = transcripts[genename] 
            line = line.strip('\n') + ' ' + ' '.join(info) + ' lncRNA' + '\n'
        file_out.write(line)
gtf.close()
fasta.close()
file_out.close()
