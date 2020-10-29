filename = "/Users/snehalilawe/Desktop/rosalind_rna.txt"
data = open(filename,'r').read();
print(data.replace('T','U'))
print(data[::-1])