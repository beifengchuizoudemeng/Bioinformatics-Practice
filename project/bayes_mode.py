from math import log
#计算先验概率
def cal_priorProbability(donors) :

    priors = []
    count = []

    for i in range(9):
        priors.append([0,0,0,0])#acgt
        count.append([0,0,0,0])

    for donor in donors:
        for j in range(len(donor)):
            if donor[j] == "a":
                count[j][0] += 1
            elif donor[j] == "c":
                count[j][1] += 1
            elif donor[j] == "g":
                count[j][2] += 1
            else:
                count[j][3] += 1

    for i in range(len(priors)):
        for j in range(4):
            priors[i][j] = count[i][j]/len(donors)


    return priors


#计算联合概率
def cal_jointProbability(donors):
    joints = []
    count = []
    N,M=8,16
    joints = [[1 for p in range(M)] for q in range(N)]
    count = joints
    for donor in donors:
        for j in range(8):
            if donor[j:j+2] == 'aa':
                count[j][0] += 1

            elif donor[j:j+2] == 'ac':
                count[j][1] += 1

            elif donor[j:j+2] == 'ag':
                count[j][2] += 1

            elif donor[j:j+2] == 'at':
                count[j][3] += 1

            elif donor[j:j+2] == 'ca':
                count[j][4] += 1

            elif donor[j:j+2] == 'cc':
                count[j][5] += 1

            elif donor[j:j+2] == 'cg':
                count[j][6] += 1

            elif donor[j:j+2] == 'ct':
                count[j][7] += 1

            elif donor[j:j+2] == 'ga':
                count[j][8] += 1

            elif donor[j:j+2] == 'gc':
                count[j][9] += 1

            elif donor[j:j+2] == 'gg':
                count[j][10] += 1

            elif donor[j:j+2] == 'gt':
                count[j][11] += 1

            elif donor[j:j+2] == 'ta':
                count[j][12] += 1

            elif donor[j:j+2] == 'tc':
                count[j][13] += 1

            elif donor[j:j+2] == 'tg':
                count[j][14] += 1

            else:
                count[j][15] += 1


    #print(len(donors))
    #print(count)

    for i in range(len(joints)):
        for j in range(16):
            joints[i][j] = count[i][j]/(len(donors)+16)

    return joints


#计算条件概率
# Pi(A,C) 第i-1位是C，第i位为A的概率
def cal_conditionalProbability(priors, joints):

    conditionals = joints
    for i in range(8):
        for j in range(4):
            for m in range(4):
                conditionals[i][4*j+m] = joints[i][4*j+m]/priors[i][j]
    return conditionals


def cal_WAM(seq, priorA, priorB, conditionalsA, conditionalsB):
    seq = seq.replace('a','0')
    seq = seq.replace('c','1')
    seq = seq.replace('g','2')
    seq = seq.replace('t','3')
    #seq = seq.replace('A','0')
    #seq = seq.replace('C','1')
    #seq = seq.replace('G','2')
    #seq = seq.replace('T','3')

    S = log(priorA[int(seq[0])]) - log(priorB[int(seq[0])])
    for i in range(8):
        temp = log(conditionalsA[i][int(seq[i])*4+int(seq[i+1])]) - log(conditionalsB[i][int(seq[i])*4+int(seq[i+1])])
        S += temp

    return S

def cal_WAM2(seq, priorA, priorB, jointsA, jointsB):
    seq = seq.replace('a','0')
    seq = seq.replace('c','1')
    seq = seq.replace('g','2')
    seq = seq.replace('t','3')
    #seq = seq.replace('A','0')
    #seq = seq.replace('C','1')
    #seq = seq.replace('G','2')
    #seq = seq.replace('T','3')

    S = log(priorA[int(seq[0])]) - log(priorB[int(seq[0])])
    for i in range(8):
        temp = log(jointsA[i][int(seq[i])*4+int(seq[i+1])]) - log(jointsB[i][int(seq[i])*4+int(seq[i+1])])
        S += temp

    return S
