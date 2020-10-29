from Bio import SeqIO
import pandas as pd
import numpy as np
from collections import defaultdict

data = []
for line in SeqIO.parse("/Users/snehalilawe/Desktop/Rosalind_BioInformatics/rosalind_cons.txt", "fasta"):
    data.append(list(line.seq))

counter = []
consensus=[]
full_seq = ""

for i in range(0,len(data[0])):
    counter.append(defaultdict(int))
    for seq in data:
        counter[i][seq[i]] += 1
    print(counter[i])
    consensus += max(counter[i], key=counter[i].get)
    
print(full_seq.join(consensus))
    
