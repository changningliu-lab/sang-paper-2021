#输入：plant_lncrna_csv/*.csv  输出：plant_lncrna_txt/*.txt  注意：其中有一些txt中物种gene的名字和对应的fasta文件不相同，用shell命令做调整，让txt的gene名和fasta的gene名对应
import sys
import os 

path=os.getcwd()
if not os.path.exists(path):
    os.makedirs(path)

csv_file_in = open(sys.argv[1],'r')
txt_file_out = open(path + '/' + 'plant_lncrna_txt' + '/' + sys.argv[1].split('/')[1].split('.')[0] + '.txt', 'a+')
for line in csv_file_in:
    if line[0] != ',':
        info = line.strip().split(',')
        column1 = '_'.join(info[0].split('Gene:')[-1].split())[:-2]
        column2 = info[1]
        column3 = info[2]
        column4 = info[3]
        txt_file_out.write('\t'.join([column1, column2, column3, column4]) + '\n')
csv_file_in.close()
txt_file_out.close()