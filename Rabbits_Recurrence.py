def get_total(n):
    if n <= 1:
        return n
    else:
        return ((get_total(n-1) + int(childrens) * (get_total(n-2))))

data = open("/Users/snehalilawe/Desktop/Rosalind_BioInformatics/rosalind_fib.txt",'r').read()

months,childrens = data.split(sep=' ')

sum = 0
for i in range(1,int(months)+1):
    sum = get_total(i)
print(sum)









