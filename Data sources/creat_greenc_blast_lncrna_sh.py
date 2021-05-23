# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 10:58:37 2018

@author: chenw
"""

import os

cmd_temp = '''makeblastdb -in plant_lncrna_fa/{0}.fasta -dbtype nucl -out blast_db/{0}_lncrna
blastn -query lncrna_15+5.fa -out blast_result/{0}_lncrna.blast -db blast_db/{0}_lncrna -evalue 1e-5 -num_threads 8 -outfmt 6 -word_size 11
echo '{0}' >> GREENC_lncrna_out.blast
grep -c '>' plant_lncrna_fa/{0}.fasta >> GREENC_lncrna_out.blast
cut -f1 blast_result/{0}_lncrna.blast |sort |uniq -c |wc -l >> GREENC_lncrna_out.blast
cut -f2 blast_result/{0}_lncrna.blast |sort |uniq -c |wc -l >> GREENC_lncrna_out.blast
echo >> GREENC_lncrna_out.blast\n'''


sh = open("blast.sh", 'w')
sh.write("#! /bin/bash\n")
work_dir = os.getcwd()
for root, dirs, files in os.walk(work_dir):
     for f in files:
         f_dir=root+f
         if 'work2/plant_lncrna_fa' in f_dir:
             cmd = cmd_temp.format(f.split('.')[0])
             sh.write(cmd)

sh.close()
             

