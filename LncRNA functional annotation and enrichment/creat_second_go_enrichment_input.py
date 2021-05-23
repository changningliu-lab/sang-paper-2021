#input:1477lnc2GO_text_format_slim_fulllist_p0.01.txt/1477lnc2GO_text_format_slim_fulllist_p0.05.txt等类似文件
#output:lnc2go_second_go_enrichment_input_slim_fulllist_p0.01.txt 类似这样形式的文件名
import sys
file_in = open(sys.argv[1], 'r')
file_out = open('lnc2go_second_go_enrichment_input_' + '_'.join(sys.argv[1].split('_')[3:]), 'w')

for line in file_in:
    item = line.split('\t')
    if item[-1] != '\n':
        file_out.write(line)

file_in.close()
file_out.close()