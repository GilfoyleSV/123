def get_max(x, y, z):
    max = 0
    if x > y:
        max = x
    else:
        max = y

    if max > z:
        pass
    else:
        max = z

    return max
