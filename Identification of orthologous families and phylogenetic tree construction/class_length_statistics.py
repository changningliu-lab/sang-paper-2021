#参数1：classify_lnc_four_class.txt
#参数2：25_species_lnc_length.txt
#输出：four_class_lnc_length/Arabidopsis_lnc_length.txt,four_class_lnc_length/Brassicaceae_lnc_length.txt,four_class_lnc_length/Dicotyledon_lnc_length.txt,four_class_lnc_length/Angiosperm_lnc_length.txt,four_class_lnc_length/Flower_lnc_length.txt

import re
import sys
import math
from collections import defaultdict

lnc_dict = defaultdict(list)
with open(sys.argv[1]) as file_in1:
    for line in file_in1:
        if line[:2] == '##':
            key = line.strip().split()[1]
        elif line[0] != '#':
            lnc_list = line.strip().split(';')[:-1]
            for lncnames in lnc_list:
                lncs = lncnames.split('#')[1]
                lnc_dict[key].append(lncs)

length_dict = {}
with open(sys.argv[2]) as file_in2:
    for line in file_in2:
        item = line.strip().split('\t')
        lncname = item[0]
        length = item[1]
        length_dict[lncname] = length

file_dict = {'list_2_1':'Arabidopsis_lnc_length.txt','list_4':'Brassicaceae_lnc_length.txt','list_18':'Dicotyledon_lnc_length.txt','list_25':'Angiosperm_lnc_length.txt','list_24':'Flower_lnc_length.txt'}

for list_num_lnc,value in lnc_dict.items():
    file_out = open('four_class_lnc_length/' + file_dict[list_num_lnc], 'w')
    for lnc in value:
        lnclength = length_dict[lnc]
        file_out.write('\t'.join([lnc, lnclength, str('%.4f' %(math.log10(int(lnclength)))), file_dict[list_num_lnc].split('_')[0]]) + '\n')
    file_out.close()

file_in1.close()
file_in2.close()