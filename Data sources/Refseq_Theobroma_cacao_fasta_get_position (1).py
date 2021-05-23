# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 21:44:07 2018

@author: chenw
"""
#参数1：.gff 参数2：.fasta 输出：带有位置信息的fasta
import re
import sys

chr_dict = {'NC_030850.1':'chr1', 'NC_030851.1':'chr2', 'NC_030852.1':'chr3', 'NC_030853.1':'chr4', 'NC_030854.1':'chr5', 'NC_030855.1':'chr6', 'NC_030856.1':'chr7', 'NC_030857.1':'chr8', 'NC_030858.1':'chr9', 'NC_030859.1':'chr10'}
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
