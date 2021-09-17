def counter(n):
    if n == 1:
        print(1)
    else:
        print(n)
        return counter(n - 1)


counter(6)
