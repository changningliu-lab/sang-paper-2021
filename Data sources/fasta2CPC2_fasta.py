#参数1：plant/animal_CPC2.txt  参数2：plant/animal.fatsa  输出：plant/animal_CPC2.fatsa 
import sys

file_out = open(sys.argv[3], 'w')

file_in1 = open(sys.argv[1], 'r')
genename_lable_dict = {}
for line in file_in1:
    if line[0] == '#':
        continue
    item = line.split()
    genename_lable_dict[item[0]] = item[-1]

file_in2 = open(sys.argv[2], 'r')
for line in file_in2:
    item = line.split()
    if line[0] == '>':
        genename = item[0][1:]
        lable = genename_lable_dict[genename]
        if lable == 'noncoding':
            flag = 1
            line = item[0] + '\n'
        elif lable == 'coding':
            flag = 0
    if flag == 1:
        file_out.write(line)

file_in1.close()
file_in2.close()
file_out.close()

        
