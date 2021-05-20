# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


# Function to return the required sum
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
    n = n%60
    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)
        sum += current**2

    return sum % 10



if __name__ == '__main__':
    # n = int(stdin.read())
    print(fibonacci_sum(7))
