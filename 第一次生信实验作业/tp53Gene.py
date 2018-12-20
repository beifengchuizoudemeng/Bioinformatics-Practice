def find_G(S):
	i = 0
	count = 0
	while (seq.find(S, i) != -1):
		i  = seq.find(S, i) + 1
		count += 1
		# print(i)

	return count


f = open('sequence.fasta','r')
a = f.readlines()
seq = ''
for line in range(1,len(a)):
       seq += a[line].strip('\n')
seq_len = len(seq)
print('sequence length:',seq_len)
print('TA:',find_G('TA'))
print('CG:',find_G('CG'))
print('CG rate:', (find_G('C') + find_G('G')) / seq_len)

