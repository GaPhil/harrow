def convert_to_binary(n):
    if n > 1:
        # // is floor division
        convert_to_binary(n // 2)
    print(n % 2)


convert_to_binary(5)
