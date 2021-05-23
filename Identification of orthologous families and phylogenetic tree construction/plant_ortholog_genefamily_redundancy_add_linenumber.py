file_in = open('plant_ortholog_genefamily_redundancy.txt', 'r')
file_out = open('plant_ortholog_genefamily_redundancy_add_linenumber.txt', 'w')
line_number = 0
for line in file_in:
    line_number = line_number + 1
    file_out.write('\t'.join([str(line_number), line]))
file_in.close()
file_out.close()

