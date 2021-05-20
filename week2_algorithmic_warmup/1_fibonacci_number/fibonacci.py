# Uses python3
def calc_fib(n):
    f = {}
    f[0] = 0
    f[1] = 1
    if (n <= 1):
        return n
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    
    return f[n]

# n = int(input('Enter value '))
print(calc_fib(40))
