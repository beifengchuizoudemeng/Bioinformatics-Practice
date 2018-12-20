#提取选定的蛋白的上游序列
from Bio import SeqIO
from Bio import SeqFeature
seq_results = []
for seq_record in SeqIO.parse("MTtabacum.gbk", "genbank"):
    #print (seq_record.id)
    #seq_gb = seq_record.seq
    #print (len(seq_record))
    #print (len(seq_record.features))
    #print(seq_record.features)
    Gene_feature_records = list((fea for fea in seq_record.features if fea.type == 'gene'))
    #print(Gene_feature_records)
    #print(len(Gene_feature_records))

    final_gene_records = list(( fea for fea in Gene_feature_records \
                         if fea.qualifiers['gene'] == ['cox2'] or \
                            fea.qualifiers['gene'] == ['atp6'] or \
                            fea.qualifiers['gene'] == ['atp9'] or \
                            fea.qualifiers['gene'] == ['cob'] ))
    #print(final_gene_records)
    for fea in final_gene_records:
        location_start = fea.location.start
        seq_result = seq_record[location_start-1000:location_start]
        seq_result.description = fea.qualifiers['gene'][0] + ' Upstream sequence'
        seq_results.append(seq_result)
    SeqIO.write(seq_results, "result3.gbk", "genbank")
