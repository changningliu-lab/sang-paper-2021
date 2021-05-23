#input:/home/sangye/lncRNA_evolution/data_analysis/lnc_genome_mapping/gffcompare_work_related_plant_merge_location_and_define_parologs_orthologs_work2_2_gffcompare_annotated_gtf_remain_oxiu_four_class_high_confident_lnc/class_code_statistics_txt/*txt
#output:/home/sangye/lncRNA_evolution/data_analysis/lnc_genome_mapping/gffcompare_work_related_plant_merge_location_and_define_parologs_orthologs_work2_2_gffcompare_annotated_gtf_remain_oxiu_four_class_high_confident_lnc/oxiu_percent_statistics.txt

import sys

percent = 0
with open(sys.argv[1], 'r') as file_in:
    for line in file_in:
        if line[0] in 'oxiu':
            item = line.strip().split('\t')
            if line[0] == 'u':
                u = item[-1]
            print('\t'.join([line[0], item[-1]]))
            percent = percent + float(item[-1])
u_percent = float(u)/percent
print('\t'.join(['u/oxiu', str('%.4f' % u_percent)]))
print('\t'.join([sys.argv[1],str('%.4f' % percent)]))
