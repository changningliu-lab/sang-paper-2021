#参数1：plan/animalt_after_CPC2_fasta_result/*.fasta   输出：plant/animal_after_CPC2_fasta_result_rm_refseq_sequence_result/*.fasta

import sys

file_out = open(sys.argv[2], 'w')

file_in = open(sys.argv[1], 'r')
for line in file_in:    
    if line[0] == '>':
        item = line.split()
        if (item[0][1:3] == 'XR') or (item[0][1:3] == 'NR'):
            flag = 0
        else:
            flag = 1
    if flag == 1:
        file_out.write(line)
    
file_in.close()
file_out.close()
