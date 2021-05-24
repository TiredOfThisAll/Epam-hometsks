def split_by_index(string, indexes):
    if not indexes:
        return [string]
    while not isinstance(indexes[0], int) or indexes[0] >= len(string) \
            or indexes[0] <= 0:
        del indexes[0]
        if not indexes:
            return [string]

    split_list = [string[0:indexes[0]]]
    i = 0
    size = len(indexes) - 1
    
    while i < size:
        if not isinstance(indexes[i + 1], int) or indexes[i] >= indexes[i + 1] \
                or indexes[i + 1] <= 0 or indexes[i + 1] >= len(string):
            del indexes[i + 1]
            size -= 1
            continue
        if not isinstance(indexes[i], int):
            del indexes[i]
            size -= 1
            continue
        split_list.append(string[indexes[i]:indexes[i + 1]])
        i += 1
    split_list.append(string[indexes[-1]:len(string)])
    return split_list
