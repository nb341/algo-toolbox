# Uses python3
import sys
import math
def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    fn = (((math.sqrt(5)+1)/2)**n)/math.sqrt(5)
    return round(fn)%10

if __name__ == '__main__':
    # input = sys.stdin.read()
    # n = int(input)
    print(get_fibonacci_last_digit_naive(1000))
