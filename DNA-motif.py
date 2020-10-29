import re
data = open('/Users/snehalilawe/Desktop/Rosalind_BioInformatics/rosalind_subs.txt','r').read()
data = data.strip("\n")
inp_string,substring = data.split("\n")

result = []
mlen = len(substring)
print(mlen)
print(inp_string)
slen = len(inp_string)
for i in range(0, slen - mlen + 1):
        if inp_string[i:i+mlen] == substring:
            result.append(i+1) 
print(result)
#a = [m.start()+1 for m in re.finditer(substring,inp_string)]
#print(a)
#all_pos=set()
#for i in range(len(inp_string)):
#    pos = inp_string.find(substring,i)
#    if(pos > -1):
#        all_pos.add(pos+1)
#    else:
#        break
#print(sorted(all_pos))