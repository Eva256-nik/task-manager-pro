import tkinter as tk
from tkinter import messagebox

tasks = []

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                tasks.append(line.strip())
    except:
        pass

def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        entry.delete(0, tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Ошибка", "Введите задачу")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except:
        messagebox.showwarning("Ошибка", "Выберите задачу")

def on_closing():
    save_tasks()
    root.destroy()

# GUI
root = tk.Tk()
root.title("Task Manager PRO")
root.geometry("400x400")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

btn_add = tk.Button(root, text="Добавить", command=add_task)
btn_add.pack()

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

btn_delete = tk.Button(root, text="Удалить", command=delete_task)
btn_delete.pack()

root.protocol("WM_DELETE_WINDOW", on_closing)

load_tasks()
update_listbox()

root.mainloop()
