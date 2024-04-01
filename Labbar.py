import tkinter as tk                                                # Behövs för GUI
from tkinter import ttk                                             # Behövs för att skapa widgets
import math

class Application(tk.Tk):                                           # Min huvudklass, ärver från tk.Tk
    def __init__(self):                                             # Konstruktor
        super().__init__()                                          # Anropar konstruktorn i tk.Tk
        self.title("Labbar")
        self.create_widgets()                                       # Anropar metoden create_widgets

    def create_widgets(self):                                       # Metoden skapar widgets
        self.notebook = ttk.Notebook(self)                          # Skapar en "flikwidget"
        self.tab1 = ttk.Frame(self.notebook)                        # Skapar mina flikar
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text='Labb1')                  # Lägger till flikarna i "flikwidgeten"
        self.notebook.add(self.tab2, text='Labb2')
        self.notebook.add(self.tab3, text='Labb3')
        self.notebook.pack(expand=1, fill='both')                   # Expanderar och fyller ut fönstret

        self.create_tab1_widgets() 
        self.create_tab2_widgets()

    def create_tab1_widgets(self):                                  # Metoden skapar widgets för flik  1
        self.number_entry = ttk.Entry(self.tab1)                    # Skapar en inmatningsruta
        self.number_entry.pack()                                    # Lägger inmatningsrutan i fliken
        self.result_label = ttk.Label(self.tab1)                    # Skapar en label för att visa resultatet
        self.result_label.pack()                                    # Lägger labeln i fliken
        self.calculate_button = ttk.Button(self.tab1, text="Calculate", command=self.calculate_factorial)   # Skapar en knapp för att påbörja beräkningen
        self.calculate_button.pack()                                # Lägger knappen i fliken

    def create_tab2_widgets(self):                                  # Mer eller mindre samma som ovan
        self.string_entry = ttk.Entry(self.tab2)
        self.string_entry.grid(row=0, column=0, columnspan=3)       # För att få knapparna på samma rad, därför används columnspan helt plötsligt :) 
        self.string_list = []
        self.print_button = ttk.Button(self.tab2, text="Print", command=self.print_strings)
        self.add_button = ttk.Button(self.tab2, text="Add", command=self.add_string)
        self.reset_button = ttk.Button(self.tab2, text="Reset", command=self.reset_string)

        self.print_button.grid(row=1, column=0)  # moved to the next row
        self.add_button.grid(row=1, column=1)
        self.reset_button.grid(row=1, column=2)

        self.string_display = ttk.Label(self.tab2, text=str(self.string_list))  # new label to display the string list
        self.string_display.grid(row=2, column=0, columnspan=3)

        self.string_entry.bind('<Return>', self.add_string)          # Bindar enterknappen till add_string

    def calculate_factorial(self):                                  # Metoden beräknar fakulteten, man ville kanske ha en for loop här gissar jag, 
        number = int(self.number_entry.get())                       # men jag är lat. Hahah
        factorial = math.factorial(number)                          # for i in range(1, number+1): factorial *= i där.                    
        self.result_label.config(text=f"{number}! = {factorial}")

    def add_string(self, event=None):                               # Metoden lägger till en sträng i listan
        string = self.string_entry.get()                            # Hämtar strängen från inmatningsrutan
        self.string_list.append(string)                             # Lägger till strängen i listan
        self.string_entry.delete(0, 'end')                          # Tömmer inmatningsrutan
        self.string_display.config(text=str(self.string_list))      # Uppdaterar labeln med listan

    def print_strings(self):                                        # Metoden skriver ut strängarna i listan
        fused_string = ''.join(self.string_list)                    # Konkatenerar ihop strängarna i listan
        self.string_display.config(text=fused_string)               # Uppdaterar labeln med den konkatenerade strängen

    def reset_string(self):                                         # Metoden rensar listan och uppdaterar labeln
        self.string_list = []
        self.string_entry.delete(0, 'end')
        self.string_display.config(text=str(self.string_list)) 

if __name__ == "__main__":                                          # Om filen körs som huvudprogram    
    app = Application()
    app.mainloop()