filename = "/Users/snehalilawe/Desktop/rosalind_rna.txt"
data = open(filename,'r').read()
# reverse string
data1 = data[::-1]

#reverse compliment
print(data1.replace('A','T').replace('C','G'))