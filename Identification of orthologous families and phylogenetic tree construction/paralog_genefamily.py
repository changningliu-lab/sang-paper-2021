#参数1：plant_pseudo_and_normal_lncrnas_fa_AA_blast_result/*.blast
#参数2：plant_each_species_lncrnas_num.txt
#输出：sh中的>>之后的文件名
import sys

network = []
with open(sys.argv[1],'r') as f:
    for line in f:
        info = line.strip().split()
        gene1 = info[0]
        gene2 = info[1]
        gene_pair = {gene1, gene2}
        if (gene1 != gene2) and (gene_pair not in network):
            network.append(gene_pair)
            
net_dict = dict()
for a,b in network:
    net_dict.setdefault(a, {})
    net_dict.setdefault(b, {})
    net_dict[a][b] = net_dict[b][a] = 0

    
nodes_dict = dict()

for node, links in net_dict.items():
    nodes_dict[node]=len(links.keys())

cluster = []
sorted_nodes_dict = sorted(nodes_dict.items(),key=lambda x:x[1], reverse=True)
nodes = [x[0] for x in sorted_nodes_dict]

num = 0

while(nodes):
    num += 1
    top_node = nodes[0]
    childs = list(net_dict[top_node].keys())
    fathers = set()
    fathers.add(top_node)
    while(childs):
        new_childs = childs
        for i in childs:
            #print('.',end='')
            fathers.add(i)
            if nodes_dict[i]-1 == 0:
                new_childs.remove(i)
            else:
                new_childs.remove(i)
                childs_childs = set(net_dict[i].keys()) - fathers
                new_childs = set(new_childs) | childs_childs
        childs = list(new_childs)
    cluster.append(fathers)
    #print('cluster {}'.format(num), fathers)
    for i in fathers:
        nodes.remove(i)

lncrna_num = {}
with open(sys.argv[2],'r') as f:
    for line in f:
        info = line.split()
        num = int(info[1])
        key = info[0]
        lncrna_num[key] = num
family_ave_lncrna = lncrna_num[sys.argv[1].split('/')[1].split('2')[0]]/len(cluster)

print('{} have {} genefamilys, family_ave_lncrna is {}'.format(sys.argv[1].split('.')[0].split('/')[1], len(cluster),str('%.2f'%family_ave_lncrna)))
