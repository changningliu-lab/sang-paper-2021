#input:/home/sangye/lncRNA_evolution/25_plant_refseq_gff/*gff
#output:/home/sangye/lncRNA_evolution/data_analysis/lnc_genome_mapping/*gff

import sys
import re
file_in = open(sys.argv[1], "r")
file_out = open(sys.argv[2], "w")
flag = 0
for line in file_in:
    if line[0] != "#":
        item = line.strip().split("\t")
        feature = item[2]
        if feature == "gene":
            try:
                gene_biotype = re.search("gene_biotype=([^;]+)", item[8])
                #print(gene_biotype.group(1))
            except:
                print('#########' + line)
                sys.exit()
            if gene_biotype.group(1) == "protein_coding":
                flag = 1
                file_out.write(line)
            else:
                flag = 0
        elif feature == "mRNA":
            flag = 1
            file_out.write(line)
        elif (feature == "exon") or (feature == "intron") or(feature == "CDS"):
            if flag == 1:
                file_out.write(line)
file_in.close()
file_out.close()
