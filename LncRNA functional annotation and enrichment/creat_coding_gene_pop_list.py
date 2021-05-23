#input1:SRR_fulllist_cc0.5.Network
#input2:rename_756lnc.txt
#output1:sys.argv[1] + coding_gene_pop_list.txt

import sys
file_in1 = open(sys.argv[1] ,'r') 
file_in2 = open(sys.argv[2] ,'r')
file_out = open(sys.argv[1] + '_coding_gene_pop_list.txt','w') 

lnc_id_list = []
for line in file_in2:
    item = line.split()
    if item[0] != 'Taxon':
        lnc_id = item[1] 
        lnc_id_list.append(lnc_id)

coding_gene_pop_list = []
for line in file_in1:
    item = line.split()
    if item[0] != '#node1':
        node1 = item[0]
        node2 = item[1]
        coding_gene_pop_list.append(node1)
        coding_gene_pop_list.append(node2)

coding_gene_pop_set = set(coding_gene_pop_list)
Difference_set = coding_gene_pop_set.difference(set(lnc_id_list))

for coding_gene in Difference_set:
    if coding_gene[:5] == 'gene-':
        file_out.write(coding_gene[5:] + '\n')
    else:
        file_out.write(coding_gene + '\n') 

