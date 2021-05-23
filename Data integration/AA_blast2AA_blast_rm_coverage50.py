#input1:25_species_lnc_length.txt
#input2:gffcompare_annotated_gtf_remain_oxiu_four_class_high_confident_lnc_fa_AA_blast/某个.blast
#output/input3:gffcompare_annotated_gtf_remain_oxiu_four_class_high_confident_lnc_fa_AA_blast_rm_coverage50/该个.blast
#过滤的两个条件：1、比对上的长度/min(qury_lnc,target_lnc)的长度>50%；2、必须正着比上

import sys
from collections import defaultdict

file_out = open(sys.argv[3], 'w')

lnc_length_dict = {}
file_in1 = open(sys.argv[1], 'r')
for line in file_in1:
    item = line.strip().split('\t')
    lnc = item[0]
    length = int(item[1])
    lnc_length_dict[lnc] = length

file_in2 = open(sys.argv[2], 'r')
for line in file_in2:
    item = line.split('\t')
    qury_start = int(item[6])
    qury_end = int(item[7])
    target_start = int(item[8])
    target_end = int(item[9])
    qury_length = lnc_length_dict[item[0]]
    target_length = lnc_length_dict[item[1]]
    alignment_length = int(item[3])
    if (((qury_start - qury_end) < 0) and ((target_start - target_end) < 0)) or (((qury_start - qury_end) > 0) and ((target_start - target_end) > 0)):
        coverage = alignment_length/min(qury_length,target_length)
        if coverage > 0.5:
            file_out.write(line)
file_in1.close()    
file_in2.close()  
file_out.close()  