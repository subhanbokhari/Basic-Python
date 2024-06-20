def factorial(n):
    if(n ==1):
        return 1
    else:
        sum = n * factorial(n-1)
    return sum

print(factorial(5))

def fibonacci(n, n2, count):
    if count <= 0:
        return
    else:
        print(n)
        sum = n + n2
        fibonacci(n2, sum, count-1)

fibonacci(0, 1, 10)