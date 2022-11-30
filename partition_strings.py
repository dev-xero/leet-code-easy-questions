def partition(s: str, k: int, fill: str):
    st = ''
    res = []

    for char in s:
        if len(st) < k:
            st += char

        else:
            res.append(st)
            st = char

    else:
        res.append(st)
        fill_count = len(st) % k
        if fill_count != 0:
            res[-1] = f'{res[-1]}{fill * (k - fill_count)}'

    return res


print(partition('abcdefghijklm', 3, 'x'))
