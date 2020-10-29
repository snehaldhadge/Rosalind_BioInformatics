
data = open("/Users/snehalilawe/Desktop/Rosalind_BioInformatics/rosalind_gc.txt",'r')

GC_content = dict()
inp_data = dict()
for line in data:
    if(line[0]=='>'):
        key = line.strip('>')
        inp_data[key]=""
    else:
        inp_data[key]+=line
        
for key,seq in inp_data.items():
        GC_content[key] = 100 * ((seq.count('G')+seq.count('C'))/float(seq.count('G')+seq.count('C')+seq.count('A')+seq.count('T'))) 

print(max(GC_content, key=GC_content.get))   
print(GC_content[max(GC_content, key=GC_content.get)])


