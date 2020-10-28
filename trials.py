"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """Print each item in the given array."""
    for item in items:
        print(item)


def get_all_evens(nums):
    """Given an array of numbers, return an array of all even numbers."""

    nums = []

    for num in nums:
        if num % 2 == 0:
            nums.append(num)
    return nums


def get_odd_indices(items):
    """Given an array, return all elements at odd numbered indices."""
    
    result = []

    for i in range(len(items)):
        if i % 2 != 0:
            result.append(items[i)
    return result



def print_as_numbered_list(items):
    """Given an array, output a numbered list."""
    i = 1

    for item in items:
        print(f"{i}. {item}")
        i+=1
    

def get_range(start, stop):
    """Return an array of numbers in a certain range."""
    nums = []
    
    for num in range(start,stop):
        nums.append(num)
    return nums
        

def censor_vowels(word):
    """Given a string, return a string where vowels are replaced with '*'."""
    chars = []
    for letter in word:
        if letter in ['a', 'e', 'i', 'o', 'u']:
            chars.append('*')
        else:
            chars.append(letter)
    return ''.join(chars)


def snake_to_camel(string):
    camelCase = []

    for word in string.split("_"):
        camelCase.append(f"{word[0].upper()}{word[1:]}")
    return "".join(camelCase)

def longest_word_length(words):
    longest = len(words[0])
    for word in words:
        if longest < len(word):
            longest = len(word)
    return longest

def truncate(string):
    result = []
    for char in string:
        if len(result) == 0 or char != result[-1]:
            result.append(char)
    return "".join(result)

def has_balanced_parens(string):
    parens = 0
    for char in string:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1
    
    return parens == 0

def compress(string):
    compressed = []
    curr_char = ''
    char_count = 0
    for char in string:
        if char != curr_char:
            compressed.append(curr_char)

            if char_count > 1:
                compressed.append(str(char_count))
            curr_char = char
            char_count = 0
        char_count += 1
    compressed.append(curr_char)
    if char_count > 1:
        compressed.append(str(char_count))
    return "".join(compressed)