file_in1 = open('work5_EBI_succeed_sra2fq.sh', 'r')
file_in2 = open('work5_EBI_succeed_sra2fq.sh.completed', 'r')
file_out = open('work5_failed.sh', 'w')

list2 = []
for line in file_in2:
    list2.append(line)

list1 = []
list3 = [] 
for line in file_in1:
    if line not in list2:
        list3.append(line)
        file_out.write(line)
    else:
        list1.append(line)