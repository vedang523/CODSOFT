import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")
        self.master.geometry("300x350")
        self.master.configure(bg="#f0f0f0")

        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.create_widgets()

    def create_widgets(self):
        # Entry for displaying result
        self.result_entry = tk.Entry(self.master, textvariable=self.result_var, font=("Arial", 16), bd=0, readonlybackground="white")
        self.result_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        # Buttons for digits and operations
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, column) in buttons:
            if text == '=':
                button = tk.Button(self.master, text=text, font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", bd=0, command=self.calculate)
            elif text == 'C':
                button = tk.Button(self.master, text=text, font=("Arial", 14), bg="#f44336", fg="white", bd=0, command=self.clear)
            else:
                button = tk.Button(self.master, text=text, font=("Arial", 14), bg="#607D8B", fg="white", bd=0, command=lambda t=text: self.append_text(t))

            button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
            button.bind("<Enter>", lambda event, b=button: self.on_enter(b))
            button.bind("<Leave>", lambda event, b=button: self.on_leave(b))

    def append_text(self, text):
        current_text = self.result_var.get()
        self.result_var.set(current_text + text)

    def calculate(self):
        try:
            expression = self.result_var.get()
            result = eval(expression)
            self.result_var.set(str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid expression")

    def clear(self):
        self.result_var.set("")

    def on_enter(self, button):
        button.config(bg="#455A64")

    def on_leave(self, button):
        button.config(bg="#607D8B")

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
