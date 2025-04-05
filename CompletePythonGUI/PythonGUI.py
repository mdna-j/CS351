import re
from tkinter import *

# Regular expressions for each token type
token_specs = [
    ('Keyword', r'\b(if|else|int|float|print)\b'),  # Keywords
    ('Operator', r'[=+>*]'),  # Operators
    ('Separator', r'[\(\):";]'),  # Separators
    ('Float_Literal', r'\b\d+\.\d+\b'),  # Floats
    ('Int_Literal', r'\b\d+\b'),  # Integers
    ('Identifier', r'[a-zA-Z][a-zA-Z0-9]*'),  # Identifiers
    ('String_Literal', r'"[^"]*"'),  # Strings
    ('Whitespace', r'\s+')  # Whitespace
]

# Combine the token regular expressions
token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specs)


def CutOneLineTokens(code):
    tokens = []
    for match in re.finditer(token_regex, code):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        if token_type != 'Whitespace':  # Skip whitespace
            tokens.append(f'<{token_type}, {token_value}>')
    return tokens


# Parsing Functions with Detailed Parse Tree Output
def parse_math_expression(tokens):
    result = [
        "----parent node exp, finding children nodes:",
        "child node (internal): identifier",
        f"   identifier has child node (token): {tokens[0].split(', ')[1].strip('>')}",
        f"     accept token from the list: {tokens[0].split(', ')[1].strip('>')}",
        "child node (token): =",
        "     accept token from the list: =",
        "Child node (internal): math"
    ]
    result.extend(parse_math_tokens(tokens[2:]))
    return result


def parse_math_tokens(tokens):
    result = ["----parent node math, finding children nodes:"]
    i = 0
    while i < len(tokens):
        token_type, token_value = tokens[i].split(', ')
        token_value = token_value.strip('>')

        # Handle different types of tokens in expressions
        if "Int_Literal" in token_type:
            result.append("child node (internal): int")
            result.append(f"   int has child node (token): {token_value}")
            result.append(f"     accept token from the list: {token_value}")
        elif "Float_Literal" in token_type:
            result.append("child node (internal): float")
            result.append(f"   float has child node (token): {token_value}")
            result.append(f"     accept token from the list: {token_value}")
        elif "Operator" in token_type:
            result.append(f"child node (token): {token_value}")
            result.append(f"     accept token from the list: {token_value}")
        elif "Identifier" in token_type:
            result.append("child node (internal): identifier")
            result.append(f"   identifier has child node (token): {token_value}")
            result.append(f"     accept token from the list: {token_value}")

        i += 1
    return result


def if_exp(tokens):
    result = [
        "----parent node if-statement, finding children nodes:",
        "child node (internal): keyword 'if'",
        "   accept token from the list: if",
        "child node (internal): Condition"
    ]

    # Handling the condition part: skip 'if', '(' and ')'
    condition_tokens = tokens[2:-1]  # Exclude 'if' and parentheses
    result.extend(comparison_exp(condition_tokens))  # Handle comparison inside condition

    return result


def comparison_exp(tokens):
    result = []
    # Expecting a comparison expression, such as `mathresult1 > mathresult2`
    if len(tokens) == 3:  # Expecting 3 tokens: operand1, operator, operand2
        left_operand = tokens[0]
        operator = tokens[1]
        right_operand = tokens[2]

        # Output breakdown for the condition
        result.append("----parent node Condition, finding children nodes:")
        result.append(f"child node (internal): left_operand")
        result.append(f"   left_operand has child node (token): {left_operand}")
        result.append(f"     accept token from the list: {left_operand}")
        result.append(f"child node (token): {operator}")
        result.append(f"     accept token from the list: {operator}")
        result.append(f"child node (internal): right_operand")
        result.append(f"   right_operand has child node (token): {right_operand}")
        result.append(f"     accept token from the list: {right_operand}")
    else:
        result.append("Error in Condition: Unexpected tokens.")

    return result


def parse_print_statement(tokens):
    result = [
        "----parent node print-statement, finding children nodes:",
        "child node (internal): keyword 'print'",
        "   accept token from the list: print"
    ]

    # Handling the content inside the parentheses for print statement
    if len(tokens) == 2 and tokens[1].startswith('<String_Literal'):
        string_content = tokens[1].split(', ')[1].strip('>')
        result.append("child node (internal): string_content")
        result.append(f"   string_content has child node (token): {string_content}")
        result.append(f"     accept token from the list: {string_content}")
    else:
        result.append("Error in print statement: Expected string content.")

    return result


# GUI Class
class LexerGUI:
    def __init__(self, root):
        self.master = root
        self.master.title("Lexer & Parser Simulator")

        # Make the window resizable
        self.master.rowconfigure(1, weight=1)
        self.master.columnconfigure([0, 1, 2], weight=1)

        # GUI Layout
        self.input_label = Label(self.master, text="Source Code Input")
        self.output_label = Label(self.master, text="Lexer Output")
        self.parser_label = Label(self.master, text="Parser Output")
        self.line_number_label = Label(self.master, text="Current Processing Line: 0")

        self.input_text = Text(self.master, height=20, width=40)
        self.output_text = Text(self.master, height=20, width=40, state=DISABLED)
        self.parser_text = Text(self.master, height=20, width=40, state=DISABLED)

        self.next_button = Button(self.master, text="Next Line", command=self.process_next_line)
        self.quit_button = Button(self.master, text="Quit", command=self.master.quit)

        self.input_label.grid(row=0, column=0, padx=10, pady=10)
        self.output_label.grid(row=0, column=1, padx=10, pady=10)
        self.parser_label.grid(row=0, column=2, padx=10, pady=10)
        self.input_text.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.output_text.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.parser_text.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        self.line_number_label.grid(row=2, column=0, sticky=W, padx=10, pady=10)
        self.next_button.grid(row=2, column=0, sticky=E, padx=10, pady=10)
        self.quit_button.grid(row=2, column=1, sticky=W, padx=10, pady=10)

        self.current_line = 0
        self.source_lines = []

    def process_next_line(self):
        if self.current_line == 0:
            input_text = self.input_text.get("1.0", END)
            self.source_lines = input_text.splitlines()

        if self.current_line < len(self.source_lines):
            line = self.source_lines[self.current_line]
            tokens = CutOneLineTokens(line)

            self.output_text.config(state=NORMAL)
            for token in tokens:
                self.output_text.insert(END, token + '\n')
            self.output_text.insert(END, '\n')
            self.output_text.config(state=DISABLED)

            # Update line count
            self.current_line += 1
            self.line_number_label.config(text=f"Current Processing Line: {self.current_line}")

            # Parsing logic with parse tree output
            self.parser_text.config(state=NORMAL)
            if line.strip().startswith("if"):
                parse_result = if_exp(tokens)
            elif '=' in line:
                parse_result = parse_math_expression(tokens)
            elif line.strip().startswith("print"):
                parse_result = parse_print_statement(tokens)
            else:
                parse_result = ["Unknown statement type"]

            for step in parse_result:
                self.parser_text.insert(END, step + '\n')
            self.parser_text.insert(END, '\n')
            self.parser_text.config(state=DISABLED)


# Main function to create and run the GUI
if __name__ == '__main__':
    root = Tk()
    lexer_gui = LexerGUI(root)
    root.mainloop()