import pandas as pd
from Bio import SeqIO

data = list(SeqIO.parse("/Users/snehalilawe/Desktop/Rosalind_BioInformatics/rosalind_grph.txt","fasta"))
pairs = []
for i in range(len(data)):
    for j in range(len(data)):
        if(i == j):
            continue
        else:
            if (data[i].seq[-3:] in data[j].seq[0:3]):
                   pairs.append([data[i].id,data[j].id])
                  

for p in pairs:
    print(p[0]+" "+p[1])


    