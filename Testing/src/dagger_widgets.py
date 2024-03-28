import customtkinter as ctk
from tkinter import ttk

def create_label(root, text, row, column):
    label = ctk.CTkLabel(root, text=text)
    label.grid(row=row, column=column, padx=5, pady=5)
    return label

def create_combobox(root, values, row, column):
    combobox = ttk.Combobox(root, values=values)
    combobox.grid(row=row, column=column, padx=5, pady=5)
    return combobox

def create_entry(root, row, column):
    entry = ctk.CTkEntry(root)
    entry.grid(row=row, column=column, padx=5, pady=5)
    return entry

def create_button(root, text, command, row, column):
    button = ctk.CTkButton(root, text=text, command=command)
    button.grid(row=row, column=column, padx=5, pady=5)
    return button

def create_textbox(root, row, column, columnspan):
    textbox = ctk.CTkTextbox(root, wrap='word')
    textbox.grid(row=row, column=column, columnspan=columnspan, sticky='nsew')
    return textbox