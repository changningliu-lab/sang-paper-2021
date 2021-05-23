#参数1：_cluster_coverage/_new.txt

import sys
from collections import defaultdict

file_in1 = open(sys.argv[1],'r')
lnc_info_dict = defaultdict(list)
key = 0
for line in file_in1:
    item = line.split()
    if item[3].strip() == '-'*150:
        key = key + 1
        lnc_info_dict[key].append(item[1])
        lnc_info_dict[key].append(item[2])
        lnc_info_dict[key].append([])
        lnc_info_dict[key].append([])
    else:
        if item[0] not in lnc_info_dict[key]:
            lnc_info_dict[key].insert(0,item[0])
        if item[1] not in lnc_info_dict[key]:
            lnc_info_dict[key].insert(1,item[1])
        if item[13] not in lnc_info_dict[key]:
            lnc_info_dict[key].insert(2,item[13]) 
        if int(item[8]) < int(item[9]):
            start = int(item[8])
            end = int(item[9])  
        elif int(item[8]) > int(item[9]):
            start = int(item[9])
            end = int(item[8])
        lnc_info_dict[key][5].append(start)
        lnc_info_dict[key][5].append(end)
        lnc_info_dict[key][6].append((start, end))

for keys,value in lnc_info_dict.items():
    location_min_value = min(value[5])
    location_max_value = max(value[5])

    end_index = sorted(value[6])[0][1] 
    start_index = sorted(value[6])[0][0] 
    tu = (start_index, end_index)
    exonnum = 1
    exon_dict = {}
    for (start, end) in sorted(value[6]):
        if (start, end) != (start_index, end_index):
            if start > end_index:
                exon_dict['exon' + '_' + str(exonnum)] = tu       
                exonnum = exonnum + 1
                tu = (start, end)
                end_index = end
                start_index = start
            else:
                if end < end_index:
                    tu = (start_index, end_index)
                elif end > end_index:
                    tu = (start_index, end)
                    end_index = end
    exon_dict['exon' + '_' + str(exonnum)] = tu
    if float(value[3].split(':')[1][:-1]) >= 80:
        print('\t'.join([value[1], '.', 'transcript', str(location_min_value), str(location_max_value), '.', value[2], '.', 'gene_id "{}"; transcript_id "{}"; cluster_coverage "{}";'.format(value[0] + '_' + str(keys), value[0] + '_' + str(keys), value[3].split(':')[1])]))
        if value[2] == '+':
            for exons,location in exon_dict.items():
                print('\t'.join([value[1], '.', 'exon', str(location[0]), str(location[1]), '.', value[2], '.', 'gene_id "{}"; transcript_id "{}"; exon_number "{}";'.format(value[0] + '_' + str(keys), value[0] + '_' + str(keys), exons)]))
        else:
           exon_list = sorted(exon_dict.items(),key=lambda  item:item[1])
           for exons,location in reversed(exon_list):
               print('\t'.join([value[1], '.', 'exon', str(location[0]), str(location[1]), '.', value[2], '.', 'gene_id "{}"; transcript_id "{}"; exon_number "{}";'.format(value[0] + '_' + str(keys), value[0] + '_' + str(keys), exons)]))
file_in1.close()

