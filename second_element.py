items = ["cheese", "water", "tea", "carrot", "sugar", "milk"]


def second(in_list):
    i = 0

    while i < len(in_list):
        print(in_list[i])
        i = i + 2


second(items)
