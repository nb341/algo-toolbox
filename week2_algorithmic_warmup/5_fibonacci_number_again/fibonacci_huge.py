# Uses python3
import sys
import math
def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def pisano(m):
    #n2 values
    previous, current = 0, 1
    for i in range(0, m*m):
        previous, current = current, (previous + current)%m
        if previous==0 and current==1:
            return i+1

def fib_huge(n, m):
    if n <= 1:
        return n
    n = n % pisano(m)
    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
    return current%m

if __name__ == '__main__':
    # input = sys.stdin.read();
    # n, m = map(int, input.split())
    # print(get_fibonacci_huge_naive(n, m))
    print(fib_huge(100, 10))