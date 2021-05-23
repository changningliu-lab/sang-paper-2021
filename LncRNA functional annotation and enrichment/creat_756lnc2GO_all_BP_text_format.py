#input:lncmame_enrichment.csv(共756个文件，对应756条lnc,但是由于原因一：有些lnc不在构建的网络中，所以没有相邻的编码基因，只有523个有相邻基因，原因二：find_enrichment.py的pvalue卡掉一部分没有富集的lnc，所以输入文件只有383/357(--p0.05/p0.01)个了)--这些数字都会根据建网及之后的所有操作所选参数不同而改变
#input2:p-value 
#input3:fulllist_ 或者 ''
#output-fo:756lnc2GO_text_format_slim_' + sys.argv[3] + 'p' + sys.argv[2] + '_allBP.txt'
#output-file_out:756lnc_pvalue_go_go-meaning.txt
#注意：由于写文件是追加模式，重跑前必须清除输出文件已有内容

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
        NS = row_list[1]
        enrichment = row_list[2]
        if (NS == 'BP') and (enrichment == 'e'):
            pvalue = float(row_list[9])
            #ratio_in_study = row_list[4]
            #study = int(ratio_in_study.split('/')[0])/int(ratio_in_study.split('/')[1])
            #ratio_in_pop = row_list[5]
            #pop = int(ratio_in_pop.split('/')[0])/int(ratio_in_pop.split('/')[1])
            #if study > pop:
            pvalue2line_dict[pvalue].append(row_list)
key_sort_list = sorted(pvalue2line_dict)
#print(key_sort_list[:20])
#sys.exit()
fo = open('/home/sangye/lncRNA_evolution/RNA-seq_analysis/transcriptome_analysis/4_normalization_90_samples_methods2_p0.05/756lnc2GO_text_format_slim_' + sys.argv[3] + 'p' + sys.argv[2] + '_allBP.txt', 'a+')
file_out = open('/home/sangye/lncRNA_evolution/RNA-seq_analysis/transcriptome_analysis/4_normalization_90_samples_methods2_p0.05/756lnc_pvalue_go_go-meaning.txt', 'a+')

count = 0
key_sort_p_list = []
for p in key_sort_list:
    if p < float(sys.argv[2]):
        count = count + 1
        key_sort_p_list.append(p)
if count > 0:
    fo.write(sys.argv[1].split('_')[-2][-10:] + '\t')
    go_num = 0
    for p in sorted(key_sort_p_list):
        row_value = pvalue2line_dict[p]
        for row_list in row_value:
            GO = row_list[0]
            name = row_list[3]
            if go_num < 10:
                file_out.write('\t'.join([sys.argv[1].split('/')[1].split('_')[0], str(p), GO, name]) + '\n')
                fo.write(GO + ';')
                go_num = go_num + 1
    fo.write('\n')

fo.close()
fi.close()
file_out.close()