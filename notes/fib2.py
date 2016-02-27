import time

def memoize(f):
    """memoize a function of one argument."""
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

#To wrap a function, use a decorator
@memoize
def fib(n):
    """Fibonacci sequence"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def timefib(n):
    """calculates clock time consumed by the running of the fib() function."""
    startTime = time.time()
    r = fib(n)
    elapsedTime = time.time() - startTime
    print('fib({}) = {}; finished in {} ms'.format(n,r,int(elapsedTime * 1000)))

if __name__ == '__main__':
    timefib(30)
    timefib(31)
    timefib(32)
    timefib(60)
