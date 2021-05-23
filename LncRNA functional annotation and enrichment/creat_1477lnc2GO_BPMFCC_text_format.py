#input:lncmame_enrichment.csv(共1477个文件)
#input2:p-value
#input3:fulllist_ 或者 ''
#output:1477lnc2GO_text_format.txt sys.argv[1]

import csv
import sys 
from collections import defaultdict
#读CSV文件
fi = open(sys.argv[1],  'r')
fi_csv = csv.reader(fi, dialect='excel-tab')

pvalue2line_dict = defaultdict(list)
for row_list in fi_csv:
    #print(row_list)#遍历csv对象，返回的是列表
    if row_list[9] != 'p_fdr_bh':
        #NS = row_list[1]
        #if NS == 'BP':
        pvalue = float(row_list[9])
        ratio_in_study = row_list[4]
        study = int(ratio_in_study.split('/')[0])/int(ratio_in_study.split('/')[1])
        ratio_in_pop = row_list[5]
        pop = int(ratio_in_pop.split('/')[0])/int(ratio_in_pop.split('/')[1])
        if study > pop:
            pvalue2line_dict[pvalue].append(row_list)
key_sort_list = sorted(pvalue2line_dict)
#print(key_sort_list[:20])
#sys.exit()
fo = open('/home/sangye/lncRNA_evolution/RNA-seq_analysis/transcriptome_analysis/4_normalization_90_samples/1477lnc2GO_text_format_slim_' + sys.argv[3] + 'p' + sys.argv[2] + '.txt', 'a+')
fo.write(sys.argv[1].split('_')[-2][-7:] + '\t')
#count = 0
for p in key_sort_list:
    if p < float(sys.argv[2]):
        row_value = pvalue2line_dict[p]
        for row_list in row_value:
            #count = count + 1
            #if count <= 10:
            GO = row_list[0]
            fo.write(GO + ';')
fo.write('\n')
    

fo.close()
fi.close()