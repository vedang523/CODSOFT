import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        self.master.geometry("400x300")

        self.tasks = []

        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task, bg="green", fg="white")
        self.add_button.grid(row=0, column=2, padx=5, pady=10)

        self.tasks_label = tk.Label(master, text="Tasks:", font=("Arial", 14, "bold"))
        self.tasks_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.tasks_listbox = tk.Listbox(master, width=50, height=10, font=("Arial", 12))
        self.tasks_listbox.grid(row=2, column=0, padx=10, pady=5, columnspan=2, rowspan=5)

        self.mark_done_button = tk.Button(master, text="Mark as Done", command=self.mark_task_done, bg="blue", fg="white")
        self.mark_done_button.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task, bg="red", fg="white")
        self.delete_button.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")

        self.clear_button = tk.Button(master, text="Clear All", command=self.clear_all, bg="orange", fg="white")
        self.clear_button.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def mark_task_done(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks_listbox.delete(index)
            del self.tasks[index]

    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.tasks_listbox.delete(index)

    def clear_all(self):
        confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?")
        if confirmed:
            self.tasks_listbox.delete(0, tk.END)
            self.tasks.clear()

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
