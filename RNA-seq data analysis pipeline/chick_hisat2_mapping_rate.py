#input:work*_hisat2_mapping*.sh_nohup.out
#output:chick_hisat2_mapping_rate.txt
import sys

file_in = open(sys.argv[1], 'r')
file_out = open(sys.argv[2], 'w')
 
for line in file_in:
    if line[7:-1] == 'overall alignment rate':
        mapping_rate = float(line[:5])
    if line[:7] == "SUCCESS":   
       SRR_ID = line.strip().split('/')[-1][:-4]
       if mapping_rate < 90:
            file_out.write(SRR_ID + '\t' + str(mapping_rate)+'\n')

file_in.close()
file_out.close()