file_in = open('lnc2go_second_go_enrichment_input_slim_fulllist_p0.01_allBP.txt', 'r')
file_out = open('lnc2go_one2one_format.txt', 'w')

for line in file_in:
    item = line.split()
    genename = item[0]
    GOs_list = item[1].split(';')[:-1]
    for GO in GOs_list:
        file_out.write(genename + '\t' + GO + '\n')
file_in.close()
file_out.close()