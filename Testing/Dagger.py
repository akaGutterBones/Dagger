import requests, os, sys, json
import pandas as pd
import tkinter as tk
import customtkinter as ctk
from src.fetch import api_call
from tkinter import ttk
class Dagger:
    def create_window():
        def submit():
            index = index_combobox.get()
            name = name_entry.get()
            result = api_call(index, name)
            formatted_result = json.dumps(result, indent=4)  # Format the result
            result_text.delete('1.0', tk.END)  # Clear the existing text
            result_text.insert(tk.END, formatted_result)

        # Fetch the available endpoints
        response = requests.get('https://www.dnd5eapi.co/api/')
        endpoints = list(response.json().keys())

        root = ctk.CTk()
        root.title("Dagger")
        root.geometry("800x400")
        
        index_label = ctk.CTkLabel(root, text="Subject:")
        index_label.grid(row=0, column=0, padx=5, pady=5)
        index_combobox = ttk.Combobox(root, values=endpoints)  # Use the fetched endpoints as values
        index_combobox.grid(row=0, column=1, padx=5, pady=5)

        name_label = ctk.CTkLabel(root, text="Search:")
        name_label.grid(row=0, column=2, padx=5, pady=5)
        name_entry = ctk.CTkEntry(root)
        name_entry.grid(row=0, column=3, padx=5, pady=5)

        submit_button = ctk.CTkButton(root, text="Submit", command=submit)
        submit_button.grid(row=0, column=4, padx=5, pady=5)

        result_text = ctk.CTkTextbox(root, wrap=tk.WORD)  # Wrap text at word boundaries
        result_text.grid(row=1, column=0, columnspan=5, sticky='nsew')  # Make the text widget expandable

        root.grid_rowconfigure(1, weight=1)  # Make the row containing the text widget expandable
        root.grid_columnconfigure(4, weight=1)
        root.mainloop()

    if __name__ == "__main__":
        create_window()