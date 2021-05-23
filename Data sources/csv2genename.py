import sys
import os 

path=os.getcwd()
if not os.path.exists(path):
    os.makedirs(path)

csv_file_in = open(sys.argv[1],'r')
txt_file_out = open(path + '/' + 'plant_lncrna_txt' + '/' + sys.argv[1].split('/')[1].split('.')[0] + '.txt', 'a+')
for line in csv_file_in:
    if line[0] != ',':
        info = line.strip().split('",')
        column1 = '_'.join(info[0].strip('"').split(':')[1].split(' '))  
        txt_file_out.write(column1 + '\n')
csv_file_in.close()
txt_file_out.close()