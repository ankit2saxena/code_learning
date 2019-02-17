'''
Catalan numbers are a sequence of natural numbers that occurs in many interesting counting problems like following.
1) Count the number of expressions containing n pairs of parentheses which are correctly matched. For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).
2) Count the number of possible Binary Search Trees with n keys.
3) Count the number of full binary trees (A rooted binary tree is full if every vertex has either two children or no children) with n+1 leaves.

The first few Catalan numbers for n = 0, 1, 2, 3, … are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, ...
'''

def catalan_simple(n):
    
    if n == 0 or n == 1:
        return 1
    
    output = 0
    
    for i in range(0, n):
        output += catalan_simple(i) * catalan_simple(n - i - 1)
    
    return output


def catalan_dp(n):
    if n == 0 or n == 1:
        return 1
    
    catalans = [0 for i in range(0, n + 1)]
    catalans[0] = 1
    catalans[1] = 1
    
    for i in range(2, n + 1):
        catalans[i] = 0
        
        for j in range(i):
            catalans[i] += catalans[j] * catalans[i - j - 1]
            
    return catalans[-1]


if __name__ == '__main__':
    n = 9
    
    n_catalan_simple = catalan_simple(n)
    print(str(n) + 'th Fibonacci number using Simple Method: ' + str(n_catalan_simple))
    
    n_catalan_dp = catalan_dp(n)
    print(str(n) + 'th Fibonacci number using Dynamic Programming Method: ' + str(n_catalan_dp))
    