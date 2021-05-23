import re
import sys
from collections import defaultdict

file_in = open('SRR.Norm', 'r')
file_in2 = open('classify_lnc_four_class.txt', 'r')

lnc_dict = defaultdict(list)
for line in file_in2:
    if line[:2] == '##':
        key  = line.strip().split('\t')[1]
    elif line[0] != '#':
        lnc_list = line.strip().split(';')[:-1]
        for lncnames in lnc_list:
            lncs = lncnames.split('#')[1]
            lnc_dict[key].append(lncs)

file_out = open('SRR_lnc.Norm', 'w')
for line in file_in:
    if line[0] != '#':
        item = line.split()
        lnc_name = item[0]
        if lnc_name in lnc_dict['list_2_1']:
            file_out.write('Arabidopsis' + '\t' + line)
        if lnc_name in lnc_dict['list_4']:
            file_out.write('Brassicaceae' + '\t' + line)  
        if lnc_name in lnc_dict['list_18']:  
            file_out.write('Dicotyledon' + '\t' + line)         
        if lnc_name in lnc_dict['list_25']:
            file_out.write('Angiosperm' + '\t' + line)
    else:
        file_out.write('Taxon' + '\t' + line)                    
file_in.close()
file_in2.close()
file_out.close()
