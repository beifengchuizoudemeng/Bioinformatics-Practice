#import NwByPython2
import NWbyPython
import xlwt

seedSequence = "AACGTACTCA"
candidateSequence = "TCGTACTCA"

n_match = -2  # a mismatch would deduce 2 point.
match = 4  # plus 4 point for one match.
gap = -2  # deduce 2 point for one gap.

tables, NewSeed, NewCandidate = NWbyPython.NWDistance(seedSequence, candidateSequence, match, n_match, gap)
NWbyPython.calScore(NewSeed, NewCandidate, match, n_match, gap)
book = xlwt.Workbook()#新建一个excel
sheet = book.add_sheet('case1_sheet')#添加一个sheet页

row = 0
for col in range(2, 2 + len(seedSequence)):
    sheet.write(row, col, seedSequence[col-2])

col = 0
for row in range(2, 2 + len(candidateSequence)):
    sheet.write(row, col, candidateSequence[row-2])

row = 1#控制行
for table in tables:
    col = 1#控制列
    for tab in table:#再循环里面list的值，每一列
        sheet.write(col, row, tab)
        col+=1
    row+=1
book.save('test.xls')#保存到当前目录下
#F = NwByPython2.CreateMark("CTGTATC","CTATAATCCC", match, n_match, gap)
#print(F)
#S1 = []
#S2 = []
#t1 = ""
#t2 = ""
#NwByPython2.traceback(" CTGTATC", " CTATAATCCC", match, n_match, gap, F, F.shape[0]-1, F.shape[1]-1, S1, S2, t1, t2)
#print(S1)
#print(S2)
