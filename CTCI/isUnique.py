def is_unique(s: str) -> bool:
    seen = set()

    for char in s:
        if char not in seen:
            seen.add(char)
        else:
            return False

    return True


def is_unique_v2(s: str) -> bool:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    seen_str = ''
    for char in s:
        if char not in seen_str:
            seen_str = f'{seen_str}{char}'
        else:
            return False

    return True


test_str = 'code'
print(is_unique(test_str))
print(is_unique_v2(test_str))
