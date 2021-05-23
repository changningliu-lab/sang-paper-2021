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
        lnc_info_dict[key].append(item[1].split(':')[-1][:-1])
        lnc_info_dict[key].append(item[2].split(':')[-1])
        lnc_info_dict[key].append([])
    else:
        if item[0] not in lnc_info_dict[key]:
            lnc_info_dict[key].insert(0,item[0])
        if item[1] not in lnc_info_dict[key]:
            lnc_info_dict[key].insert(1,item[1])
        if item[-1].strip() not in lnc_info_dict[key]:
            lnc_info_dict[key].insert(2,item[-1].strip()) 
        lnc_info_dict[key][5].append(int(item[8]))
        lnc_info_dict[key][5].append(int(item[9]))

for keys,value in lnc_info_dict.items():
    location_min_value = min(value[5])
    location_max_value = max(value[5])
    print(str(keys) + '\t' + '\t'.join(value[:3] + [str(location_min_value), str(location_max_value)] + value[3:5]))
file_in1.close()

