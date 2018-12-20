
class Test():
	"""docstring for test1"""
	def __init__(self):
		self.file = open('sequence.fasta', 'r')
		a = self.file.readlines()
		self.seq = ''
		for i in range(1,len(a)):
			self.seq += a[i].strip('\n')
		self.seq_len = len(self.seq)
		print('sequence length:',self.seq_len)


	def find_G(self, S):
		i = 0
		count = 0
		while (self.seq.find(S, i) != -1):
			i  = self.seq.find(S, i) + 1
			count += 1
			# print(i)

		return count

	def getlen(self):
		return self.seq_len



if __name__ == '__main__':
	test = Test()
	print('TA:', test.find_G('TA'))
	print('CG:', test.find_G('CG'))
	print('CG rate:', (test.find_G('C')+test.find_G('G'))/test.getlen())
