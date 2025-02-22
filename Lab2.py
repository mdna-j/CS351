import re
string = ["22.11", "23", "66.7f", "123abcde", "Case44", "Happy", "78", "66.7", "yes123", "Book111"]

# Task 1

def pattern_match(string):
    """
    Checks a given string against various patterns and prints matching results.
    """
    matched = False
    if re.match(r'^\d+$', string):
        print(f"{string} matches the pattern: An integer")
        matched = True
    if re.match(r'^\d+\.\d+$', string):
        print(f"{string} matches the pattern: A float consists of 1 or more digits before and after decimal point")
        matched = True
    if re.match(r'^\d+\.\d{2}$', string):
        print(f"{string} matches the pattern: A float with exactly 2 digits after the decimal point")
        matched = True
    if re.match(r'^\d+\.\d+f$', string):
        print(f"{string} matches the pattern: A float ends with letter f")
        matched = True
    if re.match(r'^[A-Z]+[a-z]+\d+$', string):
        print(f"{string} matches the pattern: Capital letters, followed by small case letters, followed by digits")
        matched = True
    if re.match(r'^\d{3}[a-z]{2,}$', string):
        print(f"{string} matches the pattern: Exactly 3 digits, followed by at least 2 letters")
        matched = True
    if not matched:
        print(f"{string} does not match any pattern")

# Run the pattern matching
for s in string:
    pattern_match(s)

# Task 2
def remove_integer_from_start(string):
    match = re.match(r'^(\d+)\s*(.*)', string)
    if match:
        integer_part = match.group(1)
        rest_of_string = match.group(2)
        print(f'Found integer {integer_part} at the beginning of this string. The rest of the string is: "{rest_of_string}"')
    else:
        print(f'No integer found at the beginning of the string: "{string}"')

# Test cases
remove_integer_from_start("22 street")
remove_integer_from_start("90years")

