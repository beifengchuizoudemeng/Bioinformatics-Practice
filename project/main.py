import assistant_mode
import bayes_mode
import random
import numpy as np
import matplotlib.pyplot as plt
import SVM_mode



#数据预处理阶段
Train_Path = "" #相应训练集路径
Test_Path = ""  #相应测试集路径

##解析文件，获取donor的位置信息以及相关DNA序列
DNA_lens = []
CDSjoins = []
seqs_DNA = []
seqs_name = []

DNA_lens2 = []
CDSjoins2 = []
seqs_DNA2 = []
seqs_name2 = []

DNA_lens, CDSjoins, seqs_DNA, seqs_name = assistant_mode.load_allfile(Train_Path)
DNA_lens2, CDSjoins2, seqs_DNA2, seqs_name2 = assistant_mode.load_allfile(Test_Path)


donor_locations = []
acceptor_locations = []

donor_locations2 = []
acceptor_locations2 = []

donor_locations, acceptor_locations = assistant_mode.process_CDSjoin(CDSjoins)
donor_locations2, acceptor_locations2 = assistant_mode.process_CDSjoin(CDSjoins2)


##提取donor片段并保存到相应文件
donors = []
donors2 = []

donors = assistant_mode.get_donor(seqs_DNA,donor_locations)
donors2 = assistant_mode.get_donor(seqs_DNA2,donor_locations2)

donors_filename = "Train_donors.txt"
donors_filename2 = "Test_donors.txt"
assistant_mode.save_donors(donors, donors_filename)
assistant_mode.save_donors(donors2, donors_filename2)


##生成假的donor片段用于训练模型并保存相应文件
phonyDonors = []
phonyDonors2 = []

phonyDonors = assistant_mode.create_phonyDonor(seqs_DNA, donor_locations, acceptor_locations)
phonyDonors = random.sample(phonyDonors, len(donors))
phonyDonors2 = assistant_mode.create_phonyDonor(seqs_DNA2, donor_locations2, acceptor_locations2)
phonyDonors2 = random.sample(phonyDonors2, len(donors2))
phonyDonors_filename = "Train_phonyDonors.txt"
phonyDonors_filename2 = "Test_phonyDonors.txt"
assistant_mode.save_donors(phonyDonors, phonyDonors_filename)
assistant_mode.save_donors(phonyDonors, phonyDonors_filename2)



#导入数据
donors = assistant_mode.read_donors("Train_donors.txt")
donors2 = assistant_mode.read_donors("Test_donors.txt")
phonyDonors = assistant_mode.read_donors("Train_phonyDonors.txt")
phonyDonors2 = assistant_mode.read_donors("Test_phonyDonors.txt")




#SVM mode
Train_donors = []
Train_labels = []
Test_donors1 = []
Test_labels1 = []
Test_donors2 = []
Test_labels2 = []
##数据规范化，主要是把acgt转换成数字坐标0123，并给数据添加标签，正例为1，反例为0，用于SVM模型的训练
Temp_donors, Temp_labels = assistant_mode.process_donors(donors,'T')
Train_donors.extend(Temp_donors)
Train_labels.extend(Temp_labels)
Temp_donors, Temp_labels = assistant_mode.process_donors(phonyDonors,'F')
Train_donors.extend(Temp_donors)
Train_labels.extend(Temp_labels)

Temp_donors, Temp_labels = assistant_mode.process_donors(donors2,'T')
Test_donors1.extend(Temp_donors)
Test_labels1.extend(Temp_labels)
Temp_donors, Temp_labels = assistant_mode.process_donors(phonyDonors2,'F')
Test_donors2.extend(Temp_donors)
Test_labels2.extend(Temp_labels)

SVM_mode.classifyBySVM(Train_donors, Train_labels, Test_donors1, Test_labels1, Test_donors2, Test_labels2)




#bayes mode
##计算先验概率
priorsA = []
priorsB = []

priorsA = bayes_mode.cal_priorProbability(donors)
priorsB = bayes_mode.cal_priorProbability(phonyDonors)


##计算联合概率
jointsA = []
jointsB = []

jointsA = bayes_mode.cal_jointProbability(donors)
jointsB = bayes_mode.cal_jointProbability(phonyDonors)


##计算条件概率
conditionalsA = []
conditionalsB = []

conditionalsA = bayes_mode.cal_conditionalProbability(priorsA, jointsA)
conditionalsB = bayes_mode.cal_conditionalProbability(priorsB, jointsB)


##选择合适的阈值
Ts = list(np.arange(-15,15,0.1))#阈值
Ps = []
Rs = []
SNs = []
SPs = []

for T in Ts:
    TP = 1
    TN = 1
    FP = 1
    FN = 1
    for donor2 in donors2:

        if bayes_mode.cal_WAM(donor2,priorsA[0],priorsB[0],conditionalsA,conditionalsB)>T:
            TP += 1#真正例
        else:
            FN += 1#假反例

    for phonyDonor2 in phonyDonors2:

        if bayes_mode.cal_WAM(phonyDonor2,priorsA[0],priorsB[0],conditionalsA,conditionalsB)>T:
            FP += 1 #假正例
        else:
            TN += 1 #真反例


    P = TP/(TP + FP)#查准率
    R = TP/(TP + FN)#查全率
    SN = TP/(TP + FN)
    SP = TN/(TN + FP)
    Ps.append(P)
    Rs.append(R)
    SNs.append(SN)
    SPs.append(SP)

plt.plot(Ts, SNs, c = 'r')
plt.plot(Ts, SPs, c = 'g')
plt.show()
