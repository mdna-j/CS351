import re
from tkinter import *

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

def CutOneLineTokens(code):
    # List to store <type, token> pairs
    tokens = []

    # Tokenize the input code using the regex patterns
    for match in re.finditer(token_regex, code):
        token_type = match.lastgroup
        token_value = match.group(token_type)

        if token_type == 'Whitespace':
            continue  # Skip whitespace

        tokens.append(f'<{token_type}, {token_value}>')

    return tokens

# Parsing Functions
def parse_math_expression(tokens):
    # Simplified parsing for the math expression using basic BNF
    result = []
    for token in tokens:
        result.append(f"Processing token: {token}")
    return result

def parse_if_statement(tokens):
    # Parsing logic for 'if' statements
    result = []
    if tokens[0] == '<Keyword, if>':
        result.append("Found 'if' keyword")
        if tokens[1] == '<Separator, (>' and tokens[3] == '<Separator, )>':
            result.append("Found '(' and ')'")
        if tokens[4] == '<Operator, >':
            result.append("Found '>' operator")
        if tokens[5] == '<Separator, :>':
            result.append("Found ':'")
    return result

def parse_print_statement(tokens):
    # Parsing logic for 'print' statements
    result = []
    if tokens[0] == '<Keyword, print>':
        result.append("Found 'print' keyword")
    return result

# GUI Class
class LexerGUI:
    def __init__(self, root):
        self.master = root
        self.master.title("Lexer Simulator")

        # Enable resizing of the window
        self.master.rowconfigure(1, weight=1)  # Row 1 (Textboxes) can grow
        self.master.columnconfigure(0, weight=1)  # Input column grows
        self.master.columnconfigure(1, weight=1)  # Output column grows

        # Creating labels for input and output
        self.input_label = Label(self.master, text="Source Code Input")
        self.output_label = Label(self.master, text="Lexer Output")
        self.parser_label = Label(self.master, text="Parser Output")
        self.line_number_label = Label(self.master, text="Current Processing Line: 0")

        # Creating Text widgets for multi-line input and output
        self.input_text = Text(self.master, height=20, width=40)
        self.output_text = Text(self.master, height=20, width=40, state=DISABLED)
        self.parser_text = Text(self.master, height=20, width=40, state=DISABLED)

        # Creating buttons
        self.next_button = Button(self.master, text="Next Line", command=self.process_next_line)
        self.quit_button = Button(self.master, text="Quit", command=self.master.quit)

        # Positioning the widgets side by side using grid
        self.input_label.grid(row=0, column=0, padx=10, pady=10)
        self.output_label.grid(row=0, column=1, padx=10, pady=10)
        self.parser_label.grid(row=0, column=2, padx=10, pady=10)
        self.input_text.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.output_text.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.parser_text.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        self.line_number_label.grid(row=2, column=0, sticky=W, padx=10, pady=10)
        self.next_button.grid(row=2, column=0, sticky=E, padx=10, pady=10)
        self.quit_button.grid(row=2, column=1, sticky=W, padx=10, pady=10)

        # Initialize line counter and source code lines
        self.current_line = 0
        self.source_lines = []

    def process_next_line(self):
        if self.current_line == 0:
            input_text = self.input_text.get("1.0", END)
            self.source_lines = input_text.splitlines()

        if self.current_line < len(self.source_lines):
            line = self.source_lines[self.current_line]
            tokens = CutOneLineTokens(line)

            # Append tokens to the output
            self.output_text.config(state=NORMAL)
            for token in tokens:
                self.output_text.insert(END, token + '\n')
            self.output_text.insert(END, '\n')  # Extra newline for spacing
            self.output_text.config(state=DISABLED)

            # Update current line and line number label
            self.current_line += 1
            self.line_number_label.config(text=f"Current Processing Line: {self.current_line}")

            # Parsing
            self.parser_text.config(state=NORMAL)
            if line.strip().startswith("if"):
                parse_result = parse_if_statement(tokens)
            elif '=' in line:
                parse_result = parse_math_expression(tokens)
            elif line.strip().startswith("print"):
                parse_result = parse_print_statement(tokens)
            else:
                parse_result = ["Unknown statement type"]

            for step in parse_result:
                self.parser_text.insert(END, step + '\n')
            self.parser_text.insert(END, '\n')  # Extra newline for spacing
            self.parser_text.config(state=DISABLED)

# Main function to create and run the GUI
if __name__ == '__main__':
    root = Tk()
    lexer_gui = LexerGUI(root)
    root.mainloop()