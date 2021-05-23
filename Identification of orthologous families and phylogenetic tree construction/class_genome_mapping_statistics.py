#参数1：classify_lnc_four_class_remain_only_ATHlnc.txt
#参数2：all_gffcompare_annotated_gtf_remain_oxiu_four_class_high_confident_lnc.gtf
##输出：four_class_lnc_genome_mapping/Arabidopsis_lnc_genome_mapping.txt,four_class_lnc_genome_mapping/Brassicaceae_lnc_genome_mapping.txt,four_class_lnc_genome_mapping/Dicotyledon_lnc_genome_mapping.txt,four_class_lnc_genome_mapping/Angiosperm_lnc_genome_mapping.txt;four_class_lnc_genome_mapping/Flower_lnc_genome_mapping.txt

import re
import sys
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

dict_1_new = defaultdict(list)
dict_2_new = defaultdict(list)
dict_3_new = defaultdict(list)
dict_4_new = defaultdict(list)
dict_5_new = defaultdict(list)
with open(sys.argv[2], 'r') as gtf:
    for line in gtf:
        item = line.split('\t')
        feature = item[2]
        if feature == 'transcript':
            transcript_id = re.findall('transcript_id "(\S+?)["$]', item[8])[0]
            class_code = re.findall('class_code "([^"]+)', item[8])[0]
            #print(transcript_id, class_code)
            #sys.exit()
            if transcript_id in lnc_dict['list_2_1']:
                dict_1_new[class_code].append(transcript_id)
            if transcript_id in lnc_dict['list_4']:
                dict_2_new[class_code].append(transcript_id)
            if transcript_id in lnc_dict['list_18']:
                dict_3_new[class_code].append(transcript_id)
            if transcript_id in lnc_dict['list_25']:
                dict_4_new[class_code].append(transcript_id)
            if transcript_id in lnc_dict['list_24']:
                dict_5_new[class_code].append(transcript_id)

class_code_dict = {'o':'sense_overlaping', 'u':'intergenic', 'i':'intronic', 'x':'antisense'}

file_out1 = open('four_class_lnc_genome_mapping/Arabidopsis_lnc_genome_mapping.txt', 'w')
for class_code,transcript_list in dict_1_new.items():
    transcript_nums = str(len(transcript_list))  
    file_out1.write('\t'.join([class_code_dict[class_code], transcript_nums, 'Arabidopsis']) + '\n')
file_out1.close()

file_out2 = open('four_class_lnc_genome_mapping/Brassicaceae_lnc_genome_mapping.txt', 'w')
for class_code,transcript_list in dict_2_new.items():
    transcript_nums = str(len(transcript_list))  
    file_out2.write('\t'.join([class_code_dict[class_code], transcript_nums, 'Brassicaceae']) + '\n')
file_out2.close()

file_out3 = open('four_class_lnc_genome_mapping/Dicotyledon_lnc_genome_mapping.txt', 'w')
for class_code,transcript_list in dict_3_new.items():
    transcript_nums = str(len(transcript_list))  
    file_out3.write('\t'.join([class_code_dict[class_code], transcript_nums, 'Dicotyledon']) + '\n')
file_out3.close()

file_out4 = open('four_class_lnc_genome_mapping/Angiosperm_lnc_genome_mapping.txt', 'w')
for class_code,transcript_list in dict_4_new.items():
    transcript_nums = str(len(transcript_list))  
    file_out4.write('\t'.join([class_code_dict[class_code], transcript_nums, 'Angiosperm']) + '\n')
file_out4.close()

file_out5 = open('four_class_lnc_genome_mapping/Flower_lnc_genome_mapping.txt', 'w')
for class_code,transcript_list in dict_5_new.items():
    transcript_nums = str(len(transcript_list))  
    file_out5.write('\t'.join([class_code_dict[class_code], transcript_nums, 'Flower']) + '\n')
file_out5.close()

file_in1.close()
gtf.close()