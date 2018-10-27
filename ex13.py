x = int(input("How many Fibonacci numbers do you want to generate?: "))

def fib(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return fib(n-1) + fib(n-2)

print(fib(x))


