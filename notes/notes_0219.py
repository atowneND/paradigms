def f():
    """ foo """
    return 1

## functions are objects
#print dir(f)
## this is how functions are called
#print f.__call__()
#print '__call__' in dir(f)


def outer():
    """ the outer function """
    def inner():
        """ new inner function definition """
        print "this is the inner function"
    return inner

# a couple of ways to call inner
g = outer
#g()()

s = outer()
#s.__call__()

def o2(f):
    def inner():
        print "before f()"
        ret = f()
        print "after f(), ret =",ret
    return inner

def foo(): return 1
g = o2(foo)
#g()


def fib(n):
    if (n==1) or (n==2): return 1
    else: return fib(n-1)+fib(n-2)

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

fib2 = memoize(fib)
d = 35
#fib2(d)

#### DOESN'T WORK on python 2.7 or on the student machine... WTF????
#def call_counter(func):
#    def helper(*args, **kwargs):
#        helper_calls += 1
#        return func(*args, **kwargs)
#    helper.calls = 0
#    helper.__name__ = func.__name__
#    return helper
#
#@call_counter
#def add1(x):
#    return x+1
#
#for i in xrange(50):
#    print add1(i)
