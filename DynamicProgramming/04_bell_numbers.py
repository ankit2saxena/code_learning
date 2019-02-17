'''
Let S(n, k) be total number of partitions of n elements into k sets. 
The value of n’th Bell Number is sum of S(n, k) for k = 1 to n.

Given a set of n elements, the number of ways of partitioning it is the Bell Number given n, k.
The first few Bell numbers for n = 0, 1, 2, 3, ... are 1, 1, 2, 5, 15, 52, 203, ...
'''
    

def bell_simple(n):
    
    if n == 0 or n == 1:
        return 1
    
    bell_n = 0
    
    while n > 1:
        bell_n += n * bell_simple(n - 1)
        n = n - 1
    
    return bell_n            
    

def bell_dp(n):
    bell_n = [[0 for i in range(n + 1)] for j in range(n + 1)]
    
    bell_n[0][0] = 1
    
    for i in range(1, n + 1):
        bell_n[i][0] = bell_n[i - 1][i - 1]
        
        for j in range(1, i + 1):
            bell_n[i][j] = bell_n[i - 1][j - 1] + bell_n[i][j - 1]
            
    return bell_n[n][0]
    

if __name__ == '__main__':
    n = 6
    
    n_bell_simple = bell_simple(n)
    print(str(n) + 'th Bell number using Simple Method: ' + str(n_bell_simple))
    
    n_bell_dp = bell_dp(n)
    print(str(n) + 'th Bell number using Dynamic Programming Method: ' + str(n_bell_dp))
    