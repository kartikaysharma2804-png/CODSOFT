# TASK 5 - CONTACT BOOK (GUI VERSION)
# A simple contact book using Tkinter where the user can
# add, view, search, update, and delete contacts.
# Colors added to make the GUI look nicer.

import tkinter as tk
from tkinter import messagebox

contacts = []

# ---- Simple color palette (easy to change) ----
BG_COLOR = "#eaf2f8"       # light blue background
TITLE_COLOR = "#1a5276"    # dark blue text
ADD_COLOR = "#27ae60"      # green
UPDATE_COLOR = "#2980b9"   # blue
DELETE_COLOR = "#c0392b"   # red
SEARCH_COLOR = "#f39c12"   # orange
TEXT_ON_BUTTON = "white"


def refresh_list():
    contact_listbox.delete(0, tk.END)
    for c in contacts:
        contact_listbox.insert(tk.END, c["name"] + " - " + c["phone"])


def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name == "" or phone == "":
        messagebox.showwarning("Warning", "Name and phone number are required.")
        return

    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    clear_entries()
    refresh_list()
    messagebox.showinfo("Success", "Contact added successfully!")


def show_selected_contact(event):
    selected = contact_listbox.curselection()
    if not selected:
        return
    c = contacts[selected[0]]
    clear_entries()
    name_entry.insert(0, c["name"])
    phone_entry.insert(0, c["phone"])
    email_entry.insert(0, c["email"])
    address_entry.insert(0, c["address"])


def update_contact():
    selected = contact_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a contact to update.")
        return
    index = selected[0]
    contacts[index] = {
        "name": name_entry.get().strip(),
        "phone": phone_entry.get().strip(),
        "email": email_entry.get().strip(),
        "address": address_entry.get().strip()
    }
    refresh_list()
    messagebox.showinfo("Success", "Contact updated successfully!")


def delete_contact():
    selected = contact_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a contact to delete.")
        return
    index = selected[0]
    removed = contacts.pop(index)
    clear_entries()
    refresh_list()
    messagebox.showinfo("Deleted", "Deleted contact: " + removed["name"])


def search_contact():
    keyword = name_entry.get().strip().lower()
    contact_listbox.delete(0, tk.END)
    if keyword == "":
        refresh_list()
        return
    for c in contacts:
        if keyword in c["name"].lower() or keyword in c["phone"]:
            contact_listbox.insert(tk.END, c["name"] + " - " + c["phone"])


window = tk.Tk()
window.title("Contact Book")
window.geometry("450x540")
window.configure(bg=BG_COLOR)

title_label = tk.Label(
    window, text="Contact Book", font=("Arial", 16, "bold"),
    bg=BG_COLOR, fg=TITLE_COLOR
)
title_label.pack(pady=10)

form_frame = tk.Frame(window, bg=BG_COLOR)
form_frame.pack(pady=5)

tk.Label(form_frame, text="Name:", bg=BG_COLOR, font=("Arial", 10)).grid(row=0, column=0, sticky="e")
name_entry = tk.Entry(form_frame, width=25, font=("Arial", 10))
name_entry.grid(row=0, column=1, pady=2)

tk.Label(form_frame, text="Phone:", bg=BG_COLOR, font=("Arial", 10)).grid(row=1, column=0, sticky="e")
phone_entry = tk.Entry(form_frame, width=25, font=("Arial", 10))
phone_entry.grid(row=1, column=1, pady=2)

tk.Label(form_frame, text="Email:", bg=BG_COLOR, font=("Arial", 10)).grid(row=2, column=0, sticky="e")
email_entry = tk.Entry(form_frame, width=25, font=("Arial", 10))
email_entry.grid(row=2, column=1, pady=2)

tk.Label(form_frame, text="Address:", bg=BG_COLOR, font=("Arial", 10)).grid(row=3, column=0, sticky="e")
address_entry = tk.Entry(form_frame, width=25, font=("Arial", 10))
address_entry.grid(row=3, column=1, pady=2)

button_frame = tk.Frame(window, bg=BG_COLOR)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add", width=10, font=("Arial", 9, "bold"),
          bg=ADD_COLOR, fg=TEXT_ON_BUTTON, command=add_contact).grid(row=0, column=0, padx=3)
tk.Button(button_frame, text="Update", width=10, font=("Arial", 9, "bold"),
          bg=UPDATE_COLOR, fg=TEXT_ON_BUTTON, command=update_contact).grid(row=0, column=1, padx=3)
tk.Button(button_frame, text="Delete", width=10, font=("Arial", 9, "bold"),
          bg=DELETE_COLOR, fg=TEXT_ON_BUTTON, command=delete_contact).grid(row=0, column=2, padx=3)
tk.Button(button_frame, text="Search", width=10, font=("Arial", 9, "bold"),
          bg=SEARCH_COLOR, fg=TEXT_ON_BUTTON, command=search_contact).grid(row=0, column=3, padx=3)

contact_listbox = tk.Listbox(window, width=50, height=12, bg="white", selectbackground=UPDATE_COLOR)
contact_listbox.pack(pady=10)
contact_listbox.bind("<<ListboxSelect>>", show_selected_contact)

tk.Label(
    window, text="Tip: type in Name/Phone above and click Search to filter.",
    font=("Arial", 8), bg=BG_COLOR
).pack()

window.mainloop()
