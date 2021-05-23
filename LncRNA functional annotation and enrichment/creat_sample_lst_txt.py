tissue_SRR_dict = {}
with open('tissue_SRR.txt') as file_in:
    for line in file_in:
        item = line.split('\t')
        tissue = item[0]
        SRR_list = item[1].split(';')[:-1]
        tissue_SRR_dict[tissue] = SRR_list

file_out = open('sample_lst.txt', 'w')
for key,value in tissue_SRR_dict.items():
    for SRR in value:
        file_out.write('\t'.join([SRR, '/home/sangye/lncRNA_evolution/RNA-seq_analysis/transcriptome_analysis/3_stringtie_result_methods2/stringtie_gtf_result/'+SRR+'.gtf'])+'\n')
file_in.close()
file_out.close()
