import tkinter as tk
from tkinter import messagebox

# функция за добавяне на задача
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Внимание", "Моля въведете задача!")

# функция за изтриване на избраната задача
def delete_task():
    try:
        selected_task = listbox.curselection()
        listbox.delete(selected_task)
    except:
        messagebox.showwarning("Внимание", "Няма избрана задача за изтриване!")

# създаваме основния прозорец
root = tk.Tk()
root.title("To-Do List")

# поле за въвеждане
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# бутони
add_button = tk.Button(root, text="Добави задача", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Изтрий задача", command=delete_task)
delete_button.pack(pady=5)

# списък със задачи
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# стартираме приложението
root.mainloop()
