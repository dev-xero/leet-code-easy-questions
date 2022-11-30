def partition(s: str, k: int, fill: str):
    st = ''
    res = []

    for char in s:
        if len(st) < 3:
            st += char

        else:
            res.append(st)
            st = char

    else:
        res.append(st)
        fill_count = len(st) % 3
        if fill_count != 0:
            res[-1] = f'{res[-1]}{fill * (3 - fill_count)}'

    print(res)


partition('abcdefghijklm', 3, 'x')
