#input1:SRR_lnc.Norm
#output:rename_1477lnc.txt
file_in1 = open('SRR_lnc.Norm' ,'r') #获得1477条lnc原来的名字
file_out = open('rename_1477lnc.txt', 'w')

file_out.write('\t'.join(['Taxon', 'old_name', 'new_name']) + '\n')
count = -1
for line in file_in1:
    count = count + 1
    item = line.split('\t')
    if item[0] != 'Taxon':
        taxon = item[0]
        lnc_id = item[1]
        if len(str(count)) == 1:
            file_out.write(taxon + '\t' + lnc_id + '\t' + 'Ath000' + str(count) + '\n')
        elif len(str(count)) == 2:
            file_out.write(taxon + '\t' + lnc_id + '\t' + 'Ath00' + str(count) + '\n')
        elif len(str(count)) == 3:
            file_out.write(taxon + '\t' + lnc_id + '\t' + 'Ath0' + str(count) + '\n')
        elif len(str(count)) == 4:
            file_out.write(taxon + '\t' + lnc_id + '\t' + 'Ath' + str(count) + '\n')
file_in1.close()
file_out.close()
    