def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(n - 1):
        return fibonacci(n-1)+fibonacci(n-2)



