from tkinter import *
from tkinter import ttk
import sqlite3

class Product:

    db_name = 'PyProducts.db'

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
        ttk.Button(frame, text='Save Product', command = self.add_product).grid(row= 3, columnspan= 2, sticky= W + E)

        # Output Messages
        self.message = Label(text='', fg= 'red')
        self.message.grid(row= 3, column= 0, columnspan= 2, sticky= W + E)

        # Table Data
        self.tree = ttk.Treeview(height= 10, columns= 2)
        self.tree.grid(row= 4, column= 0, columnspan= 2)
        self.tree.heading('#0', text= 'Name', anchor= CENTER)
        self.tree.heading('#1', text= 'Price', anchor= CENTER)

        # Using the get_products method so we can see all the data displayed at the beggining of the application
        self.get_products()

    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn: # Guardamos la conexión asignandole el nombre 'conn'
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def get_products(self):
        # This is just to clean the table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # Here we are making the query
        query = 'SELECT * FROM Products ORDER BY name DESC'
        db_rows = self.run_query(query)
        # Filling the table with the supplied data
        for row in db_rows:
            #print(row)
            self.tree.insert('', 0, text = row[1], values = row[2])

    def validation(self): # This function returns true or false depending on the name and price inputs
        return len(self.name.get()) != 0 and len(self.price.get()) != 0

    def add_product(self):
        if self.validation():
            query = 'INSERT INTO Products VALUES(NULL, ?, ?)'
            parameters = (self.name.get(), self.price.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Product {} has been added successfully'.format(self.name.get())
            # Clearing the name and price inputs after adding the data
            self.name.delete(0, END)
            self.price.delete(0, END)
        else:
            self.message['text'] = 'Name And Price inputs are required'
        self.get_products() # Update the table list

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()