filename = "/Users/snehalilawe/Desktop/rosalind_dna.txt"
data = open(filename,'r').read();
for c in 'ACGT': print(data.count(c),end=" ")