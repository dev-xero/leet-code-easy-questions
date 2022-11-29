def match_pair(s: str) -> bool:
    char_map = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    char_stack = []

    for char in s:
        # check if the character is in our hash map / is an 'opener'
        if char in char_map:
            # add its 'closer' to the top of the stack
            char_stack.append(char_map[char])

        # if it isn't, check if we have this character at the top of the stack
        else:
            if char_stack and char_stack[-1] == char:
                char_stack.pop()

            # if we don't, that means that this character has no opening bracket
            else:
                return False

    return True if not char_stack else False  # if the stack is empty, then we matched everything


test_str = '(){}[]()({[{}]})'
print(match_pair(test_str))
