from Bio import SeqIO
import pandas as  pd

sequences = []
data = []
data = list(SeqIO.parse("/Users/snehalilawe/Desktop/Rosalind_BioInformatics/rosalind_lcsm.txt", "fasta"))

sequences = [str(s.seq) for s in data]

# Sort the sequences to get start with smalled string

sequences.sort(key=len)

start_seq = sequences[0]
rest_seq = sequences[1:]
fnd_m = ''
for i in range(len(start_seq)):
    for j in range(i,len(start_seq)):
        sub_str = start_seq[i:j+1]
        seq_fnd = False
        for seq in rest_seq:
            if sub_str in seq:
                seq_fnd = True
            else:
                seq_fnd = False
        if seq_fnd and len(sub_str) > len(fnd_m):
            fnd_m = sub_str
print(fnd_m)