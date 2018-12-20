import os
import re
import random

def load_allfile(path) :

    files= os.listdir(path) #得到文件夹下的所有文件名称的列表

    DNA_lens = []
    CDSjoins = []
    seqs_DNA = []
    seqs_name = []

    for file in files: #遍历文件夹

         if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
              seq_name = file.strip('.txt')
              f = open(path+"/"+file); #打开文件
              a = f.readlines()
              CDSjoin = a[1].strip('\n')
              seq_DNA = ""
              for line in range(2, len(a)):
                  seq_DNA += a[line].strip('\n')

              seq_len = len(seq_DNA)

              DNA_lens.append(seq_len)
              CDSjoins.append(CDSjoin)
              seqs_DNA.append(seq_DNA)
              seqs_name.append(seq_name)
              f.close()
    print('load files successful!')
    return DNA_lens, CDSjoins, seqs_DNA, seqs_name

#处理CDSjoin信息，从而得到donor的位置
def process_CDSjoin(CDSjoins) :

     donor_locations = []
     acceptor_locations = []
     count =0
     for CDSjoin in CDSjoins:

         donor_location = []
         acceptor_location = []
         a = len(CDSjoin)
         nPos = CDSjoin.find('(')
         donor_temp = re.split(',|\.\.', CDSjoin[nPos+1:a-1])#分割字符从而得到donor的位置和acceptor的位置

         for i in range(int(len(donor_temp)/2)):
             donor_location.append(int(donor_temp[2*i+1]))
             acceptor_location.append(int(donor_temp[2*i]))
         donor_locations.append(donor_location)
         acceptor_locations.append(acceptor_location)
         count += 1
     return donor_locations, acceptor_locations

#根据donor的位置和序列，从而提取donor片段
def get_donor(seqs_DNA, donor_locations) :

    donors = []

    for i in range(len(seqs_DNA)):
        for j in range(len(donor_locations[i])):
            index = donor_locations[i][j]
            if index+5 <= len(seqs_DNA[i]):
                donors.append(seqs_DNA[i][index-4:index+5])

    return donors


#donor片段存储起来
def save_donors(donors, filename) :

    f = open(filename,'w+')
    for donor in donors:
        donor = donor.lower()
        f.write(donor + '\n')
    f.close()
    print('save donors successful!')


def save_P(Ps, filename) :
    f = open(filename,'w+')
    for P1 in Ps:
        for P2 in P1:
            f.write(str(P2)+'\n')
        f.write('************'+'\n')
    f.close()


def read_donors(filename) :
    donors = []
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        donors.append(line.strip('\n'))
    f.close()
    print('read donors successful!')
    return donors


#生成假donor片段
def create_phonyDonor(seqs_DNA, donor_locations, acceptor_locations) :

    phonyDonors = []

    for i in range(len(seqs_DNA)):
        seq_DNA = seqs_DNA[i]
        length = len(donor_locations[i])#寻找相应数量的假位点
        phonyDonor_temp = []
        for j in range(length):
            index1 = acceptor_locations[i][j]
            index2 = donor_locations[i][j]
            if j == 0:
                #m = 0
                m = random.randint(0, index1-13) if index1-13 > 0 else 0
                n = m + 3
                while m+9 <= index1 - 4 :
                    phonyDonor = seq_DNA[m:m + 9]
                    if ('n' not in phonyDonor) and ('s' not in phonyDonor) and ('N' not in phonyDonor) and ('S' not in phonyDonor):
                        phonyDonor_temp.append(phonyDonor)
                    m += 1
                    if m >= n:
                        break
                #m = index1 + 5
                m = random.randint(index1+5, index2-13) if index2-13 > index1+5 else index1+5
                n = m + 3
                while m+9 <= index2 - 4 :
                    phonyDonor = seq_DNA[m:m + 9]
                    if ('n' not in phonyDonor) and ('s' not in phonyDonor) and ('N' not in phonyDonor) and ('S' not in phonyDonor):
                        phonyDonor_temp.append(phonyDonor)
                    m += 1
                    if m > n:
                        break
            else:
                #m = donor_locations[i][j-1] + 5
                m = random.randint(donor_locations[i][j-1]+5, index1-13)  if index1-13 >  donor_locations[i][j-1]+5 else donor_locations[i][j-1]+5
                n = m + 3
                while m+9 <= index1 - 4 :
                    phonyDonor = seq_DNA[m:m + 9]
                    if ('n' not in phonyDonor) and ('s' not in phonyDonor) and ('N' not in phonyDonor) and ('S' not in phonyDonor):
                        phonyDonor_temp.append(phonyDonor)
                    m += 1
                    if m >= n:
                        break
                #m = index1 + 5
                m = random.randint(index1+5, index2-13) if index2-13 > index1+5 else index1+5
                n = m + 3
                while m+9 <= index2 - 4 :
                    phonyDonor = seq_DNA[m:m + 9]
                    if ('n' not in phonyDonor) and ('s' not in phonyDonor) and ('N' not in phonyDonor) and ('S' not in phonyDonor):
                        phonyDonor_temp.append(phonyDonor)
                    m += 1
                    if m >= n:
                        break

        slice = random.sample(phonyDonor_temp, length)
        phonyDonors.extend(slice)
    print('create phonyDonors successful!')
    return phonyDonors

def process_donors(donors,str):
    labels = []
    newdonors = []
    for seq in donors:
        temp = []
        seq = seq.replace('a','0')
        seq = seq.replace('c','1')
        seq = seq.replace('g','2')
        seq = seq.replace('t','3')
        #seq = seq.replace('A','0')
        #seq = seq.replace('C','1')
        #seq = seq.replace('G','2')
        #seq = seq.replace('T','3')

        for i in range(len(seq)):
            temp.append(int(seq[i]))
        newdonors.append(temp)
        if str == 'T':
            labels.append(1)
        else:
            labels.append(0)
    return newdonors,labels
