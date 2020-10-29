from Bio import SeqIO
from Bio.SeqUtils import GC

GC_content = dict()
for line in SeqIO.parse("/Users/snehalilawe/Desktop/Rosalind_BioInformatics/rosalind_gc.txt", "fasta"):
    GC_content[line.id] = GC(line.seq)

print(max(GC_content, key=GC_content.get))   
print(GC_content[max(GC_content, key=GC_content.get)])



