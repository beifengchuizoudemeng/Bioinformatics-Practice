def NWDistance(seedSequence, candidateSequence, match, n_match, gap):

    s = n_match  # a mismatch would deduce 2 point.
    m = match  # plus 4 point for one match.
    g = gap  # deduce 2 point for one gap.
    seedSequence = seedSequence.strip()
    candidateSequence = candidateSequence.strip()
    if len(seedSequence) == 0:
        print("Error, seed sequence length equal zero.")
        sys.exit(1)

    elif len(candidateSequence) == 0:
        print( "Error, candidate sequence length equal zero.")
        sys.exit(1)
#计算得分矩阵
    sLen = len(seedSequence)
    cLen = len(candidateSequence)
    table = []

    for i in range(0, len(seedSequence) + 1):
        table.append([i * g])

    table[0] = []

    for j in range(0, len(candidateSequence) + 1):
        table[0].append(j * g)

    for i in range(sLen):
        for j in range(cLen):
            #if seedSequence[i] == candidateSequence[j]:
            #    t1 = table[i][j] + m
            #else:
            #    t1 = table[i][j] + s
            #if t1 >= table[i + 1][j] + g and t1 >= table[i][j + 1] + g:
            #    table[i+1].append(t1)
            #    print("table[%d][%d] from table[%d][%d]"%(i+1,j+1,i,j))
            #    print(table[i+1][j+1])
            #else:
            #    if  table[i][j+1] +g >= table[i + 1][j]+g and t1 <= table[i][j + 1]+g:
            #        table[i+1].append(table[i][j+1]+g)
            #        print("table[%d][%d] from table[%d][%d]"%(i+1,j+1,i,j+1))
            #        print(table[i+1][j+1])
            #    else:
            #        table[i+1].append(table[i+1][j]+g)
            #        print("table[%d][%d] from table[%d][%d]"%(i+1,j+1,i+1,j))
            #        print(table[i+1][j+1])
            table[i + 1].append(
                max(table[i][j] + (m if seedSequence[i] == candidateSequence[j] else s),
                    table[i][j + 1] + g,
                    table[i + 1][j] + g)
                )
    #print(table)

#回溯寻找最优匹配
    i = sLen - 1
    j = cLen - 1

    NewSeed = seedSequence[i]
    NewCandidate = candidateSequence[j]

    if len(seedSequence) <= 1 or len(candidateSequence) <= 1:
        print( "Error, too short!")
        sys.exit(1)

    while True:

        if i == 0 and j == 0:
            break

        if seedSequence[i] == candidateSequence[j]:

            if table[i][j] + m > table[i][j + 1] + g and table[i][j] + m > table[i + 1][j] + g:
                i = i - 1
                j = j - 1
                NewSeed = u"%s%s" % (seedSequence[i], NewSeed)
                NewCandidate = u"%s%s" % (candidateSequence[j], NewCandidate)

            else:

                if table[i][j + 1] > table[i + 1][j]:
                    i = i - 1
                    NewSeed = u"%s%s" % (seedSequence[i], NewSeed)
                    NewCandidate = u"%s%s" % ('-', NewCandidate)

                else:
                    j = j - 1
                    NewSeed = u"%s%s" % ('-', NewSeed)
                    NewCandidate = u"%s%s" % (candidateSequence[j], NewCandidate)

        else:

            if table[i][j] + s > table[i][j + 1] + g and table[i][j] + s > table[i + 1][j] + g:
                i = i - 1
                j = j - 1
                NewSeed = u"%s%s" % (seedSequence[i], NewSeed)
                NewCandidate = u"%s%s" % (candidateSequence[j], NewCandidate)

            else:

                if table[i][j + 1] > table[i + 1][j]:
                    i = i - 1
                    NewSeed = u"%s%s" % (seedSequence[i], NewSeed)
                    NewCandidate = u"%s%s" % ('-', NewCandidate)

                else:
                    j = j - 1
                    NewSeed = u"%s%s" % ('-', NewSeed)
                    NewCandidate = u"%s%s" % (candidateSequence[j], NewCandidate)

    print(NewSeed)
    print(NewCandidate)

    return table, NewSeed, NewCandidate

#计算匹配分数
def calScore(NewSeed, NewCandidate, match, n_match, gap):

    numOfGap = 0
    numOfMatch = 0
    numOfDismatch = 0
    for i in range(len(NewSeed)):
        if NewSeed[i] == "-" or NewCandidate[i] == "-":
            numOfGap += 1
        else:
            if NewSeed[i] == NewCandidate[i]:
                numOfMatch += 1
            else:
                numOfDismatch += 1
    score = match*numOfMatch + n_match*numOfDismatch + gap*numOfGap
    print(score)

    return score
