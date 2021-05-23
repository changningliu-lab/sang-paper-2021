#input1:classify_lnc_four_class.txt
#input2:tissue_SRR.txt
#output:seedling_list_1_lnc.txt;seedling_list_2_lnc.txt;seedling_list_3_lnc.txt;seedling_list_4_lnc.txt
#       inflorescences_list_1_lnc.txt;inflorescences_list_2_lnc.txt;inflorescences_list_3_lnc.txt;inflorescences_list_4_lnc.txt
#       seeds_list_1_lnc.txt;seeds_list_2_lnc.txt;seeds_list_3_lnc.txt;seeds_list_4_lnc.txt
#       leaf_list_1_lnc.txt;leaf_list_2_lnc.txt;leaf_list_3_lnc.txt;leaf_list_4_lnc.txt
#       cotyledons_list_1_lnc.txt;cotyledons_list_2_lnc.txt;cotyledons_list_3_lnc.txt;cotyledons_list_4_lnc.txt
#       silique_list_1_lnc.txt;silique_list_2_lnc.txt;silique_list_3_lnc.txt;silique_list_4_lnc.txt
#       floral_bud_list_1_lnc.txt;floral_bud_list_2_lnc.txt;floral_bud_list_3_lnc.txt;floral_bud_list_4_lnc.txt
#       endosperm_list_1_lnc.txt;endosperm_list_2_lnc.txt;endosperm_list_3_lnc.txt;endosperm_list_4_lnc.txt
#       root_list_1_lnc.txt;root_list_2_lnc.txt;root_list_3_lnc.txt;root_list_4_lnc.txt

import sys
import re
from collections import defaultdict

lnc_dict = {}
with open(sys.argv[1]) as file_in1:
    for line in file_in1:
        if line[:2] == '##':
            key  = line.strip().split('\t')[1]
        elif line[0] != '#':
            lnc_list = line.strip().split(';')
            lnc_dict[key] = lnc_list

tissue_SRR_dict = {}
with open(sys.argv[2]) as file_in2:
    for line in file_in2:
        item = line.split('\t')
        tissue = item[0]
        print(item[1])
        sys.exit()
        SRR_list = item[1].split(';')[:-1]
        tissue_SRR_dict[tissue] = SRR_list

for key,value in tissue_SRR_dict.items():
    class_genename_fpkm = {}
    class_genename_fpkm['list_1_lnc'] = defaultdict(list)
    class_genename_fpkm['list_2_lnc'] = defaultdict(list)
    class_genename_fpkm['list_3_lnc'] = defaultdict(list)
    class_genename_fpkm['list_4_lnc'] = defaultdict(list)
    for SRR in value:
        with open('/home/sangye/lncRNA_evolution/RNA-seq_analysis/transcriptome_analysis/3_stringtie_result/stringtie_gtf_result/' + SRR + '.gtf', 'r') as file_in:
            for line in file_in:
                item = line.split()
                if item[2] == 'transcript':
                    transcript_id = re.findall('transcript_id "([^"]+)',item[8])[0]
                    FPKM = re.findall('FPKM "([^"+])',item[8])[0]
                    if transcript_id in lnc_dict['list_1_lnc']:
                        class_genename_fpkm['list_1_lnc'][transcript_id].append(FPKM)
                    if transcript_id in lnc_dict['list_2_lnc']:
                        class_genename_fpkm['list_2_lnc'][transcript_id].append(FPKM)
                    if transcript_id in lnc_dict['list_3_lnc']:
                        class_genename_fpkm['list_3_lnc'][transcript_id].append(FPKM)
                    if transcript_id in lnc_dict['list_4_lnc']:
                        class_genename_fpkm['list_4_lnc'][transcript_id].append(FPKM)
        file_in.close()
    for list_lnc,transcript_id_FPKM in class_genename_fpkm.items():
        for transcript_ids,FPKM in transcript_id_FPKM.items():
            FPKM_value = 0.0
            length = len(FPKM)
            for i in FPKM:
                FPKM_value = FPKM_value + float(i)
            ave_FPKM_value = FPKM_value/length
            with open(key + '_' + list_lnc + '.txt' ,'w') as file_out:
                file_out.write('\t'.join([transcript_ids, '%.4f' % ave_FPKM_value]) + '\n')
        file_out.close()



    
                        





        
