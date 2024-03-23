import requests, os, sys, json
import pandas as pd
import tkinter as tk
import customtkinter as ctk
from src.fetch import api_call
class Dagger:
    def create_window():
        def submit():
            index = index_entry.get()
            name = name_entry.get()
            result = api_call(index, name)
            result_label.configure(text=result)

        root = ctk.CTk()
        root.title("Dagger")
        root.geometry("800x400")
        
        index_label = ctk.CTkLabel(root, text="Subject:")
        index_label.grid(row=0, column=0, padx=5, pady=5)
        index_entry = ctk.CTkEntry(root)
        index_entry.grid(row=0, column=1, padx=5, pady=5)

        name_label = ctk.CTkLabel(root, text="Search:")
        name_label.grid(row=0, column=2, padx=5, pady=5)
        name_entry = ctk.CTkEntry(root)
        name_entry.grid(row=0, column=3, padx=5, pady=5)

        submit_button = ctk.CTkButton(root, text="Submit", command=submit)
        submit_button.grid(row=0, column=4, padx=5, pady=5)

        result_label = ctk.CTkLabel(root, text="")
        result_label.grid(row=1, column=0, columnspan=5)

        root.mainloop()

    if __name__ == "__main__":
        create_window()