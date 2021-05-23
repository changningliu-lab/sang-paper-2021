#参数1：classify_lnc_four_class.txt
#参数2：/home/sangye/lncRNA_evolution/merge_database_and_define_parologs_orthologs/merge_database_step4_merge_location_step5_define_parologs_orthologs/plant_merge_location_and_define_parologs_orthologs/gffcompare_annotated_gtf_remain_oxiu_four_class_high_confident_lnc_fa/Oryza_sativa.annotated.fa,Malus_domestica.annotated.fa,Solanum_lycopersicum.annotated.fa
#输出：print

import re
import sys
from collections import defaultdict

lnc_dict = defaultdict(list)
with open(sys.argv[1]) as file_in1:
    for line in file_in1:
        if line[:2] == '##':
            key = line.strip().split('\t')[1]
        elif line[0] != '#':
            lnc_list = line.strip().split(';')[:-1]
            for lncnames in lnc_list:
                lncs = lncnames.split('#')[1]
                lnc_dict[key].append(lncs)

species_lncname_dict = defaultdict(list)
def read_files(filename):
    file_in = open(filename, 'r')
    species = filename.split('/')[-1].split('.')[0]
    for line in file_in:
        if line[0] == '>':
            lncname = line[1:-1]    
            species_lncname_dict[species].append(lncname)
        
read_files(sys.argv[2])
read_files(sys.argv[3])
read_files(sys.argv[4])

#print(species_lncname_dict)
#sys.exit()

count_dict = {}
count_dict['list_18*Oryza_sativa'] = 0
count_dict['list_18*Malus_domestica'] = 0
count_dict['list_25*Solanum_lycopersicum'] = 0
count_dict['list_25*Oryza_sativa'] = 0
count_dict['list_2_1*Solanum_lycopersicum'] = 0
count_dict['list_4*Malus_domestica'] = 0
count_dict['list_2_1*Malus_domestica'] = 0
count_dict['list_4*Solanum_lycopersicum'] = 0
count_dict['list_18*Solanum_lycopersicum'] = 0
count_dict['list_4*Oryza_sativa'] = 0
count_dict['list_2_1*Oryza_sativa'] = 0
count_dict['list_25*Malus_domestica'] = 0

for list_n_lnc,lnc_list in lnc_dict.items():
    for lnc in lnc_list:
        for species,lncname_list in species_lncname_dict.items():
            key = list_n_lnc + '*' + species
            if lnc in lncname_list:
                count_dict[key] = count_dict[key] + 1
for keys,value in count_dict.items():
    print(keys + '\t' + str(value))