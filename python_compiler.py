import tkinter as tk
from tkinter import scrolledtext
import sys
import io

class PythonCompilerApp:
    def __init__(self, master):
        self.master = master
        master.title("Python Compiler")

        # Create a Text area for input
        self.code_input = scrolledtext.ScrolledText(master, width=60, height=20)
        self.code_input.pack(pady=10)

        # Create a button to compile and execute code
        self.run_button = tk.Button(master, text="Run Code", command=self.run_code)
        self.run_button.pack(pady=5)

        # Create a Text area for output
        self.output_area = scrolledtext.ScrolledText(master, width=60, height=10)
        self.output_area.pack(pady=10)

    def run_code(self):
        # Clear previous output
        self.output_area.delete(1.0, tk.END)

        # Redirect stdout to capture print statements
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        # Get the code from the text area
        code = self.code_input.get("1.0", tk.END)

        try:
            # Compile the source code into bytecode
            compiled_code = compile(code, '<string>', 'exec')

            # Execute the compiled code
            exec(compiled_code)
        except SyntaxError as e:
            self.output_area.insert(tk.END, f"Syntax Error: {e}\n")
        except Exception as e:
            self.output_area.insert(tk.END, f"Error: {e}\n")
        finally:
            # Restore stdout
            sys.stdout = old_stdout

        # Get the output and display it
        output = new_stdout.getvalue()
        self.output_area.insert(tk.END, output)

if __name__ == "__main__":
    root = tk.Tk()
    app = PythonCompilerApp(root)
    root.mainloop()
