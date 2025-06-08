import sqlite3
from tkinter import *
from tkinter import messagebox

# Initialize DB
conn = sqlite3.connect('contacts.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT,
    address TEXT
)''')
conn.commit()

# Functions
def add_contact():
    name = name_var.get()
    phone = phone_var.get()
    email = email_var.get()
    address = address_var.get()

    if not name or not phone:
        messagebox.showerror("Error", "Name and phone are required")
        return

    c.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
              (name, phone, email, address))
    conn.commit()
    clear_entries()
    view_contacts()
    messagebox.showinfo("Success", "Contact added successfully!")

def view_contacts():
    listbox.delete(0, END)
    c.execute("SELECT * FROM contacts")
    for row in c.fetchall():
        listbox.insert(END, f"{row[0]}. {row[1]} - {row[2]}")

def search_contact():
    query = search_var.get()
    listbox.delete(0, END)
    c.execute("SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?", (f'%{query}%', f'%{query}%'))
    for row in c.fetchall():
        listbox.insert(END, f"{row[0]}. {row[1]} - {row[2]}")

def load_selected_contact(event):
    selected = listbox.curselection()
    if not selected:
        return
    idx = listbox.get(selected[0]).split(".")[0]
    c.execute("SELECT * FROM contacts WHERE id=?", (idx,))
    row = c.fetchone()
    if row:
        name_var.set(row[1])
        phone_var.set(row[2])
        email_var.set(row[3])
        address_var.set(row[4])
        update_btn.config(state=NORMAL)
        delete_btn.config(state=NORMAL)
        global selected_id
        selected_id = row[0]

def update_contact():
    if not selected_id:
        return
    c.execute("UPDATE contacts SET name=?, phone=?, email=?, address=? WHERE id=?",
              (name_var.get(), phone_var.get(), email_var.get(), address_var.get(), selected_id))
    conn.commit()
    clear_entries()
    view_contacts()
    messagebox.showinfo("Updated", "Contact updated!")
    update_btn.config(state=DISABLED)
    delete_btn.config(state=DISABLED)

def delete_contact():
    if not selected_id:
        return
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this contact?")
    if confirm:
        c.execute("DELETE FROM contacts WHERE id=?", (selected_id,))
        conn.commit()
        clear_entries()
        view_contacts()
        messagebox.showinfo("Deleted", "Contact deleted!")
        update_btn.config(state=DISABLED)
        delete_btn.config(state=DISABLED)

def clear_entries():
    name_var.set("")
    phone_var.set("")
    email_var.set("")
    address_var.set("")
    search_var.set("")

# GUI
root = Tk()
root.title("Contact Book")
root.geometry("500x500")

name_var = StringVar()
phone_var = StringVar()
email_var = StringVar()
address_var = StringVar()
search_var = StringVar()
selected_id = None

# Form
Label(root, text="Name").pack()
Entry(root, textvariable=name_var).pack()

Label(root, text="Phone").pack()
Entry(root, textvariable=phone_var).pack()

Label(root, text="Email").pack()
Entry(root, textvariable=email_var).pack()

Label(root, text="Address").pack()
Entry(root, textvariable=address_var).pack()

Button(root, text="Add Contact", command=add_contact).pack(pady=5)

# Search
Label(root, text="Search by Name/Phone").pack()
Entry(root, textvariable=search_var).pack()
Button(root, text="Search", command=search_contact).pack(pady=5)

# Contact List
listbox = Listbox(root, width=60)
listbox.pack(pady=10)
listbox.bind('<<ListboxSelect>>', load_selected_contact)

# Update/Delete
update_btn = Button(root, text="Update Contact", command=update_contact, state=DISABLED)
update_btn.pack(pady=2)

delete_btn = Button(root, text="Delete Contact", command=delete_contact, state=DISABLED)
delete_btn.pack(pady=2)

view_contacts()  # Load on start

root.mainloop()
