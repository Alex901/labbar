import tkinter as tk
from tkinter import ttk
import math

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Labbar")
        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self)
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text='Labb1')
        self.notebook.add(self.tab2, text='Labb2')
        self.notebook.add(self.tab3, text='Labb3')
        self.notebook.pack(expand=1, fill='both')

        self.create_tab1_widgets()
        self.create_tab2_widgets()

    def create_tab1_widgets(self):
        self.number_entry = ttk.Entry(self.tab1)
        self.number_entry.pack()
        self.result_label = ttk.Label(self.tab1)
        self.result_label.pack()
        self.calculate_button = ttk.Button(self.tab1, text="Calculate", command=self.calculate_factorial)
        self.calculate_button.pack()

    def create_tab2_widgets(self):
        self.string_entry = ttk.Entry(self.tab2)
        self.string_entry.grid(row=0, column=0, columnspan=3)  # spans across all three columns
        self.string_list = []
        self.print_button = ttk.Button(self.tab2, text="Print", command=self.print_strings)
        self.add_button = ttk.Button(self.tab2, text="Add", command=self.add_string)
        self.reset_button = ttk.Button(self.tab2, text="Reset", command=self.reset_string)

        self.print_button.grid(row=1, column=0)  # moved to the next row
        self.add_button.grid(row=1, column=1)
        self.reset_button.grid(row=1, column=2)

        self.string_display = ttk.Label(self.tab2, text=str(self.string_list))  # new label to display the string list
        self.string_display.grid(row=2, column=0, columnspan=3)

        self.string_entry.bind('<Return>', self.add_string)

    def calculate_factorial(self):
        number = int(self.number_entry.get())
        factorial = math.factorial(number) # Gissar att man ville ha en for loop ? Haha
        self.result_label.config(text=f"{number}! = {factorial}")

    def add_string(self, event=None):
        string = self.string_entry.get()
        self.string_list.append(string)
        self.string_entry.delete(0, 'end')
        self.string_display.config(text=str(self.string_list))  # update the label when a string is added

    def print_strings(self):
        fused_string = ''.join(self.string_list)
        self.string_display.config(text=fused_string)  # update the label to display the fused string

    def reset_string(self):
        self.string_list = []
        self.string_entry.delete(0, 'end')
        self.string_display.config(text=str(self.string_list))  # update the label when the list is reset

if __name__ == "__main__":
    app = Application()
    app.mainloop()