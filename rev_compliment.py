filename = "/Users/snehalilawe/Desktop/Rosalind_BioInformatics/rosalind_revc.txt"
data = open(filename,'r').read();
data = data.strip("\n")

#reverse compliment
complement_dict = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}

comp_seq = (''.join([str(complement_dict.get(base)) for base in data]))[::-1]

print(comp_seq)