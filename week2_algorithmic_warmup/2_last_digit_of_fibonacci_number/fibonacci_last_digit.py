# Uses python3
import sys
def get_fibonacci_last_digit_naive(n):
    ratio = 1.618034
    if n <= 1:
        return n

    #fn = ((ratio**n)-((1-ratio)**n))/(5**0.5)
    return ratio

if __name__ == '__main__':
    input = sys.stdin.read()
    # n = int(input)
    print(get_fibonacci_last_digit_naive(6))
