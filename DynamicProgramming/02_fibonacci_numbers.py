'''
The Fibonacci numbers are the numbers in the following integer sequence.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

F(n) = F(n-1) + F(n-2)
'''

def fibonacci_simple(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci_simple(n - 1) + fibonacci_simple(n - 2)
    

def fibonacci_dp(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    t1 = 0
    t2 = 1
    
    for i in range(2, n):
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        
    return t1 + t2


if __name__ == '__main__':
    n = 12
    
    n_fibonacci_simple = fibonacci_simple(n)
    print(str(n) + 'th Fibonacci number using Simple Method: ' + str(n_fibonacci_simple))
    
    n_fibonacci_dp = fibonacci_dp(n)
    print(str(n) + 'th Fibonacci number using Dynamic Programming Method: ' + str(n_fibonacci_dp))
    