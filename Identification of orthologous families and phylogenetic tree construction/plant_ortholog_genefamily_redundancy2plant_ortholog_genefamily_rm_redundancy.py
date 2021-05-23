input_file_name = 'plant_ortholog_genefamily_redundancy_add_linenumber.txt'
output_file_name = 'plant_ortholog_genefamily_rm_redundancy.txt'
input_file = open(input_file_name, 'r')
output_file = open(output_file_name, 'w')

for line in input_file:
    species_list = []
    item = line.split('\t')
    key = item[0]
    info = item[1]
    species_lnc_list = info.split(';')
    for i in species_lnc_list[1:-1]:
        species = i.split('#')[0]
        if species not in species_list:
            species_list.append(species)
    output_file.write(key + '\t' + ';'.join([str(len(species_list))] + species_list) + '\n')
    
input_file.close()
output_file.close()
