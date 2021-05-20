# Uses python3
# properties of fib numbers >= 60
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def pisano(m):
    #n2 values
    previous, current = 0, 1
    for i in range(0, m*m):
        previous, current = current, (previous + current)%m
        if previous==0 and current==1:
            return i+1
def fibonacci_sum(n):
    if n <= 1:
        return n
    n = n%pisano(10)
    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

if __name__ == '__main__':
    input = input()
    n = int(input)
    print(fibonacci_sum(n))
