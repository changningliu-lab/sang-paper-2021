#shuru:fasta
import sys
from collections import defaultdict

file_out = open('25_species_lnc_length.txt', 'a+')
infoDict = {}
with open(sys.argv[1]) as length:
    for line in length:
            line = line.strip()
            if line[0] == '>':
                lncname = line.split(' ')[0][1:]
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
    file_out.write('\t'.join([name, str(lengths)]) + '\n')
 
length.close()
file_out.close()