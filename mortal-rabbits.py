'''
n = 6
m = 3
bunnies = [1,1]

months= 2
while months < n:
    if months < m:
        bunnies.append(bunnies[-2]+bunnies[-1])
    elif months == m or count == m+1
        bunnies.append(bunnies[-2]+bunnies[-1]-1)
    else
        bunnies.append(bunnies[-2]+bunnies[-1]-bunnies[-(m+1)])
    months+= 1

print(bunnies[-1])
'''
def mortal_fib(n, m):
    # Create an array of length m to keep track of the number of rabbits
    ages = [0] * m
    # Start with one rabbit being alive with m months to live
    ages[-1] = 1
    # Iterate over the number of n months to track
    for _ in range(1, n):
        # Newborns
        new_rabbits = sum(ages[:-1])
        # Shift ages left, i.e. getting older
        ages[:-1] = ages[1:] 
        # Assign newborns 
        ages[-1] = new_rabbits
    
    # At the end we have an array containing the number of rabbits alive
    # for each possible month in the rabbits lifespan (m).
    # The sum of all ages is then a representation of all rabbits
    # currently alive.
    return sum(ages)

if __name__ == '__main__':
    print(mortal_fib(6,3))  # Prints 4