import tkinter as tk
from tkinter import messagebox, font
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []


def save_tasks():
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)


def add_task():
    task_text = entry.get().strip()
    if task_text:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tasks.append({"task": task_text, "done": False, "created": timestamp})
        update_listbox()
        save_tasks()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")


def delete_task():
    selected = listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_listbox()
        save_tasks()


def toggle_done(event):
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["done"] = not tasks[index]["done"]
        update_listbox()
        save_tasks()


def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔️ " if task["done"] else "❌ "
        listbox.insert(tk.END, f"{status} {task['task']}")

root = tk.Tk()
root.title("🌟 Creative To-Do List")
root.geometry("500x500")
root.config(bg="#F5F5F5")


custom_font = font.Font(family="Helvetica", size=12)


frame = tk.Frame(root, bg="#F5F5F5")
frame.pack(pady=20)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(
    frame,
    width=50,
    height=15,
    font=custom_font,
    yscrollcommand=scrollbar.set,
    selectbackground="#A3D2CA",
    activestyle="dotbox"
)
listbox.pack(side=tk.LEFT)
listbox.bind('<Double-Button-1>', toggle_done)

scrollbar.config(command=listbox.yview)


entry = tk.Entry(root, font=custom_font, width=40)
entry.pack(pady=10)


btn_frame = tk.Frame(root, bg="#F5F5F5")
btn_frame.pack()

add_btn = tk.Button(btn_frame, text="➕ Add Task", command=add_task, bg="#58B4AE", fg="white", width=15)
add_btn.grid(row=0, column=0, padx=10)

del_btn = tk.Button(btn_frame, text="🗑️ Delete Task", command=delete_task, bg="#EF476F", fg="white", width=15)
del_btn.grid(row=0, column=1, padx=10)


tasks = load_tasks()
update_listbox()


root.mainloop()
