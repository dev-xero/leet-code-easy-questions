def permutation(s: str, t: str) -> bool:
    # Time Complexity: O(n)
    # case-sensitive
    # a string is a permutation of the other if their lengths are the same
    # and that they contain the same letters
    # we've converted it into a set that contains characters in the string
    if len(s) == len(t) and set(s) == set(t):
        return True

    return False


print(permutation('h!ack', 'ahck!'))
