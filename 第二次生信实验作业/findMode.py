import re
pattern = re.compile(r'[AILVFPMW]K.[DE]')
inFile = open('Q96GD4.fasta.txt', 'r')
a = inFile.readlines()
seq = ''
for line in range(2,len(a)):
       seq += a[line].strip('\n')
inFile.close()

print(pattern.findall(seq))
outFile = open(r'test.txt', 'w', encoding='utf-8')
i = 1
searchObj = pattern.search(seq)

while searchObj:
    print(searchObj)
    pos = searchObj.span()
    outFile.write('PIK%d %d-%d %s\n'%(i,pos[0],pos[1],searchObj.group()))
    searchObj = pattern.search(seq, pos[1])
    i += 1

outFile.close()
