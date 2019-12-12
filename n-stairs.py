# ways to climb stairs
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    stairs = 4
    print(fib(stairs+1))
