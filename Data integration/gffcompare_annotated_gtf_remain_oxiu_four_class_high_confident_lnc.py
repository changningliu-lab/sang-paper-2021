#input:/home/sangye/lncRNA_evolution/data_analysis/lnc_genome_mapping/gffcompare_work_related_plant_merge_location_and_define_parologs_orthologs_work2_2_gffcompare_annotated_gtf_remain_oxiu_four_class_high_confident_lnc/annotated_gtf/*gtf
#output:gffcompare_annotated_gtf_remain_oxiu_four_class_high_confident_lnc_gtf/*gtf

import sys
import re
file_in = open(sys.argv[1], "r")
file_out = open(sys.argv[2], "w")
flag = 0
for line in file_in:
    item = line.strip().split("\t")
    if item[2] == "transcript":
        class_code = re.search('class_code "([^"]+)', item[8])
        class_code_str = class_code.group(1)
        if class_code_str in "oxiu":
            file_out.write(line)
            flag = 1
        else:
            flag = 0
    elif item[2] == "exon":
        if flag == 1:
            file_out.write(line)
file_in.close()
file_out.close()