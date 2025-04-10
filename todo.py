import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")
        self.root.config(bg="#f0f0f0")

        self.tasks = []

        # Heading
        tk.Label(root, text="📝 To-Do List", font=("Helvetica", 20, "bold"), bg="#f0f0f0").pack(pady=10)

        # Entry and Add button
        entry_frame = tk.Frame(root)
        entry_frame.pack(pady=10)

        self.task_entry = tk.Entry(entry_frame, font=("Helvetica", 14), width=22)
        self.task_entry.pack(side=tk.LEFT, padx=10)

        add_btn = tk.Button(entry_frame, text="Add Task", font=("Helvetica", 12), command=self.add_task)
        add_btn.pack(side=tk.LEFT)

        # Listbox to display tasks
        self.listbox = tk.Listbox(root, font=("Helvetica", 14), width=35, height=15, selectbackground="#a6a6a6")
        self.listbox.pack(pady=10)

        # Edit and Delete buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        edit_btn = tk.Button(btn_frame, text="Edit Task", font=("Helvetica", 12), width=12, command=self.edit_task)
        edit_btn.pack(side=tk.LEFT, padx=10)

        delete_btn = tk.Button(btn_frame, text="Delete Task", font=("Helvetica", 12), width=12, command=self.delete_task)
        delete_btn.pack(side=tk.LEFT)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty.")

    def edit_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            current_task = self.tasks[selected_index[0]]
            new_task = simpledialog.askstring("Edit Task", "Update the task:", initialvalue=current_task)
            if new_task:
                self.tasks[selected_index[0]] = new_task.strip()
                self.update_listbox()
        else:
            messagebox.showinfo("Select Task", "Please select a task to edit.")

    def delete_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            confirm = messagebox.askyesno("Delete Task", "Are you sure you want to delete this task?")
            if confirm:
                del self.tasks[selected_index[0]]
                self.update_listbox()
        else:
            messagebox.showinfo("Select Task", "Please select a task to delete.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
