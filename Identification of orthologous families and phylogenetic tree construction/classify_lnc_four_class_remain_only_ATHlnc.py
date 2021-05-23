#input：classify_lnc_four_class.txt
#output:classify_lnc_four_class_remain_only_ATHlnc.txt

import re
import sys
from collections import defaultdict

file_out = open('classify_lnc_four_class_remain_only_ATHlnc.txt', 'w')
file_out.write('#Ath lncnum of four class  389    251    28     20' + '\n')

lnc_dict = defaultdict(list)
with open('classify_lnc_four_class.txt') as file_in1:
    for line in file_in1:
        if line[:2] == '##':
            key = line.strip().split('\t')[1]
        elif line[0] != '#':
            lnc_list = line.strip().split(';')[:-1]
            for lncnames in lnc_list:
                species = lncnames.split('#')[0]
                if species == 'Arabidopsis_thaliana_lncrnas':
                    lnc_dict[key].append(lncnames)
for key,value in lnc_dict.items():
    file_out.write('##' + '\t' + key + '\n')
    file_out.write(';'.join(value) +';' + '\n')
file_out.close()
file_in1.close()