from Bio import SeqIO
import numpy as np
import pandas as pd

record = list(SeqIO.parse("/Users/snehalilawe/Desktop/Rosalind_BioInformatics/rosalind_lcsm.txt", "fasta"))

df = pd.DataFrame(record)
df = pd.Series(df.fillna('').values.tolist()).str.join('')
final = pd.DataFrame()
max = 0

record_0_len = len(record[0].seq)
record_0_str = str(record[0].seq)
record_len = len(record)

for i in np.arange(0,record_0_len):
#     print(f'i: {i}')
    for j in np.flip(np.arange(i+1,record_0_len)):
        # print(f'Comparing: {i} to {j}')
        tmp = df.str.contains(record_0_str[i:j])
        col_name = f'col_{i}_{j}'
        final[col_name] = tmp
        if tmp.sum() == record_len and len(record_0_str[i:j]) > max:
            max = len(record_0_str[i:j])
            print(f'Str: {i} to {j}: {record_0_str[i:j]}')
            break
        
# =============================================================================
# TODO: 
#     1. replace for loop
#     2. do summation of T/F after computation is complete
#     3. Find column with longest name and max summation
# =============================================================================
"""         
def lcs(X, Y):
        tmp = np.zeros((len(X)+1)*(len(Y)+1)).reshape(len(X)+1,len(Y)+1)
        # print(tmp)

        maxLength = 0
        endingIndex = len(X)+1

        for i in np.arange(0, len(X)+1):
                for j in np.arange(0, len(Y)+1):
                        if i == 0 or j == 0:
                                tmp[i,j] = 0
                        elif X[i-1] == Y[j-1]:
                                tmp[i,j] = tmp[i-1,j-1] + 1
                                if tmp[i,j] > maxLength:
                                        maxLength = int(tmp[i,j])
                                        endingIndex = i
                        else:
                                tmp[i,j] = 0
        
        return X[endingIndex - maxLength: endingIndex]

Y = 'ABCXYZAY'
X = 'XYZABCB'
Z = 'AXYZABC'
  
lcs(X, Y) """



# =============================================================================
# string = str(record[0].seq[i:j])
#         print(f'Checking if {string} matches')
#         #print(str(record[0].seq[i:j]))
#         if(str(record[0].seq[i:j]) in str(record[1].seq)):
#             print("*********")
#             print(str(record[1].seq))
#             print("*********")
# =============================================================================
