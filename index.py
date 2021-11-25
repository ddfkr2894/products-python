from tkinter import *
from tkinter import ttk
import sqlite3

class Product:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Products Application')

        # Creating the Frame Container
        frame = LabelFrame(self.wind, text= 'Register a new Product')
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        # This is for the name input
        Label(frame, text='Name: ').grid(row= 1, column= 0)
        self.name = Entry(frame)
        self.name.focus()   # Con esta línea hacemos que al abrir la ventana este aputando a este input
        self.name.grid(row= 1, column=1)

        # This is for the price input
        Label(frame, text='Price: ').grid(row= 2, column= 0)
        self.price = Entry(frame)
        self.price.grid(row= 2, column= 1)

        # This is for the button which is going to add a product
        ttk.Button(frame, text='Save Product').grid(row= 3, columnspan= 2, sticky= W + E)

        # Table Data
        self.tree = ttk.Treeview(height= 10, columns= 2)
        self.tree.grid(row= 4, column= 0, columnspan= 2)
        self.tree.heading('#0', text= 'Name', anchor= CENTER)
        self.tree.heading('#1', text= 'Price', anchor= CENTER)

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()