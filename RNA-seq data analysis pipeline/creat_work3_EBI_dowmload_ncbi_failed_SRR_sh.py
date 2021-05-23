file_in = open('work1_download_SRR_nohup.out', 'r')
file_out = open('work4_EBI_dowmload_ncbi_failed_SRR.sh' , 'w')

for line in file_in:
    if line[:5] == 'Error':
        item = line.split('/')
        ID1 = item[-2][:6]
        ID2 = '00' + item[-2][-1]
        ID3 = item[-2]
        file_out.write('ascp -QT -l 200m -P33001 -i /home/sangye/miniconda3/opt/aspera/connect/etc/asperaweb_id_dsa.openssh era-fasp@fasp.sra.ebi.ac.uk:/vol1/srr/' + ID1 + '/' + ID2 + '/' + ID3 + '/' + ' SRRsra_dataset' + '\n')

file_in.close()
file_out.close()

        
