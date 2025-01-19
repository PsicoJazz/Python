#def nfat(l):
    n = 0
    fat = 1

    while fat <= l:
        n += 1
        fat *= n
    return n-1
