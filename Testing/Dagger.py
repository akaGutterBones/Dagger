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
            print(result)

        root = ctk.CTk()
        root.title("Dagger")
        root.geometry("600x400")
        
        index_label = ctk.CTkLabel(root, text="Subject:")
        index_label.pack()
        index_entry = ctk.CTkEntry(root)
        index_entry.pack()

        name_label = ctk.CTkLabel(root, text="Search:")
        name_label.pack()
        name_entry = ctk.CTkEntry(root)
        name_entry.pack()

        submit_button = ctk.CTkButton(root, text="Submit", command=submit)
        submit_button.pack()

        root.mainloop()

    if __name__ == "__main__":
        create_window()