def in_range(start, stop, step=1):
    range_list = [start]
    while stop-start:
        start += step
        range_list.append(start)
    return range_list


print(in_range(0, 20, 2))
