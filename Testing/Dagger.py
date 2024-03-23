import requests, os, sys, json
import pandas as pd
import tkinter as tk
import customtkinter as ctk

class Dagger():
    def create_window():
        root = ctk.CTk()
        root.title("Dagger")
        root.geometry("600x400")

        root.mainloop()

    if __name__ == "__main__":
        create_window()