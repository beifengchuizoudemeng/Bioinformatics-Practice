#从 FASTA文件中过滤空序列
from Bio import SeqIO
records = (rec for rec in SeqIO.parse("out22.fas", "fasta") if len(rec) > 0)
SeqIO.write(records, "result1.fas", "fasta")
