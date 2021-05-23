#input1:four_class_lnc_of_Ath.txt
#input2:rename_688lnc.txt
#output:Angiosperm_lnc_list_of_Ath.txt;Brassicaceae_lnc_list_of_Ath.txt;Arabidopsis_lnc_list_of_Ath.txt;Dicotyledon_lnc_list_of_Ath.txt

import sys
from collections import defaultdict

taxon2lnc_dict = defaultdict(list)
with open('four_class_lnc_of_Ath.txt') as file_in1:
    for line in file_in1:
        item = line.split()
        if (line[0] == 'A') or (line[0] == 'B') or (line[0] == 'D'):
            taxon  = item[0]
            lnc = item[1]
            taxon2lnc_dict[taxon].append(lnc)

old2new_name_dict = {}
with open('rename_688lnc.txt') as file_in2:
    for line in file_in2:
        item = line.strip().split('\t')
        oldname = item[1]
        newname = item[2]
        old2new_name_dict[oldname] = newname
        

file_out_name_dict = {'Arabidopsis':'Arabidopsis_lnc_list_of_Ath.txt','Brassicaceae':'Brassicaceae_lnc_list_of_Ath.txt','Dicotyledon':'Dicotyledon_lnc_list_of_Ath.txt','Angiosperm':'Angiosperm_lnc_list_of_Ath.txt'}

for key,value in taxon2lnc_dict.items():
    file_out = open(file_out_name_dict[key], 'w')
    for names in value:
        file_out.write(old2new_name_dict[names] + '\n')
    file_out.close()

file_in1.close()


