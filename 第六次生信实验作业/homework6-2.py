#创建随机序列的FASTA文件
import random
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

strList = ['A','G','C','T']
seqRecords = []

for m in range(500):
    len = random.randrange(4000, 15000+1)
    #print(len)
    seqGene = ''
    for i in range(len):
        tempSeq = random.choice(strList)
        seqGene = seqGene + tempSeq
    #print(seqGene)
    simple_seq = Seq(seqGene)
    num = "AC" + str(m)
    simple_seq_r = SeqRecord(simple_seq,id=num)
    simple_seq_r.description = "len = "+str(len)
    seqRecords.append(simple_seq_r)

SeqIO.write(seqRecords, "result2.fas", "fasta")
