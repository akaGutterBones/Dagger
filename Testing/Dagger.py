import requests, os, sys, json
import pandas as pd
import tkinter as tk
import customtkinter as ctk
from src.fetch import api_call
from src.dagger_widgets import create_label, create_combobox, create_entry, create_button, create_textbox
from tkinter import ttk
from src.json_utils import flatten_json
class Dagger:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Dagger")
        self.root.geometry("800x600")
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(4, weight=1)

    def create_window(self):
        def submit():
            index = index_combobox.get()
            name = name_entry.get()
            result = api_call(index, name)
            flattened_result = flatten_json(result)  # Flatten the JSON result
            formatted_result = json.dumps(flattened_result, indent=4)
            result_text.delete('1.0', tk.END)  # Clear the existing text
            result_text.insert(tk.END, formatted_result)
        
        response = requests.get('https://www.dnd5eapi.co/api/')
        endpoints = list(response.json().keys())
        
        index_label = create_label(self.root, "Subject:", 0, 0)
        index_combobox = create_combobox(self.root, endpoints, 0, 1)

        name_label = create_label(self.root, "Search:", 0, 2)
        name_entry = create_entry(self.root, 0, 3)

        submit_button = create_button(self.root, "Submit", submit, 0, 4)

        result_text = create_textbox(self.root, 1, 0, 5)

        self.root.mainloop()

if __name__ == "__main__":
    Dagger().create_window()