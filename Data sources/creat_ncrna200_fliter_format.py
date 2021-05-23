#read me 
#读入ncbi的rna文件（-i），输出序列名称以NR或XR开头,以ncRNA或non-coding RNA或misc_RNA结尾的且长度>200的ncra文件（-o），
#并且按照输入参数（-l，-c），格式化fasta文件


import getopt, sys

usage = "format_fasta.py -i input.fa -o output.fa -l length_per_line(default:60) -c case(U(upper) or L(lower) defualt:not-change)"

#获得参数
opts, args = getopt.getopt(sys.argv[1:], "hi:o:l:c:")
fa_in_file_name = ""
fa_out_file_name = ""
length = 60
case = ''
for op, value in opts:
    if op == "-i":
        fa_in_file_name = value
    elif op == "-o":
        fa_out_file_name = value
    elif op == "-l":
        length = int(value)
    elif op == "-c":
        case = value
    elif op == "-h":
        print(usage)
        sys.exit()

#读入fasta
fa_Info = []
fa_Seq = []
fa_Num = -1
with open(fa_in_file_name, 'r') as fa_in_file:
    for line in fa_in_file:
        line = line.strip()
        if line[0] == '>':
            fa_Info.append(line)
            fa_Num = fa_Num + 1
            fa_Seq.append([])
        else:
            fa_Seq[fa_Num].append(line)

#处理大小写
for i in range(fa_Num + 1):
    fa_Seq[i] = ''.join(fa_Seq[i])
    if case == 'U':
        fa_Seq[i] = fa_Seq[i].upper()
    elif case == 'L':
        fa_Seq[i] = fa_Seq[i].lower()


#读出文件               
with open(fa_out_file_name, 'w') as fa_out_file:
    for i in range(len(fa_Info)):
        seq_line = ''.join(fa_Seq[i])
        info=fa_Info[i]
        if ('NR_' in info) or ('XR_' in info):
            if ('ncRNA' in info) or ('non-coding RNA' in info) or ('misc_RNA' in info) or ('lncRNA' in info):
                if (len(seq_line) > 200) and ('small nucleolar RNA' not in info) and ('small Cajal body-specific RNA' not in info):
                    fa_out_file.write(info+'\n')
                    while len(seq_line) > 60:
                        fa_out_file.write(seq_line[:60] + "\n")
                        seq_line = seq_line[60:]
                    else:
                        fa_out_file.write(seq_line + "\n")
