import sys

def main():
    """This function counts the number of upper case letters, lower case letters, punctuation marks, spaces and digits in a given string. """
    if len(sys.argv) < 2:
        raise AssertionError("no argument provided")
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument")
    text = sys.argv[1]
    count_upper = count_lower = count_punctuation = count_spaces = count_digits = 0

    for char in text:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
        elif char.isspace():
            count_spaces += 1
        elif char.isdigit():
            count_digits += 1
        else:
            count_punctuation += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{count_upper} upper letters")
    print(f"{count_lower} lower letters")
    print(f"{count_punctuation} punctuation marks")
    print(f"{count_spaces} spaces")
    print(f"{count_digits} digits")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")



    # i remove import re and use str methods instead of regex to count the characters in the string.
    # Using str methods (not regex) — they're Unicode-aware, so accented
    # characters and other non-ASCII letters are classified correctly.
    # upper_letters = re.findall(r'[A-Z]', sys.argv[1])
    # lower_letters = re.findall(r'[a-z]', sys.argv[1])
    # spaces = re.findall(r'\s', sys.argv[1])
    # digits = re.findall(r'\d', sys.argv[1])
    # # Find all punctuation characters r mean raw string, [^\w\s] means any character that is not a word character or whitespace character,
    # punctuation_characters = re.findall(r'[^\w\s]', sys.argv[1])
    # count_upper = len(upper_letters)
    # count_lower = len(lower_letters)
    # count_spaces = len(spaces)
    # count_digits = len(digits)
    # count_punctuation = len(punctuation_characters)