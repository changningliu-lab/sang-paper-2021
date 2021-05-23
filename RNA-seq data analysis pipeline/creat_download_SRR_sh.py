#输入：data_for_analysis.txt
#输出：work1_download_SRR.sh
import sys
file_in = open(sys.argv[1], 'r')
file_out = open(sys.argv[2], 'w')

for line in file_in:
    if line[0] != ' ':
        item = line.strip().split('__')
        ID1 = item[0][:6]
        ID2 = item[0]
        file_out.write('ascp -i /home/sangye/miniconda3/opt/aspera/connect/etc/asperaweb_id_dsa.openssh -k 1 -T -l 80m anonftp@ftp.ncbi.nlm.nih.gov:/sra/sra-instant/reads/ByRun/sra/SRR/' + ID1 + '/' + ID2 + '/' + ID2 + '.sra' + ' SRRsra_dataset' + '\n')

file_in.close()
file_out.close()
        
