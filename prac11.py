a = [5, 10, 15, 20, 25]

b = []

def new_list():
    b.append(a[0])
    b.append(a[-1])
    print(a)
    print(b)


new_list()