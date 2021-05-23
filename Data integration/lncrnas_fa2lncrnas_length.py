#input:plant_pseudo_and_normal_lncrnas_fa80/*fasta
#output:>> /home/sangye/lncRNA_evolution/data_analysis/lnc_classify/plant_pseudo_and_normal_lncrnas_fa80_lnc_length.txt
import re
import sys
from collections import defaultdict

infoDict = {}
with open(sys.argv[1]) as length:
    for line in length:
        line = line.strip()
        if line[0] == '>':
            lncname = line[1:]
            infoDict[lncname] = []
        else:
            infoDict[lncname].append(line)
lengthDict = {}
for key,value in infoDict.items():
    lnclength = len(''.join(value))
    if key[0:4] == 'lcl|':
        lengthDict[key[4:]] = int(lnclength)
    else:
        lengthDict[key] = int(lnclength)
for name,lengths in lengthDict.items():
    print('\t'.join([name, str(lengths)]))
