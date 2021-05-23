# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 21:44:07 2018

@author: chenw
"""
#参数1：.gff 参数2：.fasta 输出：带有位置信息的fasta
import re
import sys

chr_dict = {'NC_024239.1':'chr1', 'NC_024240.1':'chr2', 'NC_024241.1':'chr3', 'NC_024242.1':'chr4', 'NC_024243.1':'chr5', 'NC_024244.1':'chr6', 'NC_024245.1':'chr7', 'NC_024246.1':'chr8', 'NC_024247.1':'chr9', 'NC_024248.1':'chr10', 'NC_024249.1':'chr11', 'NC_024250.1':'chr12', 'NC_024251.1':'chr13', 'NC_024252.1':'chr14', 'NC_024253.1':'chr15', 'NC_024254.1':'chr16', 'NC_024255.1':'chr17'}
transcripts = dict()
with open(sys.argv[1], 'r') as gff:
        for line in gff:
            if line[0] == '#':
                continue
            item = line.strip().split('\t')            
            if (item[2] == "lnc_RNA") or (item[2] == "transcript") or (item[2] == "ncRNA") or (item[2] == "lncRNA") or (item[2] == "primary_transcript") or (item[2] == "antisense_RNA") or (item[2] == "sequence_feature") or (item[2] == "sequence_conflict"):
                try:
                    transcript_id = re.findall('Genbank:(\S+?)[;,$]', item[8])[0]
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
            item = line.strip().split()
            genename = item[0][1:]  
            info = transcripts[genename]
            if info[0] in chr_dict:
                flag = 1
                info[0] = chr_dict[info[0]]
                #print(info)
                #sys.exit()
                line = '>'+ genename + ' ' + ' '.join(info) + ' ' + item[-1] + '\n'
            else:
                flag = 0
        if flag == 1:
            file_out.write(line)
gff.close()
fasta.close()
file_out.close()
