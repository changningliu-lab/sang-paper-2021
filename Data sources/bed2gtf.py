#参数1:_cpc2.fasta
#参数2：.bed 
#输出(print)：>>.gtf

import sys
from collections import defaultdict

genename_liast = []
with open(sys.argv[1], 'r') as fasta:
    for line in fasta:
        if line[0] == '>':
            genename = line[1:-1]
            genename_liast.append(genename)


file_in = open(sys.argv[2], 'r')
gene_info = defaultdict(list)
for line in file_in:
    item = line.strip().split()
    genename = item[3]
    if genename in genename_liast:
        chrome = item[0]
        if len(chrome) <= 5:
            chrome_start = int(item[1])
            chrome_end = int(item[2])
            strand = item[5]
            exon_num = item[9]
            exon_size_list = item[10].split(',')
            exon_start_list = item[11].split(',')[:-1]

            exon_list = []
            num = -1
            for exon_starts in exon_start_list:
                num = num + 1
                exon_start = chrome_start + int(exon_starts)
                exon_end = exon_start + int(exon_size_list[num])
                exon_list.append((exon_start, exon_end))

            print('\t'.join([chrome, '.', 'transcript', str(chrome_start), str(chrome_end), '.', strand, '.', 'gene_id "{}"; transcript_id "{}";'.format(genename, genename)]))
            if strand == '+':
                count = 0
                for start,end in exon_list:
                    count = count + 1
                    print('\t'.join([chrome, '.', 'exon', str(start), str(end), '.', strand, '.', 'gene_id "{}"; transcript_id "{}"; exon_number "exon_{}";'.format(genename, genename, str(count))]))
            else:
                count = 0
                for start,end in list(reversed(exon_list)):
                    count = count + 1
                    print('\t'.join([chrome, '.', 'exon', str(start), str(end), '.', strand, '.', 'gene_id "{}"; transcript_id "{}"; exon_number "exon_{}";'.format(genename, genename, str(count))]))

file_in.close()
fasta.close()
    

