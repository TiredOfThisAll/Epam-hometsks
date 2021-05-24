def get_pairs(lst: list) -> list:
    if not lst or len(lst) == 1:
        return None
    result = []
    for i in range(len(lst) - 1):
        result.append((lst[i], lst[i + 1]))
    return result
