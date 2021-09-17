def power(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    else:
        return x * power(x, n - 1)


print(power(2, 4))
