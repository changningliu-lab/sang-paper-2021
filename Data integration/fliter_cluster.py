#参数1：物种*_cluster_coverage/lncname_*new1.txt(植物)*new.txt(动物)    
#参数2：物种*_lncrnas_length.txt

import sys
import os 
from collections import defaultdict

cluster_info_dict = {}
file_in = open(sys.argv[1], 'r')
for line in file_in:
    item = line.strip().split()
    if line[0].isdigit():
        key = '*'.join(item[:3])
    else:
        identity = float(item[2])
        qury_start = float(item[6])
        qury_end = float(item[7])
        strand = item[-1]
        if strand == '+':
            genome_start = float(item[8])
            genome_end = float(item[9])
        else:
            genome_start = float(item[9])
            genome_end = float(item[8])
        if (key+'*'+strand) not in cluster_info_dict:
            cluster_info_dict[key+'*'+strand] = defaultdict(list)
        if strand == '+':
            cluster_info_dict[key+'*'+strand][(qury_start, qury_end, (100-identity), genome_start, genome_end)].append((genome_start, genome_end))
            cluster_info_dict[key+'*'+strand][(qury_start, qury_end, (100-identity), genome_start, genome_end)].append(identity)
            cluster_info_dict[key+'*'+strand][(qury_start, qury_end, (100-identity), genome_start, genome_end)].append(line)
        else:
            cluster_info_dict[key+'*'+strand][(qury_start, qury_end, (100-identity), 9000000000000000-genome_end, 9000000000000000-genome_start)].append((genome_start, genome_end))
            cluster_info_dict[key+'*'+strand][(qury_start, qury_end, (100-identity), 9000000000000000-genome_end, 9000000000000000-genome_start)].append(identity)
            cluster_info_dict[key+'*'+strand][(qury_start, qury_end, (100-identity), 9000000000000000-genome_end, 9000000000000000-genome_start)].append(line)

#读_lncrnas_length.txt
lengthDict = {}
with open(sys.argv[2]) as length:
    for line in length:
        itemm = line.strip().split()
        name = itemm[0]
        lnclength = itemm[1]
        lengthDict[name] = int(lnclength)

for cluster,info in cluster_info_dict.items():
    value = sorted(info.items(),key=lambda  item:item[0])
    qury_end_idx = 0
    cluster_line_list = []
    cluster2_line_list = []
    cluster3_line_list = []
    cluster4_line_list = []
    genome_start_end_list = []
    num = 0
    strand = cluster.split('*')[-1]
    if strand == '+':
        for tu in value:       
            num = num + 1        
            qury_start = float(tu[0][0])
            qury_end = float(tu[0][1])
            identity = float(tu[1][1])
            genome_start = float(tu[1][0][0])
            genome_end = float(tu[1][0][1])
            if qury_start >= qury_end_idx:
                if num == 1:
                    cluster_line_list.append(tu[1][2])    
                    genome_start_end_list.append((float(tu[1][0][0]), float(tu[1][0][1])))
                    identity_idx = float(tu[1][1])
                    qury_start_idx = float(tu[0][0])
                    qury_end_idx = float(tu[0][1])      
      
                else:
                    if genome_start > genome_start_end_list[-1][0]:
                        cluster_line_list.append(tu[1][2])
                        genome_start_end_list.append((float(tu[1][0][0]), float(tu[1][0][1])))
                        identity_idx = float(tu[1][1])
                        qury_start_idx = float(tu[0][0])
                        qury_end_idx = float(tu[0][1])
            else:
                qury_length = qury_end - qury_start + 1
                qury_idx_length = qury_end_idx - qury_start_idx + 1
                min_length = min((qury_length, qury_idx_length))
                if min_length == qury_length and min_length != qury_idx_length:
                    flag = 0
                elif min_length != qury_length and min_length == qury_idx_length:
                    flag = 1
                else :
                    flag = 2
                if qury_end > qury_end_idx:
                    overlap = qury_end_idx - qury_start + 1
                elif qury_end <= qury_end_idx:
                    overlap = qury_end - qury_start + 1
                overlap_cov = overlap/min_length
                if overlap_cov >= 0.8:
                    if flag == 2:
                        if identity > identity_idx:
                            if len(genome_start_end_list) > 1:
                                temp = genome_start_end_list[-1]
                                genome_start_end_list.pop()
                                if genome_start > genome_start_end_list[-1][0]:
                                    cluster_line_list.pop()
                                    cluster_line_list.append(tu[1][2])
                                    genome_start_end_list.append((float(tu[1][0][0]), float(tu[1][0][1])))
                                    identity_idx = float(tu[1][1])
                                    qury_start_idx = float(tu[0][0])
                                    qury_end_idx = float(tu[0][1])
                                else:
                                    genome_start_end_list.append(temp)
                            else:
                                cluster_line_list.pop()
                                cluster_line_list.append(tu[1][2])
                                genome_start_end_list.pop() 
                                genome_start_end_list.append((float(tu[1][0][0]), float(tu[1][0][1])))
                                identity_idx = float(tu[1][1])
                                qury_start_idx = float(tu[0][0])
                                qury_end_idx = float(tu[0][1])
                        elif identity == identity_idx:
                            if cluster2_line_list:
                                column = cluster2_line_list[-1].split('\t')
                                start = float(column[6])
                                end = float(column[7])
                                identity2 = float(column[2])
                                lengthh = end - start + 1
                                min_lengthh = min(lengthh, qury_length)
                                overlap1 = (end - qury_start + 1)/min_lengthh
                                if (overlap1 >= 0.8) and (identity == identity2):                       
                                    if cluster3_line_list:
                                        column3 = cluster3_line_list[-1].split('\t')
                                        start3 = float(column3[6])
                                        end3 = float(column3[7])
                                        identity3 = float(column3[2])
                                        lengthh3 = end3 - start3 + 1
                                        min_lengthh3 = min(lengthh3, qury_length)
                                        overlap3 = (end3 - qury_start + 1)/min_lengthh3
                                        if (overlap3 >= 0.8) and (identity == identity3):
                                            cluster4_line_list.append(tu[1][2])
                                        elif (overlap3 >= 0.8) and (identity > identity3):
                                            cluster3_line_list.pop()
                                            cluster3_line_list.append(tu[1][2])
                                        else:
                                            cluster3_line_list.append(tu[1][2])
                                    else:
                                        cluster3_line_list.append(tu[1][2])
                                elif (overlap1 >= 0.8) and (identity > identity2): 
                                    cluster2_line_list.pop()
                                    cluster2_line_list.append(tu[1][2])
                                else:
                                    cluster2_line_list.append(tu[1][2])
                            else:
                                cluster2_line_list.append(tu[1][2]) 
                    elif flag == 0:
                        if identity - identity_idx > 1:
                            if len(genome_start_end_list) > 1:
                                temp = genome_start_end_list[-1]
                                genome_start_end_list.pop()
                                if genome_start > genome_start_end_list[-1][0]:
                                    cluster_line_list.pop()
                                    cluster_line_list.append(tu[1][2])
                                    genome_start_end_list.append((float(tu[1][0][0]), float(tu[1][0][1])))
                                    identity_idx = float(tu[1][1])
                                    qury_start_idx = float(tu[0][0])
                                    qury_end_idx = float(tu[0][1])
                                else:
                                    genome_start_end_list.append(temp)
                            else:
                                cluster_line_list.pop()
                                cluster_line_list.append(tu[1][2])
                                genome_start_end_list.pop() 
                                genome_start_end_list.append((float(tu[1][0][0]), float(tu[1][0][1])))
                                identity_idx = float(tu[1][1])
                                qury_start_idx = float(tu[0][0])
                                qury_end_idx = float(tu[0][1])
                    else:
                        if identity - identity_idx > -1:
                            if len(genome_start_end_list) > 1:
                                temp = genome_start_end_list[-1]
                                genome_start_end_list.pop()
                                if genome_start > genome_start_end_list[-1][0]:
                                    cluster_line_list.pop()
                                    cluster_line_list.append(tu[1][2])
                                    genome_start_end_list.append((float(tu[1][0][0]), float(tu[1][0][1])))
                                    identity_idx = float(tu[1][1])
                                    qury_start_idx = float(tu[0][0])
                                    qury_end_idx = float(tu[0][1])
                                else:
                                    genome_start_end_list.append(temp)
                            else:
                                cluster_line_list.pop()
                                cluster_line_list.append(tu[1][2])
                                genome_start_end_list.pop() 
                                genome_start_end_list.append((float(tu[1][0][0]), float(tu[1][0][1])))
                                identity_idx = float(tu[1][1])
                                qury_start_idx = float(tu[0][0])
                                qury_end_idx = float(tu[0][1])                   
                else:
                    if genome_start > genome_start_end_list[-1][0]:
                        cluster_line_list.append(tu[1][2])
                        genome_start_end_list.append((float(tu[1][0][0]), float(tu[1][0][1])))
                        identity_idx = float(tu[1][1])
                        qury_start_idx = float(tu[0][0])
                        qury_end_idx = float(tu[0][1])
    else:
        for tu in value:  
            num = num + 1        
            qury_start = float(tu[0][0])
            qury_end = float(tu[0][1])
            identity = float(tu[1][1])
            genome_start = float(tu[1][0][0])
            genome_end = float(tu[1][0][1])
            if qury_start >= qury_end_idx:
                if num == 1:
                    cluster_line_list.append(tu[1][2])    
                    genome_start_end_list.append((float(tu[1][0][0]), float(tu[1][0][1])))
                    identity_idx = float(tu[1][1])
                    qury_start_idx = float(tu[0][0])
                    qury_end_idx = float(tu[0][1])  
                else:
                    if genome_end < genome_start_end_list[-1][1]:
                        cluster_line_list.append(tu[1][2])
                        genome_start_end_list.append((float(tu[1][0][0]), float(tu[1][0][1])))
                        identity_idx = float(tu[1][1])
                        qury_start_idx = float(tu[0][0])
                        qury_end_idx = float(tu[0][1])
            else:
                qury_length = length = qury_end - qury_start + 1
                qury_idx_length = qury_end_idx - qury_start_idx + 1
                min_length = min((qury_length, qury_idx_length))
                if min_length == qury_length and min_length != qury_idx_length:
                    flag = 0
                elif min_length != qury_length and min_length == qury_idx_length:
                    flag = 1
                else :
                    flag = 2
                if qury_end > qury_end_idx:
                    overlap = qury_end_idx - qury_start + 1
                elif qury_end <= qury_end_idx:
                    overlap = qury_end - qury_start + 1
                overlap_cov = overlap/min_length
                if overlap_cov >= 0.8:
                    if flag == 2:
                        if identity > identity_idx:
                            if len(genome_start_end_list) > 1:
                                temp = genome_start_end_list[-1]
                                genome_start_end_list.pop()
                                if genome_end < genome_start_end_list[-1][1]:
                                    cluster_line_list.pop()
                                    cluster_line_list.append(tu[1][2])
                                    genome_start_end_list.append((float(tu[1][0][0]), float(tu[1][0][1])))
                                    identity_idx = float(tu[1][1])
                                    qury_start_idx = float(tu[0][0])
                                    qury_end_idx = float(tu[0][1])
                                else:
                                    genome_start_end_list.append(temp)
                            else:
                                cluster_line_list.pop()
                                cluster_line_list.append(tu[1][2])
                                genome_start_end_list.pop() 
                                genome_start_end_list.append((float(tu[1][0][0]), float(tu[1][0][1])))
                                identity_idx = float(tu[1][1])
                                qury_start_idx = float(tu[0][0])
                                qury_end_idx = float(tu[0][1])
                        elif identity == identity_idx:    
                            if cluster2_line_list:
                                column = cluster2_line_list[-1].split('\t')
                                start = float(column[6])
                                end = float(column[7])
                                identity2 = float(column[2])
                                lengthh = end - start + 1
                                min_lengthh = min(lengthh, qury_length)
                                overlap1 = (end - qury_start + 1)/min_lengthh
                                if (overlap1 >= 0.8) and (identity == identity2):                       
                                    if cluster3_line_list:
                                        column3 = cluster3_line_list[-1].split('\t')
                                        start3 = float(column3[6])
                                        end3 = float(column3[7])
                                        identity3 = float(column3[2])
                                        lengthh3 = end3 - start3 + 1
                                        min_lengthh3 = min(lengthh3, qury_length)
                                        overlap3 = (end3 - qury_start + 1)/min_lengthh3
                                        if (overlap3 >= 0.8) and (identity == identity3):
                                            cluster4_line_list.append(tu[1][2])
                                        elif (overlap3 >= 0.8) and (identity > identity3):
                                            cluster3_line_list.pop()
                                            cluster3_line_list.append(tu[1][2])
                                        else:
                                            cluster3_line_list.append(tu[1][2])
                                    else:
                                        cluster3_line_list.append(tu[1][2])
                                elif (overlap1 >= 0.8) and (identity > identity2): 
                                    cluster2_line_list.pop()
                                    cluster2_line_list.append(tu[1][2])
                                else:
                                    cluster2_line_list.append(tu[1][2])
                            else:
                                cluster2_line_list.append(tu[1][2])         
                    elif flag == 0:                  
                        if identity - identity_idx > 1:
                            if len(genome_start_end_list) > 1:
                                temp = genome_start_end_list[-1]
                                genome_start_end_list.pop()
                                if genome_end < genome_start_end_list[-1][1]:
                                    cluster_line_list.pop()
                                    cluster_line_list.append(tu[1][2])
                                    genome_start_end_list.append((float(tu[1][0][0]), float(tu[1][0][1])))
                                    identity_idx = float(tu[1][1])
                                    qury_start_idx = float(tu[0][0])
                                    qury_end_idx = float(tu[0][1])
                                else:
                                    genome_start_end_list.append(temp)
                            else:
                                cluster_line_list.pop()
                                cluster_line_list.append(tu[1][2])
                                genome_start_end_list.pop() 
                                genome_start_end_list.append((float(tu[1][0][0]), float(tu[1][0][1])))
                                identity_idx = float(tu[1][1])
                                qury_start_idx = float(tu[0][0])
                                qury_end_idx = float(tu[0][1])
                    else:
                        if identity - identity_idx > -1:
                            if len(genome_start_end_list) > 1:
                                temp = genome_start_end_list[-1]
                                genome_start_end_list.pop()
                                if genome_end < genome_start_end_list[-1][1]:
                                    cluster_line_list.pop()
                                    cluster_line_list.append(tu[1][2])
                                    genome_start_end_list.append((float(tu[1][0][0]), float(tu[1][0][1])))
                                    identity_idx = float(tu[1][1])
                                    qury_start_idx = float(tu[0][0])
                                    qury_end_idx = float(tu[0][1])
                                else:
                                    genome_start_end_list.append(temp)
                            else:
                                cluster_line_list.pop()
                                cluster_line_list.append(tu[1][2])
                                genome_start_end_list.pop() 
                                genome_start_end_list.append((float(tu[1][0][0]), float(tu[1][0][1])))
                                identity_idx = float(tu[1][1])
                                qury_start_idx = float(tu[0][0])
                                qury_end_idx = float(tu[0][1])
                else:
                    if genome_end < genome_start_end_list[-1][1]:
                        cluster_line_list.append(tu[1][2])
                        genome_start_end_list.append((float(tu[1][0][0]), float(tu[1][0][1])))
                        identity_idx = float(tu[1][1])
                        qury_start_idx = float(tu[0][0])
                        qury_end_idx = float(tu[0][1])

    def cov_identity_caculate(lst):
        index = -1
        idx = float('inf')
        sumlength = 0
        identity_weighing_numerator = 0
        identity_weighing_denominator = 0
        for line in lst:
            items = line.split('\t')   
            lncnames = items[0] 
            strands = items[-1].strip()
            if int(items[8]) > int(items[9]):
                genomic_start = int(items[9])
                genomic_end = int(items[8])
            else:
                genomic_start = int(items[8])
                genomic_end = int(items[9])
            identities = float(items[2])
            identity_weighing_numerator = identity_weighing_numerator + identities*(genomic_end - genomic_start + 1)
            identity_weighing_denominator = identity_weighing_denominator + (genomic_end - genomic_start + 1)
            if strands == '+':
                if genomic_start > index:
                    efflength = genomic_end - genomic_start + 1
                    index = genomic_end
                    sumlength = sumlength + efflength
                else:
                    if genomic_end > index:
                        efflength = genomic_end - index
                        index = genomic_end
                        sumlength = sumlength + efflength
            else:
                if genomic_end < idx:
                    efflength = genomic_end - genomic_start + 1
                    idx = genomic_start
                    sumlength = sumlength + efflength
                else:
                    efflength = idx - genomic_start
                    idx = genomic_start
                    sumlength = sumlength + efflength
        identity_weighing = identity_weighing_numerator/identity_weighing_denominator
        cov = sumlength/lengthDict[lncnames]*100
        return(identity_weighing, cov)

    identity_weighing, cov = cov_identity_caculate(cluster_line_list)
    print('\t'.join(['1', 'cluster_coverage:'+str('%.2f'%cov)+'%', 'identity_weighing:'+str('%.3f'%identity_weighing), '-'*150]))
    for line in cluster_line_list: 
        print(line.strip()) 
    cov_index = cov
    if cluster2_line_list:
        identity_weighing, cov = cov_identity_caculate(cluster2_line_list)
        if cov == cov_index:
            print('\t'.join(['2', 'cluster_coverage:'+str('%.2f'%cov)+'%', 'identity_weighing:'+str('%.3f'%identity_weighing), '-'*150]))
            for line in cluster2_line_list: 
                print(line.strip())
    if cluster3_line_list:
        identity_weighing, cov = cov_identity_caculate(cluster3_line_list)
        if cov == cov_index:
            print('\t'.join(['3', 'cluster_coverage:'+str('%.2f'%cov)+'%', 'identity_weighing:'+str('%.3f'%identity_weighing), '-'*150]))
            for line in cluster3_line_list: 
                print(line.strip())
    if cluster4_line_list:
        identity_weighing, cov = cov_identity_caculate(cluster4_line_list)
        if cov == cov_index:
            print('\t'.join(['3', 'cluster_coverage:'+str('%.2f'%cov)+'%', 'identity_weighing:'+str('%.3f'%identity_weighing), '-'*150]))
            for line in cluster4_line_list: 
                print(line.strip())
        








                            

                                
                            






                    

     
        



