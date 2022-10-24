# Split in Half
# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

def split_in_half(string):
    if len(string) % 2 == 0:
        return string[int(len(string) / 2):] + string[:int(len(string) / 2)]
    else:
        return string[int((len(string) - 1) / 2 + 1):] + string[:int((len(string) - 1) / 2 + 1)]


# Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.

def is_unique(string):
    l = []
    for i in string:
        if i in l:
            return False
        else:
            l.append(i)
    return True
