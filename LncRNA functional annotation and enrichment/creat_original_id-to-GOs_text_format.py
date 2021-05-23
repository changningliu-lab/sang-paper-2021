#input:tair.gaf
#output1:tair_id2GO_text_format.txt
#output2:tair_gaf_irregular_line.txt(内容是没有AT*G*****的行）

import sys
import re
from collections import defaultdict

file_in = open('tair.gaf', 'r')
file_out1 = open('tair_id2GO_text_format.txt', 'w')
#file_out2 = open('tair_gaf_irregular_line.txt', 'w')

gene2go_dict = defaultdict(list)
for line in file_in:
    if line[0] != '!':
        item = line.split('\t')
        go = re.findall('GO:(\S+)',line)[0]
        go_id = 'GO:' + go
        gene_name_list = []
        try:
            gene_name = re.findall('[AT,At,at,aT](\d)[g,G](\d+)[|,\s]', line)[0]
            gene_name_id1 = 'AT' + gene_name[0] + 'G' + gene_name[1]
            gene_name_id2 = 'AT' + gene_name[0] + 'g' + gene_name[1]
            gene_name_id3 = 'At' + gene_name[0] + 'G' + gene_name[1]
            gene_name_id4 = 'At' + gene_name[0] + 'g' + gene_name[1]
            gene_name_id5 = 'at' + gene_name[0] + 'G' + gene_name[1]
            gene_name_id6 = 'at' + gene_name[0] + 'g' + gene_name[1]
            gene_name_id7 = 'aT' + gene_name[0] + 'G' + gene_name[1]
            gene_name_id8 = 'aT' + gene_name[0] + 'g' + gene_name[1]
            for i in item:
                if (gene_name_id1 in i) or(gene_name_id2 in i) or(gene_name_id3 in i) or(gene_name_id4 in i) or(gene_name_id5 in i) or(gene_name_id6 in i) or(gene_name_id7 in i) or(gene_name_id8 in i):
                    gene_name_list = gene_name_list + i.split('|')
        except:
            gene_name_id = item[2]
            for i in item:
                if gene_name_id in i:
                    gene_name_list = gene_name_list + i.split('|')

        for gene in set(gene_name_list):
            gene2go_dict[gene].append(go_id)

for gene_name,go_list in gene2go_dict.items():
    file_out1.write(gene_name + '\t' + ';'.join(set(go_list)) + '\n')

file_in.close()
file_out1.close()
#file_out2.close()