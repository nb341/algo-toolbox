def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


dp = [-1 for i in range(1000)]
 
def fib(n):
    if (n <= 1):
        return n
    global dp
    first = 0
    second = 0
 
    if (dp[n - 1] != -1):
        first = dp[n - 1]
    else:
        first = fib(n - 1)
    if (dp[n - 2] != -1):
        second = dp[n - 2]
    else:
        second = fib(n - 2)
    dp[n] = first + second
 
    # Memoization
    return dp[n]

# Function to return the required sum
def calculateSum(l, r):

	# Using our deduced result
	sum = fib(r + 2) - fib(l + 1)
	return sum%10


# This code is contributed by mits
if __name__ == '__main__':
    #from_, to = map(int, input().split())
    print(calculateSum(3,7))