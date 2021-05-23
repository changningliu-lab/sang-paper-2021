from collections import defaultdict 

file_in = open('SRR_p0.05.Network', 'r')
coding2coding = 0
coding2lncRNA = 0
lncRNA2lncRNA = 0
coding_num = set()
lncRNA_num = set()
for line in file_in:
    if line[0] != '#':
        item = line.strip().split('\t')
        node1 = item[0]
        node2 = item[1]
        if (node1[:3] == 'id-') or (node1[:4] == 'rna-'):
            node1 = 'gene-' + '-'.join(node1.split('-')[1:])
        if (node2[:3] == 'id-') or (node2[:4] == 'rna-'):
            node2 = 'gene-' + '-'.join(node2.split('-')[1:])
        
        if (node1[:4] == 'gene') and (node2[:4] == 'gene'):
            coding2coding = coding2coding + 1
            coding_num.add(node1)
            coding_num.add(node2)
        elif (node1[:4] != 'gene') and (node2[:4] != 'gene'):
            lncRNA2lncRNA = lncRNA2lncRNA + 1
            lncRNA_num.add(node1)
            lncRNA_num.add(node2)
        else:
            coding2lncRNA = coding2lncRNA + 1
            if node1[:4] == 'gene':
                coding_num.add(node1)
                lncRNA_num.add(node2)
            else:
                coding_num.add(node2)
                lncRNA_num.add(node1)

file_out = open('statisics_SRR_p0.05.Network_future.txt', 'w')
file_out.write('coding2coding_edge:' + str(coding2coding) + '\n' + 'lncRNA2lncRNA_edge:' + str(lncRNA2lncRNA) + '\n' + 'coding2lncRNA_edge:' + str(coding2lncRNA) + '\n' + 'coding_num:' + str(len(coding_num)) + '\n' + 'lncRNA_num:' + str(len(lncRNA_num)) + '\n')
file_out.close()
file_in.close()