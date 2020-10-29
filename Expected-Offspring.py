import pandas as pd 

data = open("/Users/snehalilawe/Desktop/Rosalind_BioInformatics/rosalind_iev.txt","r").read()

inp = [int(x) for x in data.split(" ")]

print((1*inp[0]*2)+(1*inp[1]*2)+(1*inp[2]*2)+(0.75*inp[3]*2)+(0.5*inp[4]*2))
