#参数1：/home/sangye/lncRNA_evolution/data_analysis/lnc_classify_methods2_5_class_ATHlnc/classify_lnc_four_class.txt
#参数2：/home/sangye/lncRNA_evolution/merge_database_and_define_parologs_orthologs/merge_database_step4_merge_location_step5_define_parologs_orthologs/plant_merge_location_and_define_parologs_orthologs/gffcompare_annotated_gtf_remain_oxiu_four_class_high_confident_lnc_gtf/Arabidopsis_thaliana.annotated.gtf
#参数3：输出：four_class_lnc_of_Ath.gtf

import re
import sys
import math
from collections import defaultdict

lnc_dict = defaultdict(list)
all_lnc_list = []
with open(sys.argv[1]) as file_in1:
    for line in file_in1:
        if line[:2] == '##':
            key = line.strip().split()[1]
        elif line[0] != '#':
            lnc_list = line.strip().split(';')[:-1]
            for lncnames in lnc_list:
                lncs = lncnames.split('#')[1]
                all_lnc_list.append(lncs)
                lnc_dict[key].append(lncs)

file_out = open(sys.argv[3], 'w')
with open(sys.argv[2]) as file_in2:
    for line in file_in2:
        item = line.split('\t')
        try:
            transcript_id = re.findall('transcript_id "([^"]+)', item[8])[0]
        except:
            print("Can not find transcript_id.")
            sys.exit()
        if transcript_id in all_lnc_list:
            file_out.write(line)

file_in1.close()
file_in2.close()
file_out.close()