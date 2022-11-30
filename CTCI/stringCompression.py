# Time Complexity: O(n)
# Space Complexity: O(n)
def string_compression(s: str) -> str:
    c_str = ''
    count = 1

    # there's no use looping over if the length of the string is less than 2
    if len(s) < 2:
        c_str = f'{s}1'

    else:
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                count += 1

            else:
                c_str = f'{c_str}{s[i]}{count}'
                count = 1

            # next character is the last character
            if i + 1 == len(s) - 1:
                c_str = f'{c_str}{s[i+1]}{count}'

    return c_str if len(c_str) <= len(s) else s


print(string_compression('aab'))
