import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("400x200")
        self.master.configure(bg="#f0f0f0")

        self.length_label = tk.Label(master, text="Password Length:", font=("Arial", 12), bg="#f0f0f0")
        self.length_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.length_entry = tk.Entry(master, font=("Arial", 12), width=10)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.generate_button = tk.Button(master, text="Generate Password", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.generate_password)
        self.generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.password_label = tk.Label(master, text="Generated Password:", font=("Arial", 12), bg="#f0f0f0")
        self.password_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(master, textvariable=self.password_var, font=("Arial", 14), bg="white", bd=0, state="readonly")
        self.password_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                messagebox.showwarning("Warning", "Password length must be a positive integer.")
                return
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_var.set(password)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid integer.")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
