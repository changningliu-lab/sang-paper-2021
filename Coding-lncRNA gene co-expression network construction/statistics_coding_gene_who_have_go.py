file_in1 = open('tair_id2GO_text_format_slim.txt', 'r')
file_in2 = open('SRR_p0.05.Network', 'r')

gene_set1 = set()
for line in file_in1:
    if line[0] != '#':
        gene = line.split('\t')[0]
        gene_set1.add(gene)
gene_set = set()
for line in file_in2:
    if line[0] != '#':
        item = line.split('\t')
        if item[0][:5] == "gene-" or item[0][:4] == "rna-" or item[0][:3] == "id-":
            gene1 = item[0].split('-')[1]
        if item[1][:5] == "gene-" or item[1][:4] == "rna-" or item[1][:3] == "id-":
            gene2 = item[1].split('-')[1]
        gene_set.add(gene1)
        gene_set.add(gene2)

intersection_gene_set = gene_set1.intersection(gene_set)
network_coding_gene_num = len(gene_set)
intersection_gene_num = len(intersection_gene_set)
percent = intersection_gene_num/network_coding_gene_num

print(str(intersection_gene_num))
print(str(network_coding_gene_num))
print('%.4f' % percent)



