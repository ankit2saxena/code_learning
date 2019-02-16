'''
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. 
The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. 
By convention, 1 is included.

Given a number n, the task is to find n(th) Ugly number.
'''

def is_ugly_simple(n):
    while n % 2 == 0:
        n = n / 2
    while n % 3 == 0:
        n = n / 3
    while n % 5 == 0:
        n = n / 5
    if n == 1:
        return True
    else:
        return False
    
    
def ugly_simple(n):
    if n == 1:
        return 1
    
    i = 1
    ugly_count = 1
    
    while ugly_count < n:
        i += 1
        if is_ugly_simple(i):
            ugly_count += 1
            
    return i


def ugly_dp(n):
    ugly_numbers = [0] * n
    ugly_numbers[0] = 1
    
    n2 = n3 = n5 = 0
    
    for i in range(1, n):
        ugly_numbers[i] = min(2 * ugly_numbers[n2], 3 * ugly_numbers[n3], 5 * ugly_numbers[n5])
        
        if ugly_numbers[i] == 2 * ugly_numbers[n2]:
            n2 += 1
        if ugly_numbers[i] == 3 * ugly_numbers[n3]:
            n3 += 1
        if ugly_numbers[i] == 5 * ugly_numbers[n5]:
            n5 += 1
        
    return ugly_numbers[-1]
    

if __name__ == '__main__':
    n = 150
    
    n_ugly_simple = ugly_simple(n)
    print(str(n) + 'th Ugly number using Simple Method: ' + str(n_ugly_simple))
    
    n_ugly_dp = ugly_dp(n)
    print(str(n) + 'th Ugly number using Dynamic Programming Method: ' + str(n_ugly_dp))
    