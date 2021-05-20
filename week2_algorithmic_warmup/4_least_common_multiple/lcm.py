# Uses python3
import sys
import math
def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)
def lcm(a,b):
    m = math.sqrt((a**2)*(b**2))
    return int(m/gcd(a,b))

if __name__ == '__main__':
    # input = sys.stdin.read()
    # a, b = map(int, input.split())
    # print(lcm_naive(a, b))
    print(lcm(761457, 614573))

