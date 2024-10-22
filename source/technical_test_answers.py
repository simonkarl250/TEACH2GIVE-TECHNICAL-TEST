""" 2. Write a Python function that checks whether a word or phrase is palindrome or not.
Note: A palindrome is word, phrase, or sequence that reads the same
backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"""


def check_if_palindrome(original_phrase):
    """ Removing the space in between and making sure that the word will be in lower case
        for uniformity in both forward and reverse
    """
    lowercase_unspaced_phrase = original_phrase.replace(" ", "").lower()

    # Reversing lowercase_unspaced_phrase the word to be compared with original word
    reversed_word = lowercase_unspaced_phrase[::-1]

    # Compare the reversed word to check if it matches with the original word
    if reversed_word == original_phrase:
        return "The word is a palindrome"
    else:
        return "The word is NOT a palindrome"


print(check_if_palindrome("madam"))  # True

"""3. Write a Python function to check whether a string is pangram or not. (Assume 
the string passed in does not have any punctuation)
Note: Pang rams are words or sentences containing every letter of the 
alphabet at least once. For example: "The quick brown fox jumps over the 
lazy dog"""


def check_if_pangram(string_to_test):
    #  Converting the passed sentence to lowercase so that we can reduce computation with lower and upper
    lowercase_string = string_to_test.lower()

    # defining all letters of the alphabet in lower case
    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    # Removing all the spaces so that we can check if all alphabets will be a set of the string
    all_letters_in_string = set(lowercase_string.replace(" ", ""))

    #  Check if all alphabet letters are in the string
    if alphabet.issubset(all_letters_in_string):
        return "This String is Pangram"
    else:
        return "This String is NOT a Pangram"


# Test the function with an example
print(check_if_pangram("The quick brown fox jumps over the lazy dog"))

"""
3. Write a program that takes an integer as input and returns an integer with 
reversed digit ordering.
Examples:
For input 500, the program should return 5.
For input -56, the program should return -65.
For input -90, the program should return -9.
For input 91, the program should return 19
"""


def reverse_integer(number_to_reverse):
    # it is easier to reverse a number if we convert it to string first
    string_to_reverse = str(number_to_reverse)

    if number_to_reverse < 0:
        # if number is negative we shall reverse the string after the sign
        reversed_str = "-" + string_to_reverse[:0:-1]
    else:
        # For positive numbers, will just reverse the digits
        reversed_str = string_to_reverse[::-1]

    # Convert the reversed string back to an integer
    return int(reversed_str)


# Test the function with examples
print(reverse_integer(-790))  # Output: 5

"""
5. Write a program that accepts a string as input, capitalizes the first letter of each 
word in the string, and then returns the result string.
Examples:
"hi"=> returns "Hi"
"i love programming"=> returns "I Love Programming"

"""


def capitalize_the_words(input_string):
    # Creating words in an array so we can loop each word capitalizing each letter
    words = input_string.split()
    capitalized_words = []
    # loop for words so that in the arrays
    for word in words:
        # Check if the word is not empty
        if len(word) > 0:
            # Capitalizing the first letter and make the rest lowercase
            capitalized_word = word[0].upper() + word[
                                                 1:].lower()
            capitalized_words.append(capitalized_word)

    return ' '.join(capitalized_words)


# Test
print(capitalize_the_words("hi"))
