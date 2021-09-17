def factorial(n):
    result = 1

    while n > 0:
        result = result * n
        n = n - 1

    return result


print(factorial(4))
