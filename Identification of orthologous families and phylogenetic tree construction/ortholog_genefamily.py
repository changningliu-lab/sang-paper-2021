# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 19:17:26 2018

@author: chenw
"""
#注意！必须在plant_pseudo_and_normal_lncrnas_fa_best_match_blast_uniq_result/下跑
#参数无
#输出：plant_ortholog_genefamily_redundancy.txt和plant_ortholog_genefamily_rm_redundancy.txt

import os
from collections import defaultdict
import sys
sys.setrecursionlimit(10000000)

AB = []
work_dir = os.getcwd()
for root, dirs, files in os.walk(work_dir):
    for f1 in files:
        for f2 in files:
            if (f1.split('2')[0] == f2.split('2')[1].split('.')[0]) and (f2.split('2')[0] == f1.split('2')[1].split('.')[0]): 
                A_to_B = []
                B_to_A = []
                with open (f1,'r') as f:
                    for line in f:
                        info = line.split()
                        lncRNA_pair_st = set((f1.split('2')[0] + '#'+ info[1], f1.split('2')[1].split('.')[0] + '#'+ info[2])) 
                        A_to_B.append(lncRNA_pair_st)

                with open (f2,'r') as f:
                    for line in f:
                        info = line.split()
                        lncRNA_pair_st = set((f2.split('2')[0] + '#'+ info[1], f2.split('2')[1].split('.')[0] + '#'+ info[2])) 
                        B_to_A.append(lncRNA_pair_st)
                        
                for lncRNA_pair in A_to_B:
                    if lncRNA_pair in B_to_A:
                        AB.append(lncRNA_pair)

path = '/home/sangye/lncRNA_evolution/merge_database_and_define_parologs_orthologs/merge_database_step4_merge_location_step5_define_parologs_orthologs/plant_merge_location_and_define_parologs_orthologs/'
output_file_name = path + "plant_ortholog_genefamily_rm_redundancy.txt"
output_file_name2 = path + "plant_ortholog_genefamily_redundancy.txt"
output_file = open(output_file_name, 'w')
output_file2 = open(output_file_name2, 'w')

node_state = dict()
network = dict()
for nodeA,nodeB in AB:
    if nodeA == nodeB:
        continue
    node_state[nodeA] = 0
    node_state[nodeB] = 0    
    if nodeA in network:
        network[nodeA].add(nodeB)
    else:
        network[nodeA] = set()
        network[nodeA].add(nodeB)
    if nodeB in network:
        network[nodeB].add(nodeA)
    else:
        network[nodeB] = set()
        network[nodeB].add(nodeA)

# 定义深度优先搜索函数，一般是一个递归函数
def dfs(node, node_state, network):
    module = set()
    if (node_state[node] == 0): # 如果没有被访问过，则递归访问
        module.update(network[node])
        node_state[node] = 1 # 标记为访问过
        for neighbor in network[node]:
            module.update(dfs(neighbor, node_state, network))
    return module

cluster_dict = defaultdict(list)
for node in node_state:
    if (node_state[node] == 0):
        module = dfs(node, node_state, network)
        module_new = []
        output_file2.write(str(len(module)) + ';')
        for node_ in module:          
            output_file2.write(node_ + ';')
            node_new = node_.split('#')[0]
            if node_new not in module_new:
                module_new.append(node_new)
        output_file2.write('\n')
        length = len(module_new)    
        cluster_dict[length].append(module_new)     

cluster_list = sorted(cluster_dict.items(),key=lambda  item:item[0])
for num,value in cluster_list: 
    for cluster in value:
        output_file.write(';'.join([str(num)]+cluster))
        output_file.write('\n')   
 
output_file.close()
output_file2.close()
