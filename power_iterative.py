def power(x, n):
    result = 1
    while n > 0:
        result = result * x
        n = n - 1

    return result


print(power(2, 3))
