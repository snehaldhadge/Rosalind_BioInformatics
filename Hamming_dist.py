def get_hamming_dist(seq1,seq2):
    seq1 = seq1.strip('\n')
    return(sum(1 for a,b in zip(seq1,seq2) if a!=b ))

data = open('/Users/snehalilawe/Desktop/Rosalind_BioInformatics/rosalind_hamm.txt','r').readlines()
print(get_hamming_dist(data[0],data[1]))



