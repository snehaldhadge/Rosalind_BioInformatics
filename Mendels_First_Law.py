filename = "/Users/snehalilawe/Desktop/Rosalind_BioInformatics/rosalind_iprb.txt"
data = open(filename,'r').read()
k,m,n = map(int,data.split(" "))
total_pop = k+m+n
total_probability = ((k ** 2 - k) + (2 * k * m) + (3 / 4 * (m ** 2 - m)) + (2* k * n) + (m * n)) / (total_pop ** 2 - total_pop)
print(total_probability)