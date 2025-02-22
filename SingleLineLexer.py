import re

# Regular expressions for each token type

token_specs = [
    ('Keyword', r'\b(if|else|int|float)\b'),        # Keywords
    ('Operator', r'[=+>*]'),                        # Operators
    ('Separator', r'[\(\):";]'),                    # Separators
    ('Float_Literal', r'\b\d+\.\d+\b'),             # Floats
    ('Int_Literal', r'\b\d+\b'),                    # Integers
    ('Identifier', r'[a-zA-Z][a-zA-Z0-9]*'),        # Identifiers
    ('String_Literal', r'"[^"]*"'),                 # Strings
    ('Whitespace', r'\s+')                          # Whitespace
]


# Combine the token regular expressions
token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specs)


def lexer(code):
    # Tokenize the input code using the regex patterns
    for match in re.finditer(token_regex, code):
        token_type = match.lastgroup
        token_value = match.group(token_type)

        if token_type == 'Whitespace':
            continue  # Skip whitespace

        # We first check for specific tokens (Order matters):
        if token_type == 'Keyword':
            print(f'<{token_type}, {token_value}>')
        elif token_type == 'Operator':
            print(f'<{token_type}, {token_value}>')
        elif token_type == 'Separator':
            print(f'<{token_type}, {token_value}>')
        elif token_type == 'Float_Literal':
            print(f'<{token_type}, {token_value}>')
        elif token_type == 'Int_Literal':
            print(f'<{token_type}, {token_value}>')
        elif token_type == 'Identifier':
            print(f'<{token_type}, {token_value}>')
        elif token_type == 'String_Literal':
            print(f'<{token_type}, {token_value}>')
        else:
            print(f'<UNKNOWN, {token_value}>')

# Example
lexer('int A1=5')

# Expected result :
# <Keyword, int>
# <Identifier, A1>
# <Operator, =>
# <Int_Literal, 5>

