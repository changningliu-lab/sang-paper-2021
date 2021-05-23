#input1:lnc2go_second_go_enrichment_input_slim_fulllist_p0.01_allBP.txt
#input2:rename_1477lnc.txt
#output:statistics_lnc2go_class.txt

file_in1 = open('lnc2go_second_go_enrichment_input_slim_fulllist_p0.01_allBP.txt', 'r')
file_in2 = open('rename_1477lnc.txt', 'r')
file_out = open('statistics_lnc2go_class_slim_fulllist_p0.01_allBP.txt', 'w')
class2name_dict = {}
for line in file_in2:
    item = line.strip().split()
    if line[0] != 'T':
        taxon = item[0]
        oldname = item[1]
        newname = item[2]
        class2name_dict[newname] = taxon
taxon2gonum_dict = {}
taxon2gonum_dict['Arabidopsis'] = 0
taxon2gonum_dict['Brassicaceae'] = 0
taxon2gonum_dict['Dicotyledon'] = 0
taxon2gonum_dict['Angiosperm'] = 0
for line in file_in1:
    item = line.split('\t')
    name = item[0]
    GOnum = len(item[1].split(';')[:-1])
    taxons = class2name_dict[name] 
    taxon2gonum_dict[taxons] = taxon2gonum_dict[taxons] + int(GOnum)
    file_out.write(taxons + '\t' + line)
for key,value in taxon2gonum_dict.items():
    file_out.write(key + '\t' + str(value) + '\n')        

file_in1.close()
file_in2.close()
file_out.close()
    
