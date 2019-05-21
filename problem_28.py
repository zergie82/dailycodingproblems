'''
Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly

'''

from math import floor

def split_into_lines(words, k):
    output = []
    current_line = []

    for word in words:
        if len(' '.join(current_line) + ' ' + word) > k:
            output.append(current_line)
            current_line = []
        current_line.append(word)

    output.append(current_line)
    return output

def justify(words, k):
    if len(words) == 1:
        word = words[0]
        num_spaces = k - len(word)
        return word + ' ' * num_spaces

    space_to_use = k - sum(len(word) for word in words)
    spaces_allowed = len(words) - 1

    space_chunk = floor(space_to_use / spaces_allowed)
    space_left = space_to_use - ( spaces_allowed * space_chunk )

    justified_output = []

    for word in words:
        justified_output.append(word)

        current_space = ' ' * space_chunk
        if space_left > 0:
            current_space += ' '
            space_left -= 1
        justified_output.append(current_space)

    print(justified_output)
    return ''.join(justified_output).rstrip()


if __name__ == '__main__':
    words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    k = 16
    lines = split_into_lines(words, k)
