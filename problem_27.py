'''
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
'''

def check_balance(s):
    char_map = {
        '}': '{',
        ']': '[',
        ')': '(',
    }

    trace = []

    for char in s:
        if trace and char in char_map and trace[-1] == char_map[char]:
            trace.pop()
        else:
            trace.append(char)
    return not trace

if __name__ == '__main__':
    s1 = "([])[]({})"
    s2 = "([)]"
    s3 = "((()"
