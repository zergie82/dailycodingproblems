'''
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
'''
import string

def encode(s):
    temp = []
    encoded = ''

    for char in s:
        if temp == [] or char == temp[-1]:
            temp.append(char)
        else:
            encoded += str(len(temp)) + temp[0]
            temp.clear()
            temp.append(char)

    encoded += str(len(temp)) + temp[0]

    return encoded

def decode(s):
    nums = string.digits
    num_temp = ''
    decoded = ''

    for char in s:
        if char in nums:
            num_temp += char
        else:
        #elif char in letters:
            decoded += int(num_temp) * char
            num_temp = ''

    return decoded

if __name__ == '__main__':
    s = "AAAABBBCCDAA" # 4A3B2C1D2A
    s2 ="ABCD" # 1A1B1C1D
    s3 = "AABCCCCDDA" # 2A1B4C2D1A

    assert decode(encode(s)) == s
    assert decode(encode(s2)) == s2
    assert decode(encode(s3)) == s3
