from tkinter import *


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
        self.line_number_label = Label(self.master, text="Current Processing Line: 0")

        # Creating Text widgets for multi-line input and output
        self.input_text = Text(self.master, height=20, width=40)
        self.output_text = Text(self.master, height=20, width=40, state=DISABLED)

        # Adding line numbers for the input text
        self.input_text.tag_configure("line_num", foreground="black")
        self.update_line_numbers()

        # Creating buttons
        self.next_button = Button(self.master, text="Next Line", command=self.process_next_line)
        self.quit_button = Button(self.master, text="Quit", command=self.master.quit)

        # Positioning the widgets side by side using grid
        self.input_label.grid(row=0, column=0, padx=10, pady=10)
        self.output_label.grid(row=0, column=1, padx=10, pady=10)

        self.input_text.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")  # Resize with window
        self.output_text.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")  # Resize with window

        self.line_number_label.grid(row=2, column=0, sticky=W, padx=10, pady=10)

        # Place "Next Line" and "Quit" buttons side by side
        self.next_button.grid(row=2, column=0, sticky=E, padx=10, pady=10)
        self.quit_button.grid(row=2, column=1, sticky=W, padx=10, pady=10)

        # Initialize line counter and source code lines
        self.current_line = 0
        self.source_lines = []

    def update_line_numbers(self):
        # Updates line numbers in the input textbox.
        self.input_text.delete("1.0", END)
        content = self.input_text.get("1.0", "end-1c")
        lines = content.splitlines()
        new_content = ""
        for i, line in enumerate(lines, 1):
            new_content += f"{i}: {line}\n"
        self.input_text.insert("1.0", new_content)

    def highlight_line(self, line_num):
        # Highlight the line being processed in the input text.
        self.input_text.tag_remove("highlight", "1.0", END)  # Remove previous highlights
        self.input_text.tag_configure("highlight", background="blue")

        line_start = f"{line_num}.0"
        line_end = f"{line_num}.end"
        self.input_text.tag_add("highlight", line_start, line_end)

    def process_next_line(self):
        # Get the text from the input if this is the first line
        if self.current_line == 0:
            input_text = self.input_text.get("1.0", END)
            self.source_lines = input_text.splitlines()

        # Process the current line if available
        if self.current_line < len(self.source_lines):
            line = self.source_lines[self.current_line]
            self.output_text.config(state=NORMAL)  # Enable editing for output
            self.output_text.insert(END, line + '\n')  # Add the current line to the output
            self.output_text.config(state=DISABLED)  # Disable editing for output

            # Update the current line counter and label
            self.current_line += 1
            self.line_number_label.config(text=f"Current Processing Line: {self.current_line}")

            # Highlight the current line in the input text
            self.highlight_line(self.current_line)


# Main function to create and run the GUI
if __name__ == '__main__':
    myTkRoot = Tk()  # Create the root window
    lexer_gui = LexerGUI(myTkRoot)
    myTkRoot.mainloop()