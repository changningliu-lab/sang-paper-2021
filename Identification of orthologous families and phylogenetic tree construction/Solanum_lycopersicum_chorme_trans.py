#input:Solanum_lycopersicum-SL3.0_NC_genomic.gff
#output:Solanum_lycopersicum-SL3.0_CM_genomic.gff
import sys
chorme_dict1 = {'NC_015438.3':'CM001064.3', 'NC_015439.3':'CM001065.3', 'NC_015440.3':'CM001066.3', 'NC_015441.3':'CM001067.3', 'NC_015442.3':'CM001068.3', 'NC_015443.3':'CM001069.3', 'NC_015444.3':'CM001070.3', 'NC_015445.3':'CM001071.3', 'NC_015446.3':'CM001072.3', 'NC_015447.3':'CM001073.3', 'NC_015448.3':'CM001074.3','NC_015449.3':'CM001075.3', 'NC_035963.1':'NC_035963.1', 'NC_007898.3':'NC_007898.3'}  
#{'NW_020442482.1':'AEKE03000001.1','NW_020442483.1':'AEKE03000002.1','NW_020442484.1':'AEKE03000003.1',      'NW_020445413.1':'AEKE03002932.1'   'NW_020442887.1': 'AEKE03000406.1'     'NW_020445617.1':'AEKE03003136.1'}

chorme_NW1 = 20442482
chorme_AEKE1 = 3000001
chorme_dict2 = {}
for i in range(3136):
    chorme_NW = chorme_NW1 + i
    chorme_AEKE = chorme_AEKE1 + i
    chorme_dict2['NW_0' + str(chorme_NW) + '.1'] = 'AEKE0' + str(chorme_AEKE) + '.1'

def Merge(dict1, dict2): 
    res = {**dict1, **dict2} 
    return res 
      
chorme_dict3 = Merge(chorme_dict1, chorme_dict2) 

file_in = open(sys.argv[1], 'r')
file_out = open(sys.argv[2], 'w')
for line in file_in:
    if line[0] != '#':
        item = line.split('\t')
        chorme_NC = item[0]
        chorme_CM = chorme_dict3[chorme_NC]
        file_out.write('\t'.join([chorme_CM] + item[1:]))
