#整合参数物种所有lncRNAs在基因组上的位置信息
#两条lncRNAs的overlap >= 较短一条的50%就合并位置，并保留lncRNAs名称。
#参数1：unified_blast_define_position_algorithm/plant_blast-10-4000_all_lncrnas_gtf/*gtf
#输出1：在.sh文件里 >> plant(animal)_pseudo_and_normal_lncrnas_gtf/物种_pseudo_and_normal_lncrnas.gtf


import sys
import os 
from collections import defaultdict

#将物种_lncrnas_position_result.txt中的lncRNAs信息存到genelocation_dict字典里
genelocation_dict = {}
gene_exons_dict = defaultdict(list)
genename_line = defaultdict(list)
file_in1 = open(sys.argv[1], 'r')
for line in file_in1:              
    info = line.strip().split('\t')
    genename_num = info[8].split(';')[0][9:-1]
    chrome = info[0]
    strand = info[6]
    start = int(info[3])
    end = int(info[4])
    genename_line[genename_num].append(line)
    if info[2] == 'transcript':
        if (chrome + ' ' + strand) not in genelocation_dict:
            genelocation_dict[chrome + ' ' + strand] = {}
        if (genename_num) not in genelocation_dict[chrome + ' ' + strand]:
            genelocation_dict[chrome + ' ' + strand][genename_num] = (start,end)
    elif info[2] == 'exon':
        gene_exons_dict[genename_num].append((start,end))
file_in1.close()

def cluster_list(value):
    cpvalue = [value[0]]
    clustered = []
    end_index = value[0][1][1]
    for (genename2,location2) in value[1:]:        
        (start2,end2) = location2        
        if start2 > end_index:
            clustered.extend(cpvalue)
            cpvalue = [(genename2,location2)]
            end_index = end2
        else:
            matched = 0
            length2 = end2 - start2 + 1
            end_index = max(end2, end_index)
            for i in range(len(cpvalue)-1,-1,-1):
                (genename1,location1) = cpvalue[i]
                (start1,end1) = location1
                length1 = end1 - start1 + 1                         
                overlap = min(end1,end2) - start2 + 1                                
                if overlap/min(length1,length2) >= 0.8:
                    genename1 = genename1 + "*" + genename2
                    location1 = (start1, max(end1,end2))
                    cpvalue[i] = (genename1,location1)
                    matched = 1
                    break
                else:
                    continue
            if not matched:
                cpvalue.append((genename2,location2))
    clustered.extend(cpvalue)
    return clustered
    
#对lncRNAs进行合并
gene_cluster_dict = {}
merged_again = 0
for chr_strand, value in genelocation_dict.items():
    value = sorted(value.items(),key=lambda item:item[1])
    #print(chr_strand,"original:",len(value))
    clustered = cluster_list(value)
    #print(chr_strand,"1 time:",len(clustered))
    merged_again += len(clustered)
    while (clustered != value):
        value = clustered
        clustered = cluster_list(value)
    #print(chr_strand,"finally:",len(clustered),"\n")
    merged_again -= len(clustered)
    gene_cluster_dict[chr_strand] = clustered
#print(merged_again)

#将该物种的fasta序列读进fasta_sequence_dict
#参数2：merge_database_step1_CPC2/plant(animal)_after_CPC2_fasta_result_rm_refseq_sequence_result/该物种_lncrnas.fasta
#fasta_sequence_dict = defaultdict(list)
#file_in2 = open(sys.argv[2], 'r')
#for line in file_in2: 
#    if line[0] == '>':
#        item = line.split()
#        if line[1:5] == 'lcl|':
#            genename = item[0][5:]
#        else:
#            genename = item[0][1:]
#    else:
#        fasta_sequence_dict[genename].append(line)
#file_in2.close()


#path = sys.argv[2] + '/' + '_'.join(sys.argv[1].split('/')[-1].split('_')[:2] + ['cluster_genename'])
#if not os.path.exists(path): os.mkdir(path)

#final_mutiple_gene_cluster = defaultdict(list)
all_cluster_genename_list = []
cluster_single_genename_list = []
for (key,value) in gene_cluster_dict.items():
    for cluster in value:   
        if '*' not in cluster[0]:
            cluster_single_genename_list.append(cluster[0])
        elif '*' in cluster[0]:
            file_out_name = '_'.join(key.split() + [str(cluster[1][0]), str(cluster[1][1])] + ['genename.txt'])
            #fo = open(path+"/"+file_out_name, "w")
            cluster_gene_exon_list = []
            for genename_num in cluster[0].split('*'):                       
                cluster_gene_exon_list = cluster_gene_exon_list + gene_exons_dict[genename_num]
                all_cluster_genename_list.append(genename_num)
                #fo.write(genename_num + '\n')
            #fo.close()

            end_index = sorted(cluster_gene_exon_list)[0][1] 
            start_index = sorted(cluster_gene_exon_list)[0][0] 
            tu = (start_index, end_index)
            exonnum = 1
            exon_dict = {}
            for (start, end) in sorted(cluster_gene_exon_list):
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
            print('\t'.join([key.split()[0], '.', 'transcript', str(cluster[1][0]), str(cluster[1][1]), '.', key.split()[1], '.', 'gene_id "{}"; transcript_id "{}";'.format(cluster[0],cluster[0])]))
            if key.split()[1] == '+':
                for exon_num,location in exon_dict.items():
                    print('\t'.join([key.split()[0], '.', 'exon', str(location[0]), str(location[1]), '.', key.split()[1], '.', 'gene_id "{}"; transcript_id "{}"; exon_number "{}";'.format(cluster[0],cluster[0],exon_num)]))
            else:
                exon_list = sorted(exon_dict.items(),key=lambda  item:item[1])
                for exon_num,location in reversed(exon_list):
                    print('\t'.join([key.split()[0], '.', 'exon', str(location[0]), str(location[1]), '.', key.split()[1], '.', 'gene_id "{}"; transcript_id "{}"; exon_number "{}";'.format(cluster[0],cluster[0],exon_num)]))

for genenum in cluster_single_genename_list:
    for line in genename_line[genenum]:
        print(line.strip('\n'))

#fo2 = open(sys.argv[2] + '/' + '_'.join(sys.argv[1].split('/')[-1].split('_')[:2]) + '_cluster_genename.txt', "w")
#fo2.write('\t'.join(all_cluster_genename_list))
#fo3 = open(sys.argv[2] + '/' + '_'.join(sys.argv[1].split('/')[-1].split('_')[:2]) + '_cluster_single_genename.txt', "w")
#fo3.write('\t'.join(cluster_single_genename_list))
    
#fo2.close()
#fo3.close()
