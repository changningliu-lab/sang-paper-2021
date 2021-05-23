#input:/home/sangye/lncRNA_evolution/data_analysis/lnc_genome_mapping/annotated_gtf/*.annotated.gtf
#output:species_class_code_statistics.txt

import sys
import re

class_code_dict = {}
transcript_sum = 0
with open(sys.argv[1]) as file_in1:
    for line in file_in1:
        item = line.strip().split("\t")
        if item[2] == "transcript":
            transcript_sum = transcript_sum + 1
            class_code = re.search('class_code "([^"]+)', item[8])
            class_code_str = class_code.group(1)
            if class_code_str not in class_code_dict:
                class_code_dict[class_code_str] = 1
            else:
                class_code_dict[class_code_str] = class_code_dict[class_code_str] + 1


for key,value in class_code_dict.items():
    percent = value/transcript_sum
    print('\t'.join([key, str(value), str('%.4f' % percent)]))