#prac14
ls1 = [1, 1, 2, 3, 4, 4, 5]


def duplicate(ls1):
    ls2 = []
    for i in ls1:
        if i not in ls2:
            ls2.append(i)
    return ls2


ls2 = duplicate(ls1)
print(ls2)
